POOL_LENGTH = 10


class Pool:
    def __init__(self):
        super().__init__()
        self.list = [[]]*10
        self.pool = dict()
        self.last = []

    def push(self, src):
        self.list.append(src)
        for i in src:
            if self.pool[i] == None:
                self.pool[i] = 0
            self.pool[i] += 1
        for i in list[0]:
            if self.pool[i] <= 1:
                del self.pool[i]
            else:
                self.pool_dict[i] -= 1

    def fetch(self):
        res = []
        for i in self.pool:
            if self.pool[i] > POOL_LENGTH / 2:
                res.append(i)
        return res

    def changing(self):
        right = self.fetch()
        if self.last == right:
            return [[], [self.last], []]
        else:
            left = self.last
            middle = []
            for i in left:
                if i in right:
                    middle.append(i)
            for i in left:
                del left[i]
            for i in right:
                del right[i]
            self.last = self.fetch()
            return [left, middle, right]
