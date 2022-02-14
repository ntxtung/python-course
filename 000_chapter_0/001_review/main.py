trabai = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(trabai)


def chao_max(input_list: list[int]):
    max_list = input_list[0]
    for i in input_list:
        if max_list < i:
            max_list = i
    return max_list


print(chao_max(trabai))


def chao_min(input_list: list[int]):
    min_list = input_list[0]
    for i in input_list:
        if min_list > i:
            min_list = i
    return min_list


print(chao_min(trabai))


def chao_sum(input_list: list[int]):
    sum_list = 0
    for i in input_list:
        sum_list = sum_list + i
    return sum_list


print(chao_sum(trabai))


def chao_pro(input_list: list[int]):
    pro_list = 1
    for i in input_list:
        pro_list = pro_list * i
    return pro_list


print(chao_pro(trabai))