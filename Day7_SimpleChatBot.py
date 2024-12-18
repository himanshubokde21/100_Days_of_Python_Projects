import random
def ChatBotRes(userIn):
    responses = {
        "hello": ["Hi there!", "Hello!", "Greetings!"],
        "hi": ["Hi there!" , "Greetings!"],
        "how are you": ["I'm doing great!", "Feeling good, thanks!", "All good here!"],
        "name": ["I'm a simple chatbot.", "My name is ChattyBot.", "Just call me Bot."]
        }
    for key in responses:
        if key == userIn:
            return random.choice(responses[key])
    return "I'm not sure how to respond to that."
        
            
def UserRes():
    print("Chatbot: Hello! Type 'bye' to exit.")
    while True:
        userIn = input('user: ')
        userIn = userIn.lower()
        if userIn == 'bye':
            print('Chatbot: Goodbye!')
            break
        res = ChatBotRes(userIn)
        print('Chatbot: ', res)
if __name__ == '__main__':
    UserRes()



