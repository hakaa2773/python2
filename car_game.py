command = ""
start = False

while command.upper() != "QUIT" :
    command = input(">").upper()
    if command == "HELP":
        print("start = car start")
        print("stop = car stop")
        print("quit = end the game")
    elif command =="START":
        if start:
            print("car is already started")
        else:
            start=True
            print("Car is starting")
    elif command == "STOP":
        if not start:
            print("car is already stop")
        else:
            start=False
            print("car is stopping")
    elif command == "QUIT":
        print("Closing")
    else:
        print("I dont get it")







