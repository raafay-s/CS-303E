# CS 303E Quiz 2C
# do NOT rename this file, otherwise Gradescope will not accept your submission

# Problem 1: Hiding Common Vowels
def hidingVowels(text):
    # write your solution to problem 1 here
    vowels = ["a", "e", "i", "o", "u"]
    frequencies = []
    for v in vowels:
        frequencies.append(text.lower().count(v))
    most_common = vowels[frequencies.index(max(frequencies))]
    final = ""
    for char in text:
        if char.lower() != most_common:
            final += char

    return final    

# Problem 2: Lunch Box Class
class LunchBox:
    # REMEMBER TO MAKE YOUR DATA MEMBERS PRIVATE
    def __init__(self, owner, color, items):
        self.__owner = owner
        self.__color = color
        self.__items = items

    def shareItems(self, people):
        total_people = people + 1
        shared_per_person = self.__items // total_people
        total_shared = shared_per_person * people
        self.__items -= total_shared
        return shared_per_person

    def changeColor(self, color):
        self.__color = color

    def getDescription(self):
        return f"{self.__owner}'s lunch box is {self.__color} and contains {self.__items} item(s)."

    def __str__(self):
        return f"{self.__owner}'s {self.__color} lunch box"


if __name__=="__main__":
    """
    If you want to test your code on your computer, uncomment the respective
    function call(s) below.
    
    DO NOT CALL YOUR FUNCTIONS ANYWHERE OUTSIDE OF THIS AREA
    """
    # You may, however, change these to test different components
    # print(hidingVowels("You may put test text here"))
    # lb = LunchBox("Susan", "red", 2)
    # lb.changeColor("green")
    # print(lb)
    # lb.changeColor("yellow")
    # print(lb)
    # lb.shareItems(1)
    # print(lb.getDescription())

    # DO NOT DELETE THIS PASS
    pass
    # DON'T DO IT
