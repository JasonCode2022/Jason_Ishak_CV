str="start - to start the car"
stp="stop - to stop the car"
hlp=""""start - to start the car
stop - to stop the car
quit - to exit"""""

print("enter you commands below:")
car_start=False
while True:
    cmd=input(">")
    if cmd.lower()=="help":
        print("""start - to start the car
stop to stop the car
quit - to exit""")

    elif cmd.lower() == "stop":
        if car_start:
            print(" the car  stopped")
            car_start = False

        else:
            print("the car already stopped")

    elif cmd.lower()=="start":
        if car_start:
            print("the  car already started")
        else:
            print("the car started")
            car_start=True
    else:
        print("invalid command")

