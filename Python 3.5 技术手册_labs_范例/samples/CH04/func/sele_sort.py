import sys

def sele_sort(number):
    # 找出未排序中最小值
    def min_index(left, right):
        if right == len(number):
            return left
        elif number[right] < number[left]:
            return min(right, right + 1)
        else:
            return min(left, right + 1)

    for i in range(len(number)):
        selected = min_index(i, i + 1)
        if i != selected:
            number[i], number[selected] = number[selected], number[i]

number = [int(arg) for arg in sys.argv[1:]]
sele_sort(number)
print(number)