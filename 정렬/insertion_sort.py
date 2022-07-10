// Insertion sort
// Python

def insertion_sort(array):
    for i in range(1, len(array)):
        
        temp_value = array[i]
        position = i - 1
    
        while position >= 0:
            if array[position] > array[temp_value]:
                array[position + 1] = array[position]
                position = position - 1
            else:
                break
        
        array[position + 1] = temp_value
        
    
    return array
