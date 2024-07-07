def solution(num_list):
    answer = 0
    tor = 0
    for i in range(len(num_list)):
        tot =0
        while(True):
            if (num_list[i] == 1): break
            if num_list[i] % 2 == 0:
                num_list[i] = num_list[i] // 2
            else:
                num_list[i] -= 1
                num_list[i] = num_list[i] // 2
            tot += 1
        answer += tot
    return answer