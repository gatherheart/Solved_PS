from collections import defaultdict


class Test:
    def __init__(self):
        super().__init__()
        self.test = 1

    def __repr__(self):
        return False

test = defaultdict(Test)

if test['a']:
    print(test['a'].test)

if test['b']:
    print(test['b'].test)

if not test['a']:
    print(test['a'].test)

