#Input: [2, 1, 5, 1, 3, 2], k=3 
#Output: 
#Time Complexity : O(N)
#Space Complexity O(1)

def sliding_Window(arr: list, k: int)->int:
    sum1 = 0
    max1 = 0
    for i in range(len(arr)-k+1):
        if i == 0:
            sum1 = sum(arr[i:i+k])
            max1 = sum1
        else:
            sum1 -= arr[i-1]
            sum1 += arr[i+k-1]

        
        if sum1 > max1:
            max1 = sum1

    return max1

if __name__ == "__main__":

    arr = [2, 1, 5, 1, 3, 2]
    k=3

    print(sliding_Window(arr, k))


    



