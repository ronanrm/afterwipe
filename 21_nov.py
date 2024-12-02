import turtle
rooms = { "room1":  {'e': 'room2'}
          'room2':  {'s': 'room5' , 'e': 'room3' , 'w': 'room1'}
          'room3':  {'w': 'room2'} 
          'room4':  {'e': 'room5'}
          'room5':  {'n': 'room2', 'e': 'room6', 'w': 'room4'}
          'room6':  {'w': 'room5'}
def choose_direction(rooms):
    print("you are in room",rooms,)
    print(rooms[room.keys()])
    choice = input('which direction do you want to go in?')
    
