import random
import pyttsx3

def game():

    engine = pyttsx3.init()
    engine.say("Welcome! Let's start the game.")
    engine.runAndWait()

    user_score = 0
    computer_score = 0

    option = ["rock","scissors", "paper"]

    try:
        while True:

            user_pick = input("Type rock,scissors,paper or q to quit : ").lower()

            if user_pick == "q":
                quit()

            random_number = random.randint(0, 2)
            computer_pick = option[random_number]
            print("Computer pick: " + computer_pick)

            if user_pick == computer_pick:
                print("Draw!")
                engine.say("Draw!")
                engine.runAndWait()
                continue

            if user_pick in option:
                if user_pick == "rock" and computer_pick == "scissors":
                    print("You win!")
                    user_score += 1
                    engine.say("You win!")
                    engine.runAndWait()

                elif user_pick == "scissors" and computer_pick == "paper":
                    print("You win!")
                    user_score += 1
                    engine.say("You win!")
                    engine.runAndWait()

                elif user_pick == "paper" and computer_pick == "rock":
                    print("You win!")
                    user_score += 1
                    engine.say("You win!")
                    engine.runAndWait()

                else:
                    print("computer win!")
                    engine.say("compute win!")
                    engine.runAndWait()
                    computer_score += 1
            else:
                continue
    except Exception:
        print("Something went wrong!")
    finally:
        print("You win ", user_score , "times.")
        print("Computer win ", computer_score , "times.")
        print("GoodBye")
        engine.say("Thank for playing with me baby. You are so sweet :) love you babe ")
        engine.runAndWait()