# 👉 1. Create a class named ‘Dog’. It should have a constructor which accepts its name, age and coat color. You must perform the following operations:

# 🔴 a. It should have a function ‘description()’ which prints the name and age of the dog.
# 🔴 b. It should have a function ‘get_info()’ which prints the coat color of the dog.
# 🔴 c. Create child classes ‘JackRussellTerrier’ and ‘Bulldog’ which is inherited from the class ‘Dog’. It should have at least two methods of its own.
# 🔴 d. Create objects and implement the above functionalities.


class Dog:
    def __init__(self, name, age, coat_color):
        self.name = name
        self.age = age
        self.coat_color = coat_color

    def description(self):
        print(f"{self.name} is {self.age} years old.")

    def get_info(self):
        print(f"{self.name}'s coat color is {self.coat_color}.")


class JackRussellTerrier(Dog):
    def __init__(self, name, age, coat_color, runningSkill):
        super().__init__(name, age, coat_color)
        self.runningSkill = runningSkill

    def run(self):
        print(f"{self.name} can a runnng faster  {self.runningSkill}.")
    def focus(self):
        print(f"{self.name} has a good focus on objects.")



class Bulldog(Dog):
    def __init__(self, name, age, coat_color, strength):
        super().__init__(name, age, coat_color)
        self.strength = strength

    def snore(self):
        print(f"{self.name} can bark loudly.")

    def protect(self):
        print(f"{self.name} is a protective breed known for its strength.")



dog1 = JackRussellTerrier("rooney", 3, "black", "High")
dog2 = Bulldog("insane", 5, "dark brown", "Strong")


dog1.description()
dog1.get_info()
dog1.run()
dog1.focus()

dog2.description()
dog2.get_info()
dog2.snore()
dog2.protect()
