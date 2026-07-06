# In this project, we buld a mini AI chatbot that can interact with users. The chatbot will understand simple message like "helloo""motivate me or python and respond eith friendly intelligent answers
# this is rule based chatbot 

print("Namaste! WELCOME TO YOUR BUDDY_CHATBOT")
print("You can ask me basic question, Type 'bye' to exit from the chatbot ")

# chatbot memory creation [ dictionary of responses]

responses = {
    "hello": "Hi! 😊 Welcome. How can I help you?",
    "hi": "Hello! 😊",
    "hey": "Hey! How are you?",
    "how are you": "I am fine. Thank you for asking! 😊",
    "who are you": "I am your Buddy AI ChatBot.",
    "motivate me": "Keep going! Every bug you fix makes you a better programmer. 💪",
    "happy": "That's great to hear! 😄",
    "functions kya hote hai": "A function is a reusable block of code that performs a specific task.",
    "python": "Python is a simple, powerful, and beginner-friendly programming language.",
    "java": "Java is an object-oriented programming language widely used for software development.",
    "dsa": "DSA stands for Data Structures and Algorithms. It is very important for coding interviews.",
    "thank you": "You're welcome! I'm always here to help. 😊",
    "good morning": "Good Morning! Have a productive day! 🌞",
    "good night": "Good Night! Sweet dreams. 🌙"
}

def getresponse(userQuestion):
  userQuestion=userQuestion.lower()
  if userQuestion in responses:
    print(responses[userQuestion])
  else:
    print("Bot: Sorry, I don't know about that yet.")
    print("Bot: Try asking something about Python, Java, DSA, or motivation.")

while(True):

  userQuestion=input("Enter the question : ")
  if userQuestion.lower()=='bye':
    print("\nthank you for chattting with me ")
    print("have a great day ")
    break

  getresponse(userQuestion)



