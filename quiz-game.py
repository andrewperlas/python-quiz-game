print("Welcome to Andrew's computer quiz!")

# Ask user if they want to play
playing = input("Do you want to play? ")

# If user's response is anything other than "yes", then end the program
# .lower() to account for any uppercase characters like "YES"
if playing.lower() != "yes":
    print("Okay, bye!")
    quit()

print("Let's play :)")
score = 0

# if/else statements to determine if user's answers are correct or not
answer = input("What does CPU stand for? ")
if answer.lower() == "central processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What does GPU stand for? ")
if answer.lower() == "graphics processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What does RAM stand for? ")
if answer.lower() == "random access memory":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What does PSU stand for? ")
if answer.lower() == "power supply unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

percent = score/4 * 100
print(f"Game over! Out of the 4 questions, you answered {score} correctly ({percent}%)")