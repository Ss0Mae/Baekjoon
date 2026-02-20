from itertools import permutations

# 두 아이디가 패턴에 맞는지 비교하는 헬퍼 함수
def match(user, ban):
    # 1. 글자 수가 다르면 절대 매칭될 수 없음
    if len(user) != len(ban):
        return False
        
    # 2. 한 글자씩 비교
    for i in range(len(user)):
        # 제재 아이디의 글자가 '*'이 아닌데, 유저 아이디와 글자가 다르다면 매칭 실패
        if ban[i] != '*' and user[i] != ban[i]:
            return False
            
    return True

# 순열로 뽑힌 유저 목록이 전체 제재 목록 패턴과 일치하는지 확인
def check_all_match(users, banned_id):
    for i in range(len(banned_id)):
        if not match(users[i], banned_id[i]):
            return False
    return True

def solution(user_id, banned_id):
    # 중복된 제재 목록을 제거하기 위해 set 사용
    answer_set = set()
    
    # 1. user_id에서 banned_id의 길이만큼 뽑는 모든 순열(경우의 수) 생성
    # user_id가 8개라면 최대 8! = 40,320번만 돌면 됨 (매우 빠름)
    for p in permutations(user_id, len(banned_id)):
        
        # 2. 뽑힌 순열(p)이 제재 아이디 패턴(banned_id)과 일치하는지 확인
        if check_all_match(p, banned_id):
            
            # 3. 일치한다면, 순서가 달라도 같은 목록으로 취급하기 위해 정렬(sorted)
            # set에 넣기 위해 리스트를 튜플(tuple)로 변환
            answer_set.add(tuple(sorted(p)))
            
    # 최종적으로 중복이 제거된 집합의 길이를 반환
    return len(answer_set)