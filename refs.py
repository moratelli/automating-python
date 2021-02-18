import copy


def eggs(someParameter):
    someParameter.append('Hello')


spam = [1, 2, 3]
cheese = copy.deepcopy(spam)
eggs(spam)
print(spam)
print(cheese)
