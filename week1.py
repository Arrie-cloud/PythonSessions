#personalized greeting app

name = ("Harriet")
color = ("purple")

print(f"Hello, [Harriet]! Your favorite color,[purple], is awesome!")

#simple quiz game
questions = [
    ("What does the name Nairobi mean?", "A place of cool waters"),
    ("Who was the first prime minister of Kenya?", "Jomo Kenyatta"),
    ("Who was the first Kenyan to win a gold medal at the olympics?", "Naftali Temu"),
]

score = 0
for question, answer in questions:
    print(question)
    user_answer = input("Enter your answer:")
    if user_answer == answer:
        print('correct!')
        score += 1
    else:
        print("Incorrect. The answer is", answer) 
print("Your final score is:", score)

#Random joke generator
import random
jokes = [
    "Why can't a bicycle stand on its own?, it's two-tired.",
    "What do you call fake spaghetti?, An impasta!",
    "I once wrote a song about a tortilla. Well, actually it's more of a warp",
    "Why don't programmers like nature?, it has too many bugs",
]
while True:
    random_joke = random.choice(jokes)
    print(random_joke)
    #add user input
    user_input = input("Press 'q' to quit, or any other key to continue:")
    if user_input.lower() == 'q':
        break
