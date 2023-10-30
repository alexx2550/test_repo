def first_func(a, b):

    return a ** b

first_func(5, 8)


def second_func(c, d):
    return c + d

second_func(10, 963)


def reverse_list(ls: list):
    for i in ls:
        rev_ls = i[::-1]
        return rev_ls

ls = ['Alexnader Babayan']
print(reverse_list(ls))
