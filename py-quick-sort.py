# Quicksort Algorithm
def main():
    array = [4, 2, 5, 6, 1, 3, 10, 8, 9]
    quick_sort()


def quick_sort(array):
    if len(array) < 2:
        return array
    else:
        pivot = array[0]
        less = [i for i in array[1:] if i <= pivot]

main()
