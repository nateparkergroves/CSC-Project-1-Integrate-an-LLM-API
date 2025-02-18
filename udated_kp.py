import ollama

def initialize_game():
    """Initialize the game with a system message."""
    return [
        {
            'role': 'system',
            'content': 'You are a gamemaster running a text-based adventure game. Keep track of the user inputs and try to build a story '
                       'following the game as it continues. Keep the content of the story appropriate for a PG-13 rating. '
                       'If you notice that the user wants to quit, prompt them to enter "q" into the input. The first response should '
                       'be the theme the user wants. After that, prompt them with ways to continue the story and continue. You should end '
                       'the story within about 10 messages or less in a logical manner. Summarize the story at the end of the prompts then tell '
                       'the player to enter "q" to quit.'
        }
    ]

def get_user_input(prompt):
    return input(prompt).strip().lower()

def get_adventurer_name(prompt):
    while True:
        name = get_user_input("What is your adventurer's name? ")
        if name:
            return name
        print("Please enter a valid name.")


def play_game():
    conversation = initialize_game()
    print("Welcome to this Text-Based Adventure Game!")
    
    adventurer_name = get_adventurer_name()
    
    conversation.append({
    'role': 'system',
    'content': f"The adventurer's name is {adventurer_name}. Use this name throughout the story to personalize the experience."
    })
    
    print("Enter 'play' to start the game or 'q' to quit.")

    user_input = get_user_input("> ")
    if user_input != 'play':
        print("Goodbye!")
        return

    while True:
        try:
            response = ollama.chat(
                model='llama3.2',
                messages=conversation,
                options={'temperature': 0}
            )
            system_message = response["message"]["content"]
            print(system_message)

            if "enter 'q' to quit" in system_message.lower():
                break

            user_input = get_user_input("> ")
            if user_input == 'q':
                print("Thanks for playing! Goodbye!")
                break

            conversation.append({
                'role': 'user',
                'content': user_input
            })

        except Exception as e:
            print(f"An error occurred: {e}")
            break

if __name__ == "__main__":
    play_game()
