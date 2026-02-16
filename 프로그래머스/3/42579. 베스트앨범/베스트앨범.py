def solution(genres, plays):
    answer = []
    
    # 1. 정보를 담을 딕셔너리 초기화
    genre_total = {} # {장르: 총 재생 횟수}
    genre_songs = {} # {장르: [(재생 횟수, 고유 번호), ...]}
    
    # 2. 데이터 집계 (Hash Map 만들기)
    # enumerate를 써서 고유 번호(i)를 같이 가져옴
    for i, (genre, play) in enumerate(zip(genres, plays)):
        # 2-1. 장르별 총 재생 횟수 누적
        if genre not in genre_total:
            genre_total[genre] = 0
            genre_songs[genre] = []
        genre_total[genre] += play
        
        # 2-2. 노래 정보 저장 (나중에 정렬하기 위해)
        genre_songs[genre].append((play, i))
        
    print(genre_total)
    print(genre_songs)
    # 3. 장르 순서 결정 (총 재생 횟수가 많은 순으로 내림차순 정렬)
    # sorted_genres 예시: ['pop', 'classic']
    sorted_genres = sorted(genre_total.keys(), key=lambda x: genre_total[x], reverse=True)
    
    # 4. 각 장르별로 노래 2개씩 뽑기
    for genre in sorted_genres:
        # 해당 장르의 노래 리스트를 가져옴
        songs = genre_songs[genre]
        
        # 5. 노래 정렬 (다중 조건 정렬)
        # 조건 1: 재생 횟수(x[0])가 많은 순서대로 (-를 붙여서 내림차순 효과)
        # 조건 2: 재생 횟수가 같다면 고유 번호(x[1])가 낮은 순서대로 (오름차순)
        songs.sort(key=lambda x: (-x[0], x[1]))
        
        # 6. 최대 2곡까지만 answer에 추가 (슬라이싱 [:2] 활용)
        # 만약 곡이 1개라면 1개만 들어감 (파이썬 슬라이싱은 에러 안 남)
        for song in songs[:2]:
            answer.append(song[1]) # 고유 번호(index)만 추가
            
    return answer