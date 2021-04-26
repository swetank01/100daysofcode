# Don;t Change
age = input("what is your current age? ")
max = 60
# CODE HERE
age_in_year = (max - int(age))
age_in_month = (age_in_year * 12)
age_in_week = age_in_month * 52
age_in_days = age_in_week * 7

# output
print(f"\n You have {str(age_in_year)} years left, \n which is about {str(age_in_month)} months, \n that is just about {str(age_in_week)} weeks, \n hence {str(age_in_days)} days.  \n")
