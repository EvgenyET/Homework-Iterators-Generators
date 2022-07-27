nested_list = [
    ['a', 'b', 'c'],
    ['d', 'e', 'f'],
    [1, 2, None],
]

def flat_generator_list(my_list):
    for item in my_list:
        if isinstance(item, list):
            for element in flat_generator_list(item):
                yield element
        else:
            yield item


for item in flat_generator_list(nested_list):
    print(item)