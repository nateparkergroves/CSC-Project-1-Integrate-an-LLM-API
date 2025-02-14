import ollama
user_input = ''
conversation = [
    {
        'role': 'system',
        'content': 'You are running a gamemaster running a  text based adventure game. Keep track of the user inputs and try to build a story\
                   following the game as it continues. Keep the content of the story appropriate for a PG-13 rating. \
                   If you notice that the user wants to quit, prompt them to enter "q" into the input. The first response should\
                   be the theme the user wants. After that, prompt them with ways to continue the story and continue. You should end'+
                   ' the story within about 10 messages or less in a logical manner. Summarize the story at the end of the prompts then tell'+
                   'the player to enter "q" to quit.',
    }]
print("Enter 'q' to quit or 'play' to play.")
while True:
    if user_input == 'q':
        break
    response = ollama.chat(
        model='llama3.2',
        messages=conversation,
        options={'temperature': 0})
    conversation.append({
        'role': 'system',
        'content': response["message"]["content"]
    })
    user_input = input(f'{response["message"]["content"]}\n')
    conversation.append({
        'role': 'user',
        'content': user_input
    })

