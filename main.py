while True:
    user_input = input("Enter a character: ")
    
    try:
        user_input = int(user_input)
        continue
    
    except:
        pass
    
    for i in range(3):
        print(user_input, end=" ")
    
    if user_input == "x" or user_input == "X":
        break
    print()

