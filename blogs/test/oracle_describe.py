# -*- coding:utf-8 -*-
import os.path
import cx_Oracle
import xlwt
import sys
import urllib
import os
import time
import io
import types
# from itertools import izip
import logging; logging.basicConfig(level=logging.INFO)


def connectDB(dbname='oanet'):
    if dbname == 'oanet':
        oracle_tns = cx_Oracle.makedsn('192.168.0.153', 1521, 'oanet')
        db = cx_Oracle.connect('gd_base', '11', oracle_tns)
        return db

def sqlSelect(sql,db):
    # include:select
    cr = db.cursor()
    cr.execute(sql)
    rs = cr.fetchall()
    cr.close()
    return rs


def writeTxt(name, text):  # 定义函数名
    b = 'des'
    if not os.path.exists(b):  # 判断当前路径是否存在，没有则创建new文件夹
        os.mkdir(b)
    xxoo = b + '//' + name + '.txt'  # 在当前py文件所在路径下的new文件中创建txt
    file = open(xxoo, 'wb')
   # file.write(unicode("\xEF\xBB\xBF", "utf-8"))
    file.write(text.encode("utf-8"))  # 写入内容信息
    file.close()

#导出表字段结构
def exportTabeColumn(table):
    table = table.upper()
    db = connectDB()
    sql = "select t1.column_name, data_type, data_length, data_default, nullable, comments " \
          "from (select table_name, column_name, data_type, data_length, data_default, nullable " \
          "from user_tab_cols where Table_Name = "+ table +") t1 " \
          "RIGHT JOIN (select column_name, comments " \
          "from user_col_comments where Table_Name = "+ table +") t2 " \
          "on t1.column_name = t2.column_name"
    result = sqlSelect(sql, db)
    # resultStr = "".join(list(result))
    resultStr = "('字段名称', '类型', '默认值', '是否为空 ', '备注')\n\n"
    for r in result[1:]:
        tup1 = r[0]
        tup2 = r[1]
        tup3 = r[2]
        tup4 = r[3:6]
        if tup3 is not None:
            tup2 = tup2 + '(' + tup3.__str__() + ')'
        r = tuple([tup1, tup2])
        r = r + tup4
        resultStr = resultStr + r.__str__() + '\n'
    print(resultStr)
    writeTxt('result', resultStr)

#导出字段sql
def exportTableColumnSql(table, column):
    if table is None or column is None:
        return
    table = table.upper()
    table = table.split(',')
    table_name = "("
    for t in table:
        table_name += '\'' + t + '\''
    table_name += ")"
    column = column.upper()
    db = connectDB()
    sql = "select t1.column_name, data_type, data_length, data_default, nullable, comments, data_precision, data_scale " \
          "from (select table_name, column_name, data_type, data_length, data_default, nullable, data_precision, data_scale " \
          "from user_tab_cols where Table_Name in "+ table_name +" and column_name = '"+ column +"') t1 " \
          "RIGHT JOIN (select table_name, column_name, comments " \
          "from user_col_comments where Table_Name in "+ table_name +" and column_name = '"+ column +"') t2 " \
          "on t1.column_name = t2.column_name and t1.table_name = t2.table_name"
    result = sqlSelect(sql, db)
    result_seq = ""
    for r, t in zip(result, table):
        column_type = r[1]
        if r[2] is not None and r[1] != "DATE": #类型长度不为空时，添加类型长度，DATE除外
            if r[1] == "NUMBER":    #NUMBER类型特殊处理
                if r[6] is not None:
                    column_type = r[1] + '(' + r[6].__str__() + ',' + r[7].__str__() + ')'
            else:
                column_type = r[1] + '(' + r[2].__str__() + ')'
        default = ''
        if r[3] is not None:
            default = 'default ' + r[3]
        comment = r[5]
        column_sql = 'alter table ' + t.__str__() + ' add ' + column + ' ' + column_type + ' ' + default + ';\n'\
              'comment on column ' + t.__str__() + '.' + column + ' is \'' + comment + "\';\n\n"
        print(column_sql)
        result_seq += column_sql
    writeTxt(table_name + '.' + column, result_seq)

if __name__ == '__main__':
   # exportTabeColumn('appr_handle_info')
   # exportTableColumnSql('APPR_CONTROL_CHARGE,appr_handle_info', 'Control_seq')
   if len(sys.argv) >= 3:
       exportTableColumnSql(sys.argv[1], sys.argv[2])
   else:
       print('参数缺失：table and column')



