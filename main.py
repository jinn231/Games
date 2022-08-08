import pyttsx3
import Rock as r
import quiz as q

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty("voice",voices[1].id)
engine.setProperty("rate", 170)

print("                                                                                     ")
print(" H         H EEEEEEEEEEEE LL            LL            OOOOOOOOOOO0       **************             ")
print(" H         H EE           LL            LL            OO        OO      *  # #    # #  *           ")
print(" H         H EE           LL            LL            OO        OO      *  # #    # #  *           ")
print(" H         H EE           LL            LL            OO        OO      *              *           ")
print(" HHHHHHHHHHH EEEEEEEEEE   LL            LL            OO        OO      *    ######    *           ") 
print(" H         H EE           LL            LL            OO        OO       * * **  * * * *           ")
print(" H         H EE           LL            LL            OO        OO            *  *                ")
print(" H         H EE           LL            LL            OO        OO            *  *                ")
print(" H         H EEEEEEEEEEEE LLLLLLLLLLLLL LLLLLLLLLLLLL OOOOOOOOOOOO            *  *                ")
print("                                                                         ******  ******           ")
print("                                                                         *            *           ")
print("                                                                         ******  ******           ")


try:
    engine.say("I am a Robot! My name is Alexia and I'm so boring right now! So let's play a game with me!")
    print("I am a Robot! \nMy name is Alexia and I'm so boring right now! So let's play a game with me!")
    engine.runAndWait()

    lst = ["quiz game","Rock/scissors/paper", "exit"]

    x = 0
    engine.say("What kind of game do you want to play?")
    print("What kind of game do you want to play?")
    engine.runAndWait()

    for i in lst:
        x = x + 1
        print(x , " . ", i)

    def main():
        usr_input = int(input("Type here to select : "))
        while usr_input != 3:
            if usr_input == 1:
                q.game()
            elif usr_input == 2:
                r.game()
            else:
                print("Please type valid number ;(")
        else:
            print("No one want to play with me. And no one love me :(")
            engine.say("No one want to play with me. And no one love me :(")
            engine.runAndWait()
            exit()

    main()
except Exception:
    print("Something went wrong!")
    exit()
finally:
    engine.say("Thanks for connecting with me baby:)")
    engine.runAndWait()
    exit()


