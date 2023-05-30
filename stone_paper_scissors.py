from datetime import datetime
import pyttsx3
import speech_recognition as sr
import random
engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id) 
engine.setProperty('volume', 1)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def greed():
    time_hour = datetime.now().hour
    if(time_hour<12):
        greed="Good Morning"
        return greed
    elif(12<=time_hour<16):
        greed="Good Afternoon"
        return greed
    else:
        greed="Good evening"
        return greed
speak("please tell me your name")
# speak(greed()+" cherry")

def listen():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening......")
        r.pause_threshold=0.5
        r.energy_threshold=250
        audio=r.listen(source)

    try:
        inuser=r.recognize_google(audio,language="en-in") #covert into words
        print("User said: " + inuser)
    except Exception as e:
        b="please say again!!"
        print(b)
        return "None"
    return inuser

if __name__ == "__main__":
    greed()
    search_keyword=listen().lower()
    speak(greed()+search_keyword)
    speak('would you like to play this game yes or no')
    choose=listen().lower()
    if choose =='no':
        speak('thank you')
    elif choose =='yes':
        speak('lets start')
        computer_win=0
        user_win=0
        tied=0

        while True:
            a='stone'
            b='paper'
            c='scissors'
            list=[a,b,c]
            computer=random.choice(list)
            speak(a+b+c)
            user_choice=listen().lower()
            print('computer: ' + computer)
            if user_choice == computer or user_choice == computer or user_choice == computer:
                speak('match tie')
                print('match tie')
                tied+=1
            elif user_choice=='stone' and computer=='paper':
                speak('Computer wins')
                print('Computer wins')
                computer_win+=1

            elif user_choice=='stone' and computer=='scissors':
                speak('You wins')
                print('You wins')
                user_win+=1

            elif user_choice=='paper' and computer=='stone':
                speak('You wins')
                print('You wins')
                user_win+=1
            elif user_choice=='paper' and computer=='scissors':
                speak('Computer wins')
                print('Computer wins')
                computer_win+=1

            elif user_choice=='quit':
                z=computer_win+tied+user_win
                z=str(z)
                speak('total matches played '+ z )
                print('total matches played '+ z )
                speak(search_keyword +' win '+user_win +' matches')
                print(search_keyword +' win '+user_win +' matches')
                speak('computer win '+computer_win +' matches')
                print('computer win '+computer_win +' matches')
                speak('tied '+tied  +' matches')
                print('tied '+tied  +' matches')
                speak('game quit')
                print('game quit!!')
                quit()
    else:
        speak('speak again')
        choose=listen().lower()
        if choose =='no':
            speak('thank you')
        elif choose =='yes':
            speak('lets start')
            computer_win=0
            user_win=0
            tied=0

            while True:
                a='stone'
                b='paper'
                c='scissors'
                list=[a,b,c]
                computer=random.choice(list)
                speak(a+b+c)
                user_choice=listen().lower()
                print('computer: ' + computer)
                if user_choice == computer or user_choice == computer or user_choice == computer:
                    speak('match tie')
                    print('match tie')
                    tied+=1
                elif user_choice=='stone' and computer=='paper':
                    speak('Computer wins')
                    print('Computer wins')
                    computer_win+=1

                elif user_choice=='stone' and computer=='scissors':
                    speak('You wins')
                    print('You wins')
                    user_win+=1

                elif user_choice=='paper' and computer=='stone':
                    speak('You wins')
                    print('You wins')
                    user_win+=1
                elif user_choice=='paper' and computer=='scissors':
                    speak('Computer wins')
                    print('Computer wins')
                    computer_win+=1

                elif user_choice=='quit':
                    z=computer_win+tied+user_win
                    z=str(z)
                    speak('total matches played '+ z )
                    print('total matches played '+ z )
                    speak(search_keyword +' win '+user_win +' matches')
                    print(search_keyword +' win '+user_win +' matches')
                    speak('computer win '+computer_win +' matches')
                    print('computer win '+computer_win +' matches')
                    speak('tied '+tied  +' matches')
                    print('tied '+tied  +' matches')
                    speak('game quit')
                    print('game quit!!')
                    quit()

    # while True:
    #     t-=1
    #     search_keyword=listen().lower()
    #     if search_keyword == 'yes':
    #         speak('stone paper scissor')