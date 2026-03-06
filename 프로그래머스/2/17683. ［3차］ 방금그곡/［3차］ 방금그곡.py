# 1. '#'이 붙은 음표를 하나의 소문자 알파벳으로 치환해주는 헬퍼 함수
def replace_sharps(melody):
    # C# -> c, D# -> d 등으로 바꾸면 한 글자가 하나의 음표를 의미하게 되어
    # 길이를 구하거나 문자열 포함 여부(in)를 확인할 때 매우 편리해집니다.
    melody = melody.replace('C#', 'c')
    melody = melody.replace('D#', 'd')
    melody = melody.replace('F#', 'f')
    melody = melody.replace('G#', 'g')
    melody = melody.replace('A#', 'a')
    melody = melody.replace('B#', 'b')
    melody = melody.replace('E#', 'e')

        
    # 카카오 문제 조건에는 없지만 가끔 E#이나 B# 같은 엣지 케이스가 있을 때를 대비해
    # melody.replace('E#', 'e').replace('B#', 'b')를 추가해도 무방합니다.
    return melody

# 2. "HH:MM" 형식의 시간을 분(Minute) 단위의 정수로 변환하는 헬퍼 함수
def time_to_minutes(time_str):
    h, m = map(int, time_str.split(':'))
    return h * 60 + m

def solution(m, musicinfos):
    # 네오가 기억하는 멜로디의 샵(#)을 미리 치환해 둡니다.
    m = replace_sharps(m)
    
    answer_title = "(None)"
    max_duration = 0 # 가장 길게 재생된 음악을 찾기 위한 변수
    
    for info in musicinfos:
        # 3. 콤마(,)를 기준으로 정보 분리
        start_time, end_time, title, melody = info.split(',')
        
        # 4. 재생 시간(분) 계산
        duration = time_to_minutes(end_time) - time_to_minutes(start_time)
        
        # 5. 악보의 샵(#)도 치환
        melody = replace_sharps(melody)
        
        # 6. 실제 재생된 멜로디 문자열 만들기
        # 전체 재생 시간(duration)만큼 멜로디를 반복해서 늘리거나 잘라냅니다.
        # 파이썬의 문자열 곱셈(*)과 슬라이싱을 이용하면 아주 쉽습니다.
        # (duration // len(melody) + 1) 번 반복한 뒤, 앞에서부터 duration만큼 자름
        played_melody = (melody * (duration // len(melody) + 1))[:duration]
        
        # 7. 네오가 기억하는 멜로디(m)가 실제 재생된 멜로디에 포함되어 있는지 확인
        if m in played_melody:
            # 조건: 일치하는 음악이 여러 개일 때, 재생된 시간이 제일 긴 음악을 반환
            # (재생 시간이 같을 경우 먼저 입력된 음악을 반환해야 하므로 '>' 만 사용)
            if duration > max_duration:
                max_duration = duration
                answer_title = title
                
    return answer_title