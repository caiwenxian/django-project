

#返回实体
class Result(object):
    def __init__(self, status=0, msg='success', data=None):
        self.status = status
        self.msg = msg
        self.data = data
    pass