# Leaf Year

### Don't Change
year = int(input("Which year do you want to check? "))
### Don't Change

year_mod = year % 4

if year_mod == 0:
    print(f"{year} is a LeaF Year.")
else:
    print(f"{year} is not a Leaf Year.")