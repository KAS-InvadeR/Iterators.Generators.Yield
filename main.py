class FlatIterator:
    def __init__(self, nested_list):
        self.nested_list = nested_list

    def __iter__(self):
        self.count_1 = 0
        return self

    def __next__(self):

        if len(self.nested_list) > self.count_1:
            if len(self.nested_list[self.count_1]):
                self.result = self.nested_list[self.count_1].pop(0)
            if not len(self.nested_list[self.count_1]):
                self.count_1 += 1
        else:
            raise StopIteration

        return self.result


nested_list = [
    ['a', 'b', 'c'],
    ['d', 'e', 'f', 'h', False],
    [1, 2, None],
    # ['df', 'asd']
    ]


def flat_generator(nested_list):
    for nested_list_id in nested_list:
        for element in nested_list_id:
            yield element


if __name__ == '__main__':
    for item in flat_generator(nested_list):
        print(item)

    for item in FlatIterator(nested_list):
        print(item)

    # flat_list = [item for item in FlatIterator(nested_list)]
    # print(flat_list)
