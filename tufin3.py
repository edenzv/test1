def is_above_age(age):
    replay = str(input("Are you above age {}? [y/n] ".format(age))).lower().strip()
    if replay == 'y':
        return True
    if replay == 'n':
        return False
    else:
        print("Wrong value, Please do it again")
        return yes_no(age)

min_age = 0
max_age = 120
avg_age = 0
tries = 0

while tries<8 and round(min_age)!=round(max_age):
    avg_age = (min_age + max_age) / 2
    tries+=1
    if is_above_age(int(avg_age)):
        min_age = avg_age
    else:
        max_age = avg_age

print("You age is {}".format(round(avg_age)))