class IterDataStruct(object):

    def __init__(self):
        self.list = []
        self.index = -1

    def __iter__(self):
        return iter(self.list)

    def __next__(self):
        if self.index > len(self.list) - 1:
            raise StopIteration
        else:
            self.index += 1
        return self.data[self.index]

    def __len__(self):
        return len(self.list)

    def __setitem__(self, index, val):
        self.list[index] = val

    def __getitem__(self, index):
        return self.list[index]

    def append(self, x):
        self.list.append(x)

    def __delitem__(self, index):
        del self.list[index]

    def pop(self, id):
        self.list.pop(id - 1)

    def clear(self):
        self.list.clear()

    def gnomeSort(self):
        i = 0
        n = len(self.list)
        while i < n:
            if i and self.list[i] < self.list[i - 1]:
                self.list[i], self.list[i - 1] = self.list[i - 1], self.list[i]
                i -= 1
            else:
                i += 1
        return self.list
