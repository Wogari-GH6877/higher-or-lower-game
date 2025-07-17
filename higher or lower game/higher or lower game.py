# importing different modules to our code
import random
import picture
import mydata

#this to display the logo
logo=picture.logo
print(logo)



def PlayGame():
    CorrectAnswer = 0
    checked = False

    while(not checked):
        # this to generate random people from mydata module

        people = mydata.famous_people
        person1 = random.choice(people)
        person2 = random.choice(people)
        while person1==person2:
            person2=random.choice(people)

        A = person1["followers"]
        B = person2["followers"]

        if A > B:
            winner = "A"

        elif A < B:
            winner = "B"

        print(f"Compare A: {person1['name']},a {person1['profession']},from {person1['country']}")
        vs=picture.vs
        print(vs)
        print(f"Compare B: {person2['name']},a {person2['profession']},from {person2['country']}")

        famous=input("Who has more Followers ? Type A or B : ").upper()

        if winner==famous:
            print("you get it")
            CorrectAnswer+=1
            print(f"You're right ! Current Score: {CorrectAnswer}")
        else:
            print(f"Sorry,that's wrong.Final Score: {CorrectAnswer} ")
            checked=True
PlayGame()