# -*- coding:utf-8 -*-

import os

class FileOperateUtil(object):
    """
    文件操作类
    """

    @staticmethod
    def file_iterator(down_file):
        """根据文件路径获取待下载文件流"""
        content = open(down_file, 'rb+').read()
        return content

    @staticmethod
    def extract_file_name(src_file_name):
        """
        从完整路径名称中提取文件扩展名
        :param src_file_name:
        :return: 文件扩展名元组（文件路径，文件扩展名） eg:C:/tmp/test.ext --> ('C:/tmp/', '.txt')
        """
        ext_meta = os.path.splitext(src_file_name)
        return ext_meta

    @staticmethod
    def validate_folder_exists(folder, is_create=False):
        """
        判断文件目录是否存在，如果不存在则创建
        :param folder: 待判断目录
        :param is_create: 是否创建
        :return:
        """
        if not os.path.exists(folder):
            if is_create:
                os.makedirs(folder)
            else:
                raise Exception("该目录不存在，请先创建该目录")
        return True

    @staticmethod
    def validate_file_size(src_file_path, limit_size):
        """
        判断文件大小，不能小于指定文件大小，更不能大于最大文件限制
        :param src_file_path:源文件
        :param limit_size: 限制大小
        :return:
        """
        if isinstance(src_file_path, object):  # 文件对象
            file_size = src_file_path.size
        else:
            file_size = os.path.getsize(src_file_path)
        # 判断文件大小，是否小于最大文件限制
        if file_size >= settings.UPLOAD_MAX_SIZE:
            raise Exception("上传失败,文件过大，超过10M")
        else:
            if file_size >= limit_size:
                raise Exception("上传失败，文件过大")
        return True

    @staticmethod
    def copy_file_chunks(src_file_obj, dst_file_path):
        """
        文件复制到指定目录【因为chunks貌似只有从request拿到的文件流才有，所以此方法只用于文件上传】
        :param src_file_obj: 待复制文件流对象
        :param dst_file_path: 存放目标文件路径，带文件名的完整路径 如:c:/tmp/test.txt
        :return:
        """
        # 创建存放文件流对象
        destination = open(dst_file_path, 'wb+')
        try:
            # 循环源文件块对象
            for chunk in src_file_obj.chunks():
                # 将文件流写入
                destination.write(chunk)
        except Exception as e:
            log.debug("复制文件失败,%s" % e)
            os.remove(dst_file_path)
            raise Exception("复制文件失败,%s" % e)
        finally:
            log.debug("关闭文件destination")
            destination.close()
        return True

    @staticmethod
    def copy_file(src_file_path, dst_file_path):
        """
        文件复制到指定目录【任意文件】
        :param src_file_path: 待复制文件完整路径
        :param dst_file_path: 存放目标文件路径，带文件名的完整路径 如:c:/tmp/test.txt
        :return:
        """
        # 判断源文件是否是文件
        if not os.path.isfile(src_file_path):
            raise Exception("上传失败，不是一个文件!")
        # 创建存放文件流对象
        destination = open(dst_file_path, 'wb+')
        try:
            src_file = open(src_file_path, "rb+")
            # 循环源文件块对象
            for line in src_file:
                # 将文件流写入
                destination.write(line)
        except Exception as e:
            log.debug("复制文件失败,%s" % e)
            os.remove(dst_file_path)
            raise Exception("复制文件失败,%s" % e)
        finally:
            destination.close()
        return True

    @staticmethod
    def zip_dir(tar_dir_name, zip_file_name):
        """
         函数目的: 压缩指定目录为zip文件
         使用DEMO: FileOperateUtil.zip_dir("C:/tmp/", "E:/test.zip")
        :param tar_dir_name: 待压缩的目录
        :param zip_file_name:  压缩后的zip文件路径 eg:C:/tmp/test.zip
        :return: boolean ,True-成功，False-失败
        """
        file_list = []
        ret = False
        try:
            # 判断是否为文件
            if os.path.isfile(tar_dir_name):
                file_list.append(tar_dir_name)
            else:
                # 循环目录，读取文件列表
                for root, dirs, files in os.walk(tar_dir_name):
                    for name in files:
                        file_list.append(os.path.join(root, name))
            # 创建ZIP文件操作对象
            zf = zipfile.ZipFile(zip_file_name, "w", zipfile.zlib.DEFLATED)
            try:
                for tar in file_list:
                    arc_name = tar[len(tar_dir_name):]
                    zf.write(tar, arc_name)
                ret = True
            except Exception as e:
                log.debug("压缩文件发送异常，%s" % e)
                raise Exception("压缩文件发送异常")
            finally:
                zf.close()
        except Exception as e:
            log.debug("---- 压缩文件发生异常，%s --" % e)
            ret = False
        return ret

    @staticmethod
    def unzip_file(zip_file_name, unzip_dir_path):
        """
        解压zip文件到指定目录
        使用DEMO：FileOperateUtil.unzip_file("C:/tmp/test.zip", "c:/tmp/zip/")
        :param zip_file_name: 为zip文件路径，
        :param unzip_dir_path:  为解压文件后的文件目录
        :return : boolean
        """
        # 判断目标文件目录是否存在，不存在就创建
        if not os.path.exists(unzip_dir_path):
            os.mkdir(unzip_dir_path)
        # 创建zip操作对象
        zf_obj = zipfile.ZipFile(zip_file_name)
        try:
            for name in zf_obj.namelist():
                name = name.replace('\\', '/')
                if name.endswith('/'):
                    p = os.path.join(unzip_dir_path, name[:-1])
                    if os.path.exists(p):
                        # 如果文件夹存在，就删除之：避免有新更新无法复制[递归删除]
                        shutil.rmtree(p)
                    os.mkdir(p)
                else:
                    ext_filename = os.path.join(unzip_dir_path, name)
                    ext_dir = os.path.dirname(ext_filename)
                    if not os.path.exists(ext_dir):
                        os.mkdir(ext_dir)
                    outfile = open(ext_filename, 'wb')
                    try:
                        outfile.write(zf_obj.read(name))
                    except Exception as e:
                        log.debug("写文件发生异常 %s" % e)
                        raise Exception("解压文件发生异常")
                    finally:
                        outfile.close()
        except Exception as e:
            log.debug("解压文件发生异常 %s" % e)
            raise Exception(e)
            shutil.rmtree(unzip_dir_path)
        return True