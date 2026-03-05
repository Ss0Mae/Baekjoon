def solution(n, k, cmd):
    # 1. 이중 연결 리스트 초기화
    # 딕셔너리를 사용해 {현재 노드: [이전 노드, 다음 노드]} 형태로 만듭니다.
    linked_list = {i: [i - 1, i + 1] for i in range(n)}
    #print(linked_list)
    # 양 끝단의 예외 처리 (이전/다음이 없는 곳은 None으로 표시)
    linked_list[0][0] = None
    linked_list[n - 1][1] = None
    
    # 2. 삭제된 노드의 정보를 담을 스택 (Z 명령어를 위한 LIFO 구조)
    deleted = []
    
    # 3. 명령어 하나씩 실행
    for command in cmd:
        
        # [Case 1] 위로 이동 (U)
        if command[0] == 'U':
            x = int(command[2:]) # 'U 2'에서 '2'를 추출
            for _ in range(x):
                k = linked_list[k][0] # 현재 노드의 '이전 노드'로 커서 이동
                
        # [Case 2] 아래로 이동 (D)
        elif command[0] == 'D':
            x = int(command[2:])
            for _ in range(x):
                k = linked_list[k][1] # 현재 노드의 '다음 노드'로 커서 이동
                
        # [Case 3] 삭제 (C)
        elif command[0] == 'C':
            prev, next = linked_list[k]
            # 복구를 위해 스택에 (내 위치, 내 이전, 내 다음) 정보를 저장
            deleted.append((k, prev, next))
            
            # 내 윗사람과 아랫사람을 서로 연결해 줌 (나를 건너뛰게 만듦)
            if prev is not None:
                linked_list[prev][1] = next
            if next is not None:
                linked_list[next][0] = prev
                
            # 커서 이동: 삭제된 행이 맨 마지막 행이었다면 윗 행(prev)으로, 아니면 아래 행(next)으로
            if next is None:
                k = prev
            else:
                k = next
                
        # [Case 4] 복구 (Z)
        elif command[0] == 'Z':
            # 가장 최근에 삭제된 노드를 스택에서 꺼냄
            restored, prev, next = deleted.pop()
            
            # 내 윗사람과 아랫사람에게 내가 돌아왔음을 알림 (연결 복구)
            # (이때 현재 커서 위치 k는 변하지 않음)
            if prev is not None:
                linked_list[prev][1] = restored
            if next is not None:
                linked_list[next][0] = restored

    # 4. 정답 도출
    # 처음에 모두 "O"로 초기화
    answer = ["O"] * n
    
    # 스택에 여전히 남아있는 노드들만 "X"로 변경
    for node in deleted:
        answer[node[0]] = "X"
        
    return "".join(answer)