#create fanrom 4 digit number without repeats
import random
print("This is Mastermind. A game where you will have to guess a four digit number that has no repeats and may start with a '0'.")
print("Red is printed out if there are no matches within the user's guess")
string = '1234567890'
def feedback():
    return sorted(result)
string = list(string)

def check_num():
    for n in range (4):
            if guess[n] == secret_num[n]:
                result.append("green")
            if guess[n] in secret_num[n]:
                result.append("yellow")
        if len(result) == 0:
            result.append("red")

random.shuffle(string)
#

secret_num = string[:4]

attempts = 0

result = []
while attempts < 10:
    for i in range (1,10):
        guess = str(input("Enter a four digit number: "))
        guess = list(guess)
        attempts += 1
        #guess is entered and attempts are made up one 
        check_num()
        print(result)
        result.clear()
    if attempts <10 and result == ["green", "green", "green", "green"]:
        print("you win in", attempts,"attempts!") #prints win
        attempts = 40
if attempts < 30 and attempts >10:
    print("You lose") #prints lose
