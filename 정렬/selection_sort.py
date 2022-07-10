// Selection sort

// Python

def selection_sort(arr):
    for i in range(len(arr) - 1):
        min_idx = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

// O(N^2)


-----

// C++
void sort(int *a, cont int n)
{
    for(int i = 0; i < n; i++)
        {
            int j = i;
            // a[i]와 a[n-1]사이에 가장 작은 정수를 찾는다.
            for(int k = i+1; k < n; k++)
                    if(a[k] < a[j]) j = k;
            // 교환
            swap(a[i],a[j]);
        }
}
