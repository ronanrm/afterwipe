# take a number as a parameter
# Print true if number is within 10 of 100 and


def check_within_ten(n):
    if 100-n <=-10 or 100-n >=10:
        return("False")
    else:
        return("True")

print(check_within_ten(73))
print(check_within_ten(95))
print(check_within_ten(103))
print(check_within_ten(117))
