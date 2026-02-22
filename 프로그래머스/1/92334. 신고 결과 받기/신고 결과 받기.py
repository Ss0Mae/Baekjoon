def solution(id_list, report, k):
    # 1. 중복 신고 제거
    # 파이썬의 set을 사용하면 "무지가 콘을 여러 번 신고한 경우"를 알아서 1번으로 압축해 줍니다.
    unique_reports = set(report)
    #print(unique_reports)
    
    # 2. 상태를 기록할 딕셔너리 2개 초기화
    # reported_count: 각 유저가 "신고 당한 횟수"
    # mail_count: 각 유저가 결과 알림 "메일을 받을 횟수"
    reported_count = {user_id: 0 for user_id in id_list}
    mail_count = {user_id: 0 for user_id in id_list}
    
    #print(reported_count)
    #print(mail_count)
    
    # 3. 각 유저별로 신고 당한 횟수 집계
    for r in unique_reports:
        # "muzi frodo" -> reporter: "muzi", reported: "frodo"
        reporter, reported = r.split()
        reported_count[reported] += 1
    #print(reported_count)

    # 4. k번 이상 신고당해서 정지된 유저들을 빠르게 찾기 위해 Set으로 묶어둠
    suspended_users = set()
    for user_id, count in reported_count.items():
        if count >= k:
            suspended_users.add(user_id)
            
    # 5. 내가 신고한 사람이 정지된 유저(suspended_users)에 포함되어 있다면 메일 횟수 +1
    for r in unique_reports:
        reporter, reported = r.split()
        if reported in suspended_users:
            mail_count[reporter] += 1
            
    # 6. id_list에 담긴 유저 순서대로 메일 받을 횟수를 배열에 담아 반환
    answer = [mail_count[user_id] for user_id in id_list]
    
    return answer