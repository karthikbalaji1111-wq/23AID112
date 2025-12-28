signal = input("Enter traffic light colour: ").lower()

if signal == "red":
    print("STOP!")
elif signal == "yellow":
    print("Get ready to start")
elif signal == "green":
    print("You can go")
else:
    print("Wrong input!")
