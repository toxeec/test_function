import random


def random_list_create(n, max_listlen=20, random_range=1000):
    final_list = []
    if n % 1 != 0:  # проверяем n на натуральность
        return final_list
    sizes = random.sample(range(1, max_listlen), n)  # генерируем уникальные длины списков
    for i in range(0, n):
        row = []
        for j in range(0, sizes[i]):
            number = random.randint(-random_range, random_range)
            row.append(number)
        if i % 2 == 0:  # сортируем списки row четные
            final_list.append(sorted(row))
        elif i % 2 != 0:  # сортируем списки row нечетные
            final_list.append(sorted(row, reverse=True))
    return final_list


def print_random_list(any_list):
    for i in range(0, len(any_list)):
        print(i, " - ", *any_list[i])


print_random_list(random_list_create(7))
