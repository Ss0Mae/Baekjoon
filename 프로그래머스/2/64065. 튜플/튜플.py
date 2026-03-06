def solution(s):
    answer = []
    
    # 1. 양 끝의 '{{' 와 '}}' 를 잘라내고, '},{' 를 기준으로 문자열을 쪼갭니다.
    # -> ['2', '2,1', '2,1,3', '2,1,3,4'] 형태로 깔끔하게 배열이 만들어집니다.
    s_list = s[2:-2].split('},{')
    
    # 2. 리스트의 요소들을 '길이가 짧은 순서대로' 정렬합니다.
    # 원소가 1개인 집합이 튜플의 1번째 원소, 2개인 집합이 2번째 원소... 가 되기 때문입니다.
    s_list.sort(key=len)
    #print(s_list)
    # 3. 중복 확인을 아주 빠르게(O(1)) 하기 위해 set을 하나 만듭니다.
    seen = set()
    
    # 4. 정렬된 집합을 순회하면서 새로운 숫자를 찾아냅니다.
    for subset in s_list:
        for num in subset.split(','):
            num_int = int(num)
            
            # 처음 보는 숫자라면 정답 배열에 넣고, 본 적 있다고 seen에 기록합니다.
            if num_int not in seen:
                answer.append(num_int)
                seen.add(num_int)
                
    return answer