def solution(num_list):
    answer = []
    tot_even = 0
    tot_odd = 0
    for i in range(len(num_list)):
        if num_list[i] % 2 == 0:
            tot_even += 1
        else:
            tot_odd +=1
    answer.append(tot_even)
    answer.append(tot_odd)
    return answer