#task6 problem 2 prepared by Bekzat Bakytbek

# N = 6
A = [1, 5, 2, 4, 0]
# N = 8
B = [2, 6, 1, 4, 3, 1, 10]

def solution(A):
    result = 0
    for i in range(len(A)):
        for j in range(len(A)):
            if (i != j):
                c = (j - i)**2 + (A[i])**2 - (A[j])**2
                if (c > 1): # if c = 1, then circumferences are touching each other, but not intersecting
                    result = result + 1
    if (result > 10000000):
        result = -1
    return result

output1 = solution(A)

print("Result: ", output1)

output2 = solution(B)

print("Result: ", output2)
