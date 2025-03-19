# def chceck_palindrome(i ,n):
#     if i >= n // 2:
#         return True
#     if arr[i] != arr[n - i  - 1]:
#         return False
#     return chceck_palindrome(i+1, n)

# arr = input()
# print(chceck_palindrome(0, len(arr)))


# def get_all_subsequences(i, temp):
#     if i >= n:
#         print(temp)
#         return
#     temp.append(arr[i])
#     get_all_subsequences(i+1, temp)
#     temp.pop()
#     get_all_subsequences(i+1,temp)

# arr = list(map(int, input().split()))
# n = len(arr)
# get_all_subsequences(0, [])


def get_all_subseq_whose_sum_is_k(i, temp):
    if i >= n:
        if sum(temp) == k:
            print(temp)
        return
    temp.append(arr[i])
    get_all_subseq_whose_sum_is_k(i+1,temp)
    temp.pop()
    get_all_subseq_whose_sum_is_k(i+1,temp)

arr = list(map(int, input().split()))
n = len(arr)
k = int(input())
get_all_subseq_whose_sum_is_k(0, [])