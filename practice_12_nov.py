def find_max():
    if a > b:
        print(a, "is bigger")
    return b
a = int(input("enter a number: "))
b = int(input("enter another number: "))
find_max()

def return_top_two(a,b,c):
    temp = [a,b,c]
    sorted(temp)
    return temp[1], temp[2]

best,next_best = return_top_two(5,78,2)

top = return_top_two(3245,56,133525464)

{} = set
