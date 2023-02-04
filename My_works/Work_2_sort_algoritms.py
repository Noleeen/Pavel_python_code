# СОРТИРОВКА СЛИЯНИЕМ

# слияние двух отсортированных списков------------
def list_mergin(l1, l2):
    fin_list = []
    size1 = len(l1)
    size2 = len(l2)

    i = 0
    j = 0

    while i < size1 and j < size2:
        if l1[i] <= l2[j]:
            fin_list.append(l1[i])
            i += 1
        else:
            fin_list.append(l2[j])
            j += 1
    # if size1 > size2:
    #     while i < size1:
    #         fin_list.append(l1[i])
    #         i += 1
    # else:
    #     while j < size2:
    #         fin_list.append(l2[j])
    #         j += 1
    # в PYTHON можно записать проще:

    fin_list += l1[i:] + l2[j:]
    return fin_list

# рекурсивная функция, которая делит список пополам пока в списке не окажется 1 элемент, а потом собирает сортируя с пом ф-ии merge

def list_sort(l):
    half = len(l) // 2
    res_list1 = l[:half]
    res_list2 = l[half:]

    if len(res_list1) > 1:
        res_list1 = list_sort(res_list1)
    if len(res_list2) > 1:
        res_list2 = list_sort(res_list2)

    return list_mergin(res_list1, res_list2)


my_list = [5,1,8,6,9,4,2,1,7,8]

print(list_sort(my_list))