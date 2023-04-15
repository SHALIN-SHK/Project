import gtts
import os
from playsound import playsound
import random


# function for voice output to given text(speech)
def text_speech(speech):
    speech_file = gtts.gTTS(speech) # passing text to gtts function
    speech_file.save("hello.mp3")# title of sound file


    playsound("hello.mp3")


    os.remove("hello.mp3")# deletes file each time it runs


# returns rock, paper , scissor for computer
def random_generator():
    rint = random.randint(0,2)
    if rint == 0:
        return 'rock'
    elif rint == 1:
        return 'scissor'
    elif rint == 2:
        return 'paper'


# check who wins 
def winner(user_choice, comp_choice):
    if user_choice == comp_choice:
        return 'draw'
    elif comp_choice == 'paper' and user_choice == 'rock':
        return 'computer wins'
    elif comp_choice == 'rock'  and user_choice == 'scissor':
        return 'computer wins'
    elif comp_choice == 'scissor' and user_choice == 'paper':
        return 'computer wins'
    else:
        return 'user wins'


# user input validity
def validity(user_input):
    valid_tpl = ("rock", "paper","scissor")
    if user_input.lower() in valid_tpl:
        return True
    else:
        return False


# the result shown to user
def output_text(user_choice, comp_choice, result):
    if result == 'draw':
        text_speech(f"You entered {user_choice} and computer picks {comp_choice} ")
        print("it's a draw")
        text_speech("it's a draw")


    elif result == 'computer wins':
        text_speech(f"You entered {user_choice} and computer picks {comp_choice} ")
        print("computer wins")
        text_speech("computer wins")


    else:
        text_speech(f"You entered {user_choice} and computer picks {comp_choice} ")
        print("user wins")
        text_speech("user wins")


# scores counter
def scores(result,scores_list):
    if result == 'draw':
        scores_list[0] += 1
    elif result == 'user wins':
        scores_list[1] += 1
    else:
        scores_list[2] += 1
    return scores_list


        
scores_list = [0, 0, 0] #draw count, user win count, computer win count


# main coding
flag = True
while flag:
    text_speech('please enter rock, paper or scissors') 
    user_choice = input("please enter rock, paper or scissors: ")
    user_choice = user_choice.lower()


    check = validity(user_choice)


    while check is False:
        text_speech("error! please enter the given options")
        user_choice = input("error! please enter the given options: ")
        check = validity(user_choice)


    comp_choice = random_generator()
    result = winner(user_choice,comp_choice)
    output_text(user_choice,comp_choice,result)
    scores_list = scores(result, scores_list)
    
    condt = input("Continue:(yes/no)").lower()
    if condt.lower() != "yes":
        flag = False


else:
    text_speech("Thank you for playing")
    print(f"""\n\t\t-----scoreboard-----\n
    \tNumber of draws: {scores_list[0]}
    \tuser wins:{scores_list[1]}
    \tcomputer wins:{scores_list[2]}""")
import gtts
import os
from playsound import playsound
import random


# function for voice output to given text(speech)
def text_speech(speech):
    speech_file = gtts.gTTS(speech) # passing text to gtts function
    speech_file.save("hello.mp3")# title of sound file


    playsound("hello.mp3")


    os.remove("hello.mp3")# deletes file each time it runs


# returns rock, paper , scissor for computer
def random_generator():
    rint = random.randint(0,2)
    if rint == 0:
        return 'rock'
    elif rint == 1:
        return 'scissor'
    elif rint == 2:
        return 'paper'


# check who wins 
def winner(user_choice, comp_choice):
    if user_choice == comp_choice:
        return 'draw'
    elif comp_choice == 'paper' and user_choice == 'rock':
        return 'computer wins'
    elif comp_choice == 'rock'  and user_choice == 'scissor':
        return 'computer wins'
    elif comp_choice == 'scissor' and user_choice == 'paper':
        return 'computer wins'
    else:
        return 'user wins'


# user input validity
def validity(user_input):
    valid_tpl = ("rock", "paper","scissor")
    if user_input.lower() in valid_tpl:
        return True
    else:
        return False


# the result shown to user
def output_text(user_choice, comp_choice, result):
    if result == 'draw':
        text_speech(f"You entered {user_choice} and computer picks {comp_choice} ")
        print("it's a draw")
        text_speech("it's a draw")


    elif result == 'computer wins':
        text_speech(f"You entered {user_choice} and computer picks {comp_choice} ")
        print("computer wins")
        text_speech("computer wins")


    else:
        text_speech(f"You entered {user_choice} and computer picks {comp_choice} ")
        print("user wins")
        text_speech("user wins")


# scores counter
def scores(result,scores_list):
    if result == 'draw':
        scores_list[0] += 1
    elif result == 'user wins':
        scores_list[1] += 1
    else:
        scores_list[2] += 1
    return scores_list


        
scores_list = [0, 0, 0] #draw count, user win count, computer win count


# main coding
flag = True
while flag:
    text_speech('please enter rock, paper or scissors') 
    user_choice = input("please enter rock, paper or scissors: ")
    user_choice = user_choice.lower()


    check = validity(user_choice)


    while check is False:
        text_speech("error! please enter the given options")
        user_choice = input("error! please enter the given options: ")
        check = validity(user_choice)


    comp_choice = random_generator()
    result = winner(user_choice,comp_choice)
    output_text(user_choice,comp_choice,result)
    scores_list = scores(result, scores_list)
    
    condt = input("Continue:(yes/no)").lower()
    if condt.lower() != "yes":
        flag = False


else:
    text_speech("Thank you for playing")
    print(f"""\n\t\t-----scoreboard-----\n
    \tNumber of draws: {scores_list[0]}
    \tuser wins:{scores_list[1]}
    \tcomputer wins:{scores_list[2]}""")
import gtts
import os
from playsound import playsound
import random


# function for voice output to given text(speech)
def text_speech(speech):
    speech_file = gtts.gTTS(speech) # passing text to gtts function
    speech_file.save("hello.mp3")# title of sound file


    playsound("hello.mp3")


    os.remove("hello.mp3")# deletes file each time it runs


# returns rock, paper , scissor for computer
def random_generator():
    rint = random.randint(0,2)
    if rint == 0:
        return 'rock'
    elif rint == 1:
        return 'scissor'
    elif rint == 2:
        return 'paper'


# check who wins 
def winner(user_choice, comp_choice):
    if user_choice == comp_choice:
        return 'draw'
    elif comp_choice == 'paper' and user_choice == 'rock':
        return 'computer wins'
    elif comp_choice == 'rock'  and user_choice == 'scissor':
        return 'computer wins'
    elif comp_choice == 'scissor' and user_choice == 'paper':
        return 'computer wins'
    else:
        return 'user wins'


# user input validity
def validity(user_input):
    valid_tpl = ("rock", "paper","scissor")
    if user_input.lower() in valid_tpl:
        return True
    else:
        return False


# the result shown to user
def output_text(user_choice, comp_choice, result):
    if result == 'draw':
        text_speech(f"You entered {user_choice} and computer picks {comp_choice} ")
        print("it's a draw")
        text_speech("it's a draw")


    elif result == 'computer wins':
        text_speech(f"You entered {user_choice} and computer picks {comp_choice} ")
        print("computer wins")
        text_speech("computer wins")


    else:
        text_speech(f"You entered {user_choice} and computer picks {comp_choice} ")
        print("user wins")
        text_speech("user wins")


# scores counter
def scores(result,scores_list):
    if result == 'draw':
        scores_list[0] += 1
    elif result == 'user wins':
        scores_list[1] += 1
    else:
        scores_list[2] += 1
    return scores_list


        
scores_list = [0, 0, 0] #draw count, user win count, computer win count


# main coding
flag = True
while flag:
    text_speech('please enter rock, paper or scissors') 
    user_choice = input("please enter rock, paper or scissors: ")
    user_choice = user_choice.lower()


    check = validity(user_choice)


    while check is False:
        text_speech("error! please enter the given options")
        user_choice = input("error! please enter the given options: ")
        check = validity(user_choice)


    comp_choice = random_generator()
    result = winner(user_choice,comp_choice)
    output_text(user_choice,comp_choice,result)
    scores_list = scores(result, scores_list)
    
    condt = input("Continue:(yes/no)").lower()
    if condt.lower() != "yes":
        flag = False


else:
    text_speech("Thank you for playing")
    print(f"""\n\t\t-----scoreboard-----\n
    \tNumber of draws: {scores_list[0]}
    \tuser wins:{scores_list[1]}
    \tcomputer wins:{scores_list[2]}""")
