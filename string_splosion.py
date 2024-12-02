def string_splosion(str):
    word = " "
    for i in range(len(str)):
        word += str[:i+1]
    return word

peter = string_splosion("bomboclatt sigma rizzler ohio")
print(peter)


