// Linear Search

// Python

def linear_search(element, list):
    for i in range(len(list)):
            if element == list[i]:
                    return i
    return None

// 입출력
print(linear_search(2, [2, 3, 5, 7, 9]))
