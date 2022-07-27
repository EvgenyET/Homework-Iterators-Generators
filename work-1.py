nested_list = [
    ['a', 'b', 'c'],
    ['d', 'e', 'f', 'h', False],
    [1, 2, None],
]

class FlatIteratoPresent:
    def __init__(self, lst):
        self.lst = sum(lst, [])

    def __iter__(self):
        self.index = -1
        return self

    def __next__(self):
        self.index += 1
        if self.index == len(self.lst):
            raise StopIteration
        else:
            return self.lst[self.index]


for item in FlatIteratoPresent(nested_list):
    print(item)

print("_______________________")
print()

flat_list = [item for item in FlatIteratoPresent(nested_list)]
print(flat_list)