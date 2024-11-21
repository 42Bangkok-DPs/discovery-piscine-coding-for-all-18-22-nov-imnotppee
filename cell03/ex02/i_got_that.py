while True:
    # input
    user_input = input("What you gotta say? : ")
    
    # Check "STOP"
    if user_input == "STOP":
        break
    
    # Display
    print(f"I got that! Anything else? : {user_input}")