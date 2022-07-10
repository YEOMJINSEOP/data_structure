//Binary Search

//Python

def binary_search(array, search_value):
    left = 0
    right = len(array) - 1

// left와 right를 조정하면서 원하는 값을 찾아가는 과정
    while left < right:
        
        midpoint = (left + right) / 2
                
                // 원하는 값을 찾은 경우
        if search_value == array[midpoint]:
            return midpoint
                
                // 원하는 값이 중간 지점의 값보다 작은 경우
        elif search_value < array[midpoint]:
            right = midpoint - 1
        
                // 원하는 값이 중간 지점의 값보다 큰 경우
        elif search_value > array[midpoint]:
            left = midpoint + 1

        // while 문을 돌았음에도 찾지 못한 경우 -1 return
    return -1

//입출력
print(binary_search([1,2,3,4,5,6,7,8,9], 3))



-----


// C++
