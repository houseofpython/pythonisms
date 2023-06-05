

class MyCollection:
    def __init__(self):
        self.items = ['Kennedi','Ariella','Tina']

    def __iter__(self):
        yield from self.items

    def to_list(self):
        return list(self)

my_collection = MyCollection()

for item in my_collection:
    print(item)

plus_me = [item + 'Tre' for item in my_collection]
print(plus_me)

my_list = my_collection.to_list()
print(my_list)