

#返回实体
class Result(object):
    def __init__(self, code=0, msg='success', data=None):
        self.code = code
        self.msg = msg
        self.data = data
    pass