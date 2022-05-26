first_list = [11, 1, 22, 33]
second_list = [1, 2, 3]
third_list = []


def combine_list(first_list, second_list):
    third_list = first_list + second_list
    third_list = list(set(third_list))
    print(third_list)


combine_list(first_list, second_list



