#task6 problem 3 prepared by Bekzat Bakytbek

def solution(A):
    if len(A) % 2 == 0:
        print("massive should be with odd elements in it")
    else:
        pairs = []
        for i in range(len(A)):
            count = 0
            for j in range(len(A)):
                if (A[i] == A[j]):
                    count = count + 1
            pairs.append([A[i], count])

        for i in range(len(pairs)):
            if (pairs[i][1]%2 != 0):
                res = pairs[i][0]
        return res

A = [9, 3, 9, 3, 9, 7, 9]

out = solution(A)

print("Value in list without a pair:", out)

A = [9, 3, 9, 3, 9, 7, 9, 7]

out = solution(A)

print("Value in list without a pair: ", out)

A = [1, 3, 1, 3, 9, 5, 9]

out = solution(A)

print("Value in list without a pair: ", out)
