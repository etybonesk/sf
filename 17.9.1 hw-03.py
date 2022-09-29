y = None
y_y = False
x = None
x_x = False

while not y_y:
    try:
        y = list(map(float, input('Введите последовательность чисел через пробел:').split(' ')))
        y_y = True
    except ValueError as e:
        print('Введены нечисловые символы!')

while not x_x:
    try:
        x = float(input('Введите число для поиска ближайших:'))
        x_x = True
    except ValueError as e:
        print('Введены нечисловые символы, либо более одного числа!')

print('\n')
print(f'Последовательность для сортировки: {y}')
print(f'Число для поиска ближайших: {x}')


def sort(array):  # сортировка пузырьком по возрастанию
    for i in range(len(array)):
        for j in range(len(array) - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
    return array


def binary_search(array, element, left, right):
    if left > right:
        return False

    middle = (right + left) // 2
    if array[middle] == element or array[middle] > element > array[middle - 1]:
        # если заданное число равно элементу последовательности, либо меньше текущего элемента и больше предыдущего
        return middle
    elif element < array[middle]:
        return binary_search(array, element, left, middle - 1)
    else:
        return binary_search(array, element, middle + 1, right)


sort(y)
ff = binary_search(y, x, 0, len(y) - 1)
print(ff)

print('\n')
print(f'Последовательность, отсортированная в порядке возрастания: {y}')

print('\n')
if x == y[0]:
    print(f'Заданное число {x} является первым элементом последовательности.')
elif not ff:
    print('Заданное число не входит в заданный диапазон.')
elif x == y[ff]:
    print(f'Заданное число {x} совпадает с {ff + 1}-м элементом последовательности.')
    print(f'Предыдущий элемент последовательности: {ff}-й, равный {y[ff-1]}.')
else:
    print(f'Заданное число {x} находится между {ff}-м и {ff + 1}-м элементами последовательности,'
          f' равными {y[ff - 1]} и {y[ff]} соответственно.')
