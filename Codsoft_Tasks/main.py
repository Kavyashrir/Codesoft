def simple_chatbot(user_input):
    # Convert user input to lowercase for case-insensitive matching
    user_input = user_input.lower()

    # Define predefined rules and responses
    if "hello" in user_input:
        return "Hi there! How can I help you?"

    elif "how are you" in user_input:
        return "I'm just a computer program, but thanks for asking!"

    elif "bye" in user_input:
        return "Goodbye! Have a great day."

    else:
        return "I'm sorry, I didn't understand that. Can you please rephrase or ask something else?"

# Example usage:
user_query = input("User: ")
response = simple_chatbot(user_query)
print("Bot:", response)