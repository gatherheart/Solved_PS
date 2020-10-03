INF = 0xFFFFFFFF

def flush(result, compressed):
    for compressed_key in compressed:
        occurence = str(compressed[compressed_key]) if compressed[compressed_key] != 1 else ""
        result += occurence + compressed_key
    
    compressed.clear()
    return result

def solution(s):
    answer = INF
    prev_key = ""
    len_of_string = len(s)
    
    for unit in range(1, len_of_string + 1):
        compressed = {}
        result = ""
        for i in range(0, len_of_string + 1 - unit, unit):
            key = s[i:i+unit]
            
            # Start of Occurence
            if not key in compressed and prev_key == key:
                # rollback
                len_of_prev = len(prev_key)
                result = result[:-len_of_prev]
                compressed[key] = 2
                
            # Occurence
            elif key in compressed and prev_key == key:
                compressed[key] += 1
            # Flush
            elif prev_key != key:
                result = flush(result, compressed)
                result += key
                
            prev_key = key
        
        # Flush
        remains = s[i + unit:]
        result = flush(result, compressed)
        result = result + remains
        result_length = INF if result == "" else len(result)
        answer = min(answer, result_length)

    return answer