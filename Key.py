class Key:
    def __init__(self):
        self.key_list = []
        self.current = 1
    def getKey(self):
        if len(self.key_list) == 0:
            curr = self.current
            self.current+=1
            return curr
        else:
            self.key_list = sorted(self.key_list)
            return self.key_list.pop(0)
    def returnKey(self,key):
        self.key_list.append(key)
    def __repr__(self):
        return f'maxKey: {self.current}'