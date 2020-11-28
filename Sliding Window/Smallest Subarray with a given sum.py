#Input: [2, 1, 5, 2, 3, 2], S=7 
#Output: 2
#Explanation: The smallest subarray with a sum great than or equal to '7' is [5, 2].

#Problem Statement
#Given an array of positive numbers and a positive number ‘S,’ find the length of the smallest contiguous subarray whose sum is greater than or equal to ‘S’. 
# Return 0 if no such subarray exists.


def sliding_window(arr: list, s: int)-> list:
    window_start = 0
    window_end = 0
    window_sum = 0
    min_length = float('inf')
    result = []

    for i in range(len(arr)):
        window_start = i
        while(window_end < len(arr)):
            window_sum = sum(arr[window_start:window_end+1])
            if window_sum >= s:
                temp_length = len(arr[window_start:window_end+1])
                if temp_length < min_length:
                    min_length = temp_length
                    result = arr[window_start:window_end+1]
                    #print(result)
                break
            window_end += 1
        window_sum = 0
    return len(result)

if __name__ == "__main__":

    #1
    arr = [2, 1, 5, 2, 3, 2]
    s=7
    print(sliding_window(arr,s))

    #2
    arr = [2, 1, 5, 2, 8]
    s=7
    print(sliding_window(arr,s))

    #3
    arr = [3, 4, 1, 1, 6]
    s=8
    print(sliding_window(arr,s))



        


