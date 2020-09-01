class Dog:
    species = "Canis familiaris"
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __str__(self):
        return f"{self.name} is {self.age} years old"

    def speak(self, sound):
        return f"{self.name} says parent {sound}"

class JackRussellTerrier(Dog):
    def run(self, speed="30"):
        return f"{self.name} speed {speed}"

    def speak(self, sound="Arf"):
        return f"{self.name} says child {sound}"

miles = JackRussellTerrier("Miles", 4)
print(miles.speak("vou"));
print(miles.run("100"));
parent = Dog("Miles2", 4)
print(parent.speak("vou"))


# class Dog:
#     species = "Canis familiaris"
#
#     def __init__(self, name, age, breed):
#         self.name = name
#         self.age = age
#         self.breed = breed
#
#     # def description(self, color):
#     #     return f"{self.name} is {self.age} years old {color} color"
#
# class
#
# a = Dog("Buddy", 9)
# print(a.name)
# # print(a.description("black"))
