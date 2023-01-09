class animal:
    pass


class pets(animal):
    pass


class dog(pets):
    def bark(self):
        print("dog is barking")


obj=dog()
obj.bark()
