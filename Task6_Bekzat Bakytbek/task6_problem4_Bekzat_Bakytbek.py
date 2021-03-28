#task6 problem 4 prepared by Bekzat Bakytbek

def solution(A,B):

    alive = len(A)

    direction = 0
    for i in range(len(B)):
        direction = i
        if B[i] != 0:
            break

    newList = []
    for j in range(direction, len(B)):
        if B[j] == 1:
            newList.append(j)

        while B[j] == 0 and len(newList) > 0:
            if A[j] > A[newList[-1]]:
                newList = newList[:-1]
                alive -= 1
            else:
                alive -= 1
                break
    return alive


A = [4, 3, 2, 1, 5]
B = [0, 1, 0, 0, 0]

out = solution(A,B)

print("Alive # of fish: ", out)


A = [4, 3, 2, 1, 5]
B = [0, 1, 0, 1, 1]

out = solution(A,B)

print("Alive # of fish: ", out)


A = [4, 3, 2, 1, 5, 7]
B = [0, 1, 0, 1, 1, 0]

out = solution(A,B)

print("Alive # of fish: ", out)
