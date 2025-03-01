import random

words= [
    "lion", "elephant", "tiger", "giraffe", "zebra", "kangaroo", "panda",
    "dolphin", "eagle", "crocodile", "penguin", "wolf", "gorilla",
    "hippopotamus", "cheetah", "fox", "bear", "octopus", "owl", "deer",
    "apple", "banana", "orange", "mango", "grapes", "pineapple",
    "watermelon", "strawberry", "blueberry", "papaya", "pomegranate",
    "kiwi", "avocado", "cherry", "pear", "plum", "fig", "coconut",
    "guava", "lychee"
]
#randomly choosing
guess_word=random.choice(words)
print(guess_word)

#display ------
for i in range(len(guess_word)):
    print("-",end="")
#user entry
print("\n")
life=5
hidden_word=["-"]*len(guess_word)
while life>=0:
    print("Word :", "".join(hidden_word))
    user_letter=input("Guess letter  of  fruit/animal\n").lower()
    if user_letter in guess_word:
        for i in range(len(guess_word)):
            if guess_word[i]== user_letter:
                hidden_word[i]=guess_word[i]
    else:
        print("Sorry! Try again")
        life-=1
        if life==4:
            print("""
                     ------
                     |    |
                     |
                     |
                     |
                     |
                     =========""",)
        elif life==3:
            print(""" 
                     ------
                     |    |
                     |    O
                     |
                     |
                     |
                     =========""",)
        elif life==2:
            print("""
                     ------
                     |    |
                     |    O
                     |   /|\
                     |
                     |
                     =========""",)
        elif life==1:
            print("""
                    ------
                     |    |
                     |    O
                     |   /|\
                     |    |
                     |
                     =========""",)
        elif life==0:
            print("""
                     ------
                     |    |
                     |    O
                     |   /|\
                     |    |
                     |   / \
                     ========= """,)
            



    
            



