// Bubble sort

// Python
def bubble_sort(list):
        unsorted_until_index = len(list) - 1
        sorted = False

        While not sorted:
                sorted = True
                for i in range(unsorted_until_index):
                        if list[i] > list[i+1]:
                                list[i], list[i+1] = list[i+1], list[i]
                                sorted = False
                unsorted_until_index -= 1

        return list


// 모든 배열 크기에 적용되도록 표현하면 원소 N개가 있을 때,
// (N-1) + (N-2) + (N-3) ... + 1 번의 비교를 수행한다.
// O(N^2)
