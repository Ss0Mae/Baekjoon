def solution(array, commands):
    answer = []
    for i in range(len(commands)):
        sliceArray= array[commands[i][0] -1 : commands[i][1]]
        sliceArray.sort()
        answer.append(sliceArray[commands[i][2]-1])
    return answer