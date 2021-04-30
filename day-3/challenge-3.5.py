# Love 

### Don;t Change this
print("Welcome to The Love Calc ")
name1 = input("What is your name : ")
name2 = input("What is her name : ")
### Don;t Change this

# Write your code below this line 👇

add_name = name1 + name2
togther_name = add_name.lower()

T = togther_name.count("t") # 1
R = togther_name.count("r") # 1
U = togther_name.count("u") 
E = togther_name.count("e") # 1

L = togther_name.count("l")
O = togther_name.count("o")
V = togther_name.count("v")
E = togther_name.count("e") #1

first = T + R + U + E 
second = L + O + V + E

score = str(first) + str(second)
love_score = int(score)

if love_score > 40 and love_score < 50:
    print(f"your score is {love_score}, you are together like coke and mentos.")
elif love_score < 10 or love_score > 90:
    print (f"your score is {love_score}, you are alright together.")
else:
    print(f"Your Score is {love_score}")