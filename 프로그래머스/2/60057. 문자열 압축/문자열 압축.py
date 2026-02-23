def solution(s):
    if len(s) == 1:
        return 1
    
    min_length = len(s)
    
    for step in range(1, len(s)//2 +1):
        compressed=""
        prev = s[0:step]
        count = 1
        
        for j in range(step,len(s),step):
            current = s[j:j+step]
            
            if prev == current:
                count += 1
            else:
                if count >= 2:
                    compressed += str(count) + prev
                else:
                    compressed += prev
                prev = current
                count = 1
        
        if count >= 2:
            compressed += str(count) + prev
        else:
            compressed += prev
        
        min_length = min(min_length, len(compressed))
    return min_length