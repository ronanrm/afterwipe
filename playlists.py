#list songs


import random 
#ask user to input a choice

# 1 move first song to the end

# 2 move last song to beggining


# 3 swaps first two songs

# 4 shuffles playlist

# 5 plays each song on spereate line

def button1():
    songs.append(songs[0])
    songs.remove(songs[0])

def button2():
    songs.insert(0,songs[-1])
    songs.pop[-1]


def button3():
    pass

def button4():
    rand.sort.songs()

def button5():
    print(songs)
songs = ['a', 'b', 'c', 'd', 'e']


print("""Key:
1 will move the first song to the end
2 will move the last song to the beggining
3 will swap the first two songs
4 will shuffle the  playlist
5 will play the playlist""")

i = input("Please input a number 1-5: ")

while i != 5:
    if i == 1:
        button1()
    if i == 2:
        button2()
    if i == 3:
        button3()
    if i == 4:
        button4()
    i = input("Please input a number 1-5: ")
    if i == 5:
        print(songs) 







    




