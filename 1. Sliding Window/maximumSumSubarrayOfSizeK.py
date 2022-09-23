def max_sub_array_of_size_k(k, arr):
    # TODO: Write your code here
    sumTemp = 0
    sumResult = 0
    start = 0

    for i in range(len(arr)):
        sumTemp += arr[i]
        if i >= k - 1:
            sumResult = max(sumResult, sumTemp)
            sumTemp -= arr[start]
            start += 1

    return sumResult
