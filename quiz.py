from asyncio import exceptions
import pyttsx3
engine = pyttsx3.init()


def game():
    try:
        engine = pyttsx3.init()
        engine.say("If you want to play the game Please type yes or no")
        engine.runAndWait()
        Page = input("Do you want to play game? yes/no : ")
        score = 0

        if Page.lower() != "yes":
            engine.say("BITCH!!!")
            engine.runAndWait()
            print("      #########  ######### ########## ########### #          #")
            print("      #       #      #          #     #           #          #")
            print("      #       #      #          #     #           #          #")
            print("      #       #      #          #     #           #          #")
            print("      #       #      #          #     #           #          #")
            print("      #########      #          #     #           ############")
            print("      #       #      #          #     #           #          #")
            print("      #       #      #          #     #           #          #")
            print("      #       #      #          #     #           #          #")
            print("      #       #      #          #     #           #          #")
            print("      #########  #########      #     ##########  #          #")

            quit()
        else:
            engine.say("Challange accepted!")
            engine.runAndWait()
            print("Challange start!!!")

        engine.say("What is the meaning of BIOS! : ")
        engine.runAndWait()
        quiz1 = input("What is the meaning of BIOS! : ")

        if quiz1.lower() == "basic input output system":
            print("Correct!")
            engine.say("Answer Correct!")
            engine.runAndWait()
            score += 1
        else:
            print("Incorrect!")
            engine.say("Ïncorrect!!")
            engine.runAndWait()

        engine.say("What is power supply unit AC or DC ")
        engine.runAndWait()
        quiz2 = input("What is power supply unit AC or DC : ")
        if quiz2.lower() == "dc":
            print("Correct!")
            engine.say("Answer Correct!")
            engine.runAndWait()
            score += 1
        else:
            print("Incorrect!")
            engine.say("Answer Incorrect!")
            engine.runAndWait()

        engine.say("What is CPU stand for")
        engine.runAndWait()
        quiz3 = input("What is CPU stand for : ")

        if quiz3.lower() == "central processing unit":
            print("Correct!")
            engine.say("correct!!")
            engine.runAndWait()
            score += 1
        else:
            print("Incorrect!")
            engine.say("Incorrect")
            engine.runAndWait()

        engine.say("Can we install the graphic card on the hard drive")
        engine.runAndWait()
        quiz4 = input("Can we install the graphic card on the hard drive(Yes/No) : ")

        if quiz4.lower() == "yes":
            print("Correct!")
            engine.say("Correct")
            engine.runAndWait()
            score += 1
        else:
            print("Incorrect!")
            engine.say("Incorrect")
            engine.runAndWait()

        engine.say("What is the meaning of RAM? ")
        engine.runAndWait()
        quiz5 = input("What is the meaning of RAM? : ")

        if quiz5.lower() == "random access memory":
            print("Correct!")
            engine.say("Correct")
            engine.runAndWait()
            score += 1
        else:
            print("Incorrect!")
            engine.say("Incorrect")
            engine.runAndWait()

        print("You got " + str(score) + "answers correct!!!")
        print("You got " + str((score/5) * 100) + "%.")
        engine.say("Congratuation!")
        engine.say("You got " + str(score) + "answers correct!!!")
        engine.say("You got " + str((score/5) * 100) + "%.")
        engine.runAndWait()
    except Exception:
        print("Something went wrog!")
        exit()
    finally:
        engine.say("Thank for playing with me baby. You are so sweet :) love you babe  ")
        engine.runAndWait()
        exit()
    