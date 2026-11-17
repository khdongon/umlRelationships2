class person: 
    def __init__(self, name, age):
        self.name = name 
        self.age = age

    def displayinfo(self):
        print(f"Person(name='{self.name}', age={self.age})")

person1 = person("Lina", 20)
person1.displayinfo()

