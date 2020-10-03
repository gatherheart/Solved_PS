import re
from collections import defaultdict

HTTPS_PATTERN = r"\b((:?https?://(www[.])?([a-zA-Z0-9\-]+[.])*[a-zA-Z]{2,4})(/[a-zA-Z0-9\-]*)*)"
META_PATTERN = '<meta [a-z]+="[a-z]+:url" content="({})"/>'.format(HTTPS_PATTERN)
HREF_PATTERN = '<a href="({})">'.format(HTTPS_PATTERN)
WORD_PATTERN = '([a-zA-Z]*({})[a-zA-Z]*)'

def solution(word, pages):  
    answer = 0
    page_set = {}
    refered = defaultdict(list)
    total_score = {}
    results = []
    
    for page in pages:
        curr_url = re.search(META_PATTERN, page, re.IGNORECASE).group(1)
        print(curr_url)
        refering_to = list(map(lambda x: x[0], re.findall(HREF_PATTERN, page)))
        for _to in refering_to:
            refered[_to].append(curr_url) 
        
        score = len(list(filter(lambda x: x[0].lower() == word.lower(), 
                            re.findall(WORD_PATTERN.format(word), page, re.IGNORECASE))))

        page_set[curr_url] = (score, refering_to)
        
    #print(page_set)
    for page_id in page_set:
        basic_score, curr_refering = page_set[page_id]
        froms = refered[page_id]
        link_score = 0
        #print(froms)
        for _from in froms:
            _from_basic_score, _from_refering = page_set[_from]
            print("From", _from_basic_score, _from_refering)
            link_score += _from_basic_score / len(_from_refering)
            
        #print(page_id, link_score + basic_score)
        results.append(link_score + basic_score)
        
    answer = max(range(len(results)), key=lambda x: results[x])
    return answer

if __name__ == "__main__":

    test = 2
    
    if test == 1:
        word, pages = "blind", ["<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://a.com\"/>\n</head> \n<body>\nBlind Lorem Blind ipsum dolor Blind test sit amet, consectetur adipiscing elit. \n<a href=\"https://b.com\"> Link to b </a>\n</body>\n</html>", "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://b.com\"/>\n</head>  \n<body>\nSuspendisse potenti. Vivamus venenatis tellus non turpis bibendum, \n<a href=\"https://a.com\"> Link to a </a>\nblind sed congue urna varius. Suspendisse feugiat nisl ligula, quis malesuada felis hendrerit ut.\n<a href=\"https://c.com\"> Link to c </a>\n</body>\n</html>", "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://c.com\"/>\n</head>  \n<body>\nUt condimentum urna at felis sodales rutrum. Sed dapibus cursus diam, non interdum nulla tempor nec. Phasellus rutrum enim at orci consectetu blind\n<a href=\"https://a.com\"> Link to a </a>\n</body>\n</html>"]
    
    if test == 2:
        word, pages = "Muzi", ["<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://careers.kakao.com/interview/list\"/>\n</head>  \n<body>\n<a href=\"https://programmers.co.kr/learn/courses/4673\"></a>#!MuziMuzi!)jayg07con&&\n\n</body>\n</html>", "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://www.kakaocorp.com\"/>\n</head>  \n<body>\ncon%\tmuzI92apeach&2<a href=\"https://hashcode.co.kr/tos\"></a>\n\n\t^\n</body>\n</html>"]

    
    print(solution(word, pages))