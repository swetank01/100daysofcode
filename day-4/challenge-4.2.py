# Banker Roulette (ru-e-at) 
import random

friends_in_party = input("enter friends names who are going to have party:")
friends_list = friends_in_party.split(", ")
friends_length = int(len(friends_list))
random_integer = random.randint(0,friends_length - 1)

print(f"{friends_list[random_integer]} is going to buy the meal today!")