import re

class CustomFile:
    
    def __init__(self, name):
        super().__init__()
        self.original_name = name
        self.HEAD = '([a-zA-Z-\s]+)'
        self.NUMBER = '([0-9]{1,5})'
        self.TAIL = '([a-zA-Z0-9-\s]*(?:[.][a-zA-Z0-9]+)?)'
        
        self.head = None
        self.number = None
        self.tail = None
        
        self.convert(name)
        
    def convert(self, name):
        
        self.head, self.number, self.tail = \
            re.search(self.HEAD+self.NUMBER+self.TAIL, name).groups()
        
        self.head = self.head.lower()
        self.number = int(self.number)
        
        return
        
    def __repr__(self):
        return self.original_name

def solution(files):
    answer = []
    for _file in files:
        answer.append(CustomFile(_file))
    
    answer.sort(key=lambda x: (x.head, x.number))
        
    return list(map(lambda x: x.original_name, answer))


if __name__ == "__main__":

    test = 4
    
    if test == 1:
        files = ["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"]
        answer = ["img1.png", "IMG01.GIF", "img02.png", "img2.JPG", "img10.png", "img12.png"]

    if test == 2:
        files = ["F-5 Freedom Fighter", "B-50 Superfortress", "A-10 Thunderbolt II", "F-14 Tomcat"]
        answer = ["A-10 Thunderbolt II", "B-50 Superfortress", "F-5 Freedom Fighter", "F-14 Tomcat"]

    if test == 3:
        files = ["muzi1.txt", "MUZI1.txt", "muzi001.txt", "muzi1.TXT"]
        answer = ["A-10 Thunderbolt II", "B-50 Superfortress", "F-5 Freedom Fighter", "F-14 Tomcat"]

    if test == 4:
        files = ["aa 123456", "aa 12345"]
        answer = []
        
    print(solution(files))
