def shutdown():
    user_input = input("Enter your choice: ")
    
    if user_input == "yes":
        print("shutting down")
    elif user_input == "no":
        print("abort shut down")
    else:
        print("sorry")
shutdown()

 