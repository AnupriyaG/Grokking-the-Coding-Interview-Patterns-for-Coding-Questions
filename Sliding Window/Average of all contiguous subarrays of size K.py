#input : Array: [1, 3, 2, 6, -1, 4, 1, 8, 2], K=5
# output: Output: [2.2, 2.8, 2.4, 3.6, 2.8]
import time

#Brute Force approach
#Time complexity O(N*k)
#Space Complexity(K)
def brute_force(arr: list, k: int) -> list:
    result = []
    for i in range(len(arr)-k+1):
        sum = 0
        for j in range(i, i+k):
            #if not (i+k > len(arr)):
            sum += arr[j]
        result.append(sum/k)
    return result
            

#Sliding window
#Time complexity O(N)
#Space Complexity(K)
def sliding_window(arr: list, k: int) -> list:
    result=[]
    sum1 =0
    for i in range(len(arr)-k+1):
        if i == 0:
            sum1 = sum(arr[i:i+k])
        else:
            sum1 -= arr[i-1]
            sum1 += arr[i+k-1]
        result.append(sum1/k)
    
    return result



if __name__ == "__main__":
    arr = [1, 3, 2, 6, -1, 4, 1, 8, 2]
    k =5

    start = time.time()
    print("brute force :",brute_force(arr,k))
    print('--- %s seconds ---' % (time.time() - start))

    start = time.time()
    print("sliding window :",sliding_window(arr,k))
    print('--- %s seconds ---' % (time.time() - start))


