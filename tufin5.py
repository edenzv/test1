

class Numbers:
    def _init_(self):
        Self.num1 = 1
        Self.num2 = 2

class Letters:
    def _init_(self):
        Self.leta = 1
        Self.letb = 2

class Collection(object):
    def _init_(self, dict):
        self.numbers = dict.numbers
        Self.letters = dict.letters


collection = {'numbers': {'num1': 1, 'num2':2}, 'letters': {'leta': 'a', 'letb': 'b'}}

col = Collection(collection);

print(col)
