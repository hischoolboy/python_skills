from schema import Schema, And, Use, Optional


testjson1 = Schema([{'name': And(Use(str)), 'age': And(int)}])


def testjson(input):

    if testjson1.is_valid(input):
        return True
    return False




if __name__ == '__main__':

    print(Schema(int).is_valid(10))

    input1 = [{'name': {'a':  'a'}, 'age': 2}]
    print(testjson(input1))

    print(str({'a':  'a'}))

    print(str('a'))
    print(repr('a'))
