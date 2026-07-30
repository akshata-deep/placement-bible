# Problem 3 – Traffic Signal

# Take input:

# Red
# Yellow
# Green

# Print:

# Red → Stop
# Yellow → Wait
# Green → Go
# Anything else → Invalid Signal



trafic_light = input("Enter the colour :")

match trafic_light:
    case "Red":
        print("Red → Stop")
    case "Yellow":
        print("Yellow → Wait")
    case "Green":
        print("Green → Go")
    case _:
        print("invalid signal")