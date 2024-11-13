import random
import art

def select_option(return_1,return_2):
    pass
def winner(lose_data):
    pass
def analyse(user_input,a,b):
    pass
def find_person(folowers):
    pass

data ={
    "Cristiano Ronaldo :Football contracts, endorsement deals, business investments " : 589000000,
    "Lionel Messi :Football contracts, endorsement deals, business investments" :281000000,
    "Selena Gomez :Instagram posts, music albums, actor, brand endorsements and her makeup line Rare Beauty" : 250000000,
    "Kylie Jenner :TV Personality, Model, Entrepreneur" : 394000000,
    "Dwayne Johnson :Wrestling, Acting, Business, Brand endorsements" : 384000000
}

#introduction
# print(art.high())
# print("\n\n")
print("welcome to the high and lower game")
print("you need to choose an option from give option which have higher insta follower.")
print("let start the game ................")

#duplication option

def find_person(folowers):
    global data

    for person,followers in data.items():
        if followers == folowers:
            return person


def duplicate(option_1):
    option_2 = random.choice(list(data))
    if option_2 == option_1:
        option_2 = random.choice(list(data))
    return option_2


#options

option_1 = random.choice(list(data))
option_2 = duplicate(option_1)



# compare
win_count = 0

def analyse(user_input,a,b):
    global data
    global win_count

    if user_input == "a":
        if data[a]>data[b]:
            win_count += 1
            print(f"you win this round and total win is : {win_count}")
            winner(data[b])

            return
        else:
            print(f"you loss this match ! and total wins are {win_count}")
            return
    if user_input =="b":
        if data[b]>data[a]:
            win_count +=1
            print(f"you win this round and total win is : {win_count}")
            winner(data[a])

            return
        else:
            print(f"you loss this match ! and total wins are {win_count}")
            return

#winner
def winner(lose_data):
    a = find_person(lose_data)
    b = duplicate(a)
    select_option(a,b)

#player to choose an option

right_entry = 0

def select_option(return_1,return_2):
 global right_entry
 global win_count

 print(f"A. {return_1}\n")


 print(f"B. {return_2}\n")

 while right_entry ==0:
    selected_input = input(print("Enter answer 'A' and 'B' from given option :")).lower()
    if selected_input == "a":
        analyse(selected_input,return_1,return_2)
        right_entry = 1
    elif selected_input == "b":
        analyse(selected_input,return_1,return_2)
        right_entry = 1
    else:
        print("enter the valid input")



select_option(option_1,option_2)





