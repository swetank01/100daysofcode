# Condition

## If Else
#if Condition:
#    do this
#else: 
#    do this

## Nested If Else

#height = int(input("Enter your Height in cm: "))
#age=int(input("Enter Age: "))
#if height >= 120:
#    print("Can Ride")
#    if age >= 18:
#        print("Ticket: $12")
#    else:
#        print("Ticket: $7")
#else:
#    print("Can't Ride")


### if - elif - else

height = int(input("Enter your Height in cm: "))
age=int(input("Enter Age: "))
bill=0
if height >= 120:
    print("Can Ride")
    if age < 12:
        bill=5
        print(f"Ticket: ${bill}")
    elif age <= 18:
        bill=8
        print(f"Ticket: ${bill}")
    else:
        bill=12
        print(f"Ticket: ${bill}")
    
    photoshoot = input("Do you want to take photo:")
    if photoshoot == "yes":
        bill += 3
        print(f"Total bill is ${bill}")
    else:
        print(f"Total bill is ${bill}")
else:
    print("Can't Ride")