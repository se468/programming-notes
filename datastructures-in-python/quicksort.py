def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) - 1]
    ind = len(arr) - 1
    left, right = 0, len(arr) - 2
    print('original', arr)
    while left < right:
        if arr[left] <= pivot:
            left += 1
        elif arr[right] >= pivot:
            right -= 1
        else:
            arr[left], arr[right] = arr[right], arr[left]
    if arr[right] > pivot:
        arr[right], arr[len(arr) - 1] = arr[len(arr) - 1], arr[right]
        ind = right
    print('after', arr)
    left_arr = quicksort(arr[0 : ind])
    right_arr = quicksort(arr[ind + 1:])

    return left_arr + [arr[ind]] + right_arr

arr = [2,1,8,4,7,2,3]
print(quicksort(arr))
