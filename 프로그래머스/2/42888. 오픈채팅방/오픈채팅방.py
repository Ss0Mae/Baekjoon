def solution(record):
    answer = []
    uid_to_nickname = {} # 유저 아이디(Key)와 최종 닉네임(Value)을 매핑할 딕셔너리
    
    # [1차 순회] 최종 닉네임 상태만 먼저 확정 짓기
    for r in record:
        parts = r.split() # 공백을 기준으로 명령어, 아이디, 닉네임 분리
        cmd = parts[0]
        uid = parts[1]
        
        # Enter(입장)이거나 Change(변경)일 때만 닉네임이 주어지므로 딕셔너리 갱신
        if cmd == "Enter" or cmd == "Change":
            nickname = parts[2]
            uid_to_nickname[uid] = nickname
            
    # [2차 순회] 완성된 딕셔너리를 바탕으로 결과 메시지 만들기
    for r in record:
        parts = r.split()
        cmd = parts[0]
        uid = parts[1]
        
        # 최종 닉네임을 딕셔너리에서 가져와서 메시지 조립
        if cmd == "Enter":
            answer.append(f"{uid_to_nickname[uid]}님이 들어왔습니다.")
        elif cmd == "Leave":
            answer.append(f"{uid_to_nickname[uid]}님이 나갔습니다.")
        
        # Change 명령어는 메시지를 출력하지 않으므로 무시합니다.
            
    return answer