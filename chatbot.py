from datetime import datetime

def chatbot():
    print("🤖 Chatbot: Hi there! I'm ChatBot. Type 'bye' to exit.\n")

    while True:
        user_input = input("You: ").lower().strip()

        # Exit condition
        if user_input in ["bye", "exit", "quit"]:
            print("🤖 Chatbot: Goodbye! Have a great day 😊")
            break

        # Greetings
        elif "hello" in user_input or "hi" in user_input:
            print("🤖 Chatbot: Hello! How are you doing today?")

        # Asking about well-being
        elif "how are you" in user_input:
            print("🤖 Chatbot: I'm just a program, but I'm feeling great! How about you?")

        # Asking for name
        elif "your name" in user_input:
            print("🤖 Chatbot: I'm your friendly Python chatbot 🤖")

        # Asking time
        elif "time" in user_input:
            now = datetime.now().strftime("%H:%M:%S")
            print(f"🤖 Chatbot: The current time is {now}")

        # Asking about date
        elif "date" in user_input:
            today = datetime.now().strftime("%Y-%m-%d")
            print(f"🤖 Chatbot: Today's date is {today}")

        # Asking about weather
        elif "weather" in user_input:
            print("🤖 Chatbot: I can’t check the weather yet, but I hope it’s nice outside!")

        # Thank you response
        elif "thank" in user_input:
            print("🤖 Chatbot: You're very welcome! 😊")

        # Default fallback
        else:
            print("🤖 Chatbot: Sorry, I didn’t understand that. Could you rephrase?")

# Run the chatbot
if __name__ == "__main__":
    chatbot()
