# startup message to show that the chatbot is running
print("ChatBot is running, Type something\n")

# boolean variable to control the loop
running = True

while(running):
    # ask the user for input
    user_message = input("You: ").lower()
    
    # check if the user greets the chatbot
    if user_message == "hello" or user_message == "hi" or user_message == "hey":
        print("ChatBot: Hi!") 
    
    # check if the user asks how the chatbot is doing
    elif user_message == "how are you" or user_message == "how are you doing":
        print("ChatBot: I'm fine, thanks!")
        
    # check if the user ends the conversation
    elif user_message == "bye" or user_message == "stop":
        print("ChatBot: Goodbye!")
        # stop the loop
        running = False
        
    # handle unrecognized input
    else:
        print("I dont understand!")