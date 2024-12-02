import random
def make_random_list(a, start, end):
    randlist = []
    for i in range(a):
        randlist.append(random.randint(start,end))
    return randlist

a = int(input("Enter how many random values you want to be displayed: "))

start = int(input("What is the beginning of the random range: "))

end = int(input("What is the end of the random range: "))


print("Printing ", a," random numbers...")

peter = make_random_list(a,start,end)
print(peter)
