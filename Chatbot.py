def rule_based_chatbot():
    print("Chatbot: Hello! I am a rule-based assistant. Type 'exit' or 'bye' to quit.")
    
    while True:
        user_input = input("You: ").strip().lower()

        if user_input in ["exit", "bye", "goodbye", "see you"]:
            print("Chatbot: Goodbye! Have a great day!")
            break
            
        elif user_input in ["hello", "hi", "hey", "greetings"]:
            print("Chatbot: Hello there! How can I help you today?")

        elif "how are you" in user_input or "how's it going" in user_input:
            print("Chatbot: I'm just a computer program, but I'm functioning perfectly! Thanks for asking.")

        elif "your name" in user_input or "who are you" in user_input:
            print("Chatbot: I am TaskBot, a simple rule-based chatbot created in Python.")

        elif "what can you do" in user_input or "help" in user_input:
            print("Chatbot: I can answer basic greetings, tell you my name, or say goodbye. Try asking 'who are you?'.")

        else:
            print("Chatbot: I'm sorry, I don't understand that. Could you try phrasing it differently?")

if __name__ == "__main__":
    rule_based_chatbot()
