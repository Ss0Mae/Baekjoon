def solution(answers):
    ans_2 = [2,1,2,3,2,4,2,5]
    ans_3 = [3,1,2,4,5]
    score = [0,0,0]
    result = []
    for i in range(len(answers)):
        j = i % 5
        if answers[i] == j + 1:
            score[0] += 1
    for idx, answer in enumerate(answers):
         if answer == ans_2[idx % len(ans_2)]:
             score[1] += 1
    for i in range(len(answers)):
        j = i //2
        ans_idx = j % 5
        if answers[i] == ans_3[ans_idx]:
            score[2] +=1
    for idx, s in enumerate(score):
        if s == max(score):
            result.append(idx+1)
    return result