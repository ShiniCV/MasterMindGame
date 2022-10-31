#---------------------------------------------------------------------------------------------------------------------#
#---------------------------------------------------------------------------------------------------------------------#
#                          Final Project for Introduction to python,spring 2021_22[Block course]
#---------------------------------------------------------------------------------------------------------------------#
#                                             "MASTERMIND"
#---------------------------------------------------------------------------------------------------------------------#
#Name::Shini Cherattu Valappil
#Mat.Nr:2314325
#After evaluation expecting grade and credits
#---------------------------------------------------------------------------------------------------------------------#
#OBJECTIVE:
#To create a fully functioning computer version of the MASTERMIND game using Python programming language.
#
#---------------------------------------------------------------------------------------------------------------------#
#LIMITATIONS:
#Very basic Code Breaker Game.Only 4 colours will be generated randomly and user only have 5 colours as option.
#Players not getting chance to choose colours directly they can only play with colour codes(alphabets) but after every
# guess the programm will print their guess and feedback as colours on the terminal using colorama module.
#The back ground colour should be white or light colour for the best convenience in  playing because dark colour
# especially black(feedback colour) will be difficult to see  if the terminal background colour is dark.
#
#--------------------------------------------------------------------------------------------------------------------------#
#PLANING
#-------------------------------------------------------------------------------------------------------------------------#
#
#                                             |main()|"While loop for looping game"
#                                                | 
#                                                |
#          <---------1 --------->-------------|first_look()|---------------->-------------------<--->-------3
#          |                                     |                                  |
#          |                                     |                                  ^                                 
#|instructions()|                                |2                      |invalid input|                  |Quit|                       
#                                                |
#                                                |
#                                        --------|----
#    ----------------------------------  |Lets_play()|
# |        ----------------------------- |one set of |--------------------------------------------
# |        |                             |play.      |                                           |
# |     |inpt_values()|                  |10 attempts|                ------------------|feedback()|------------
# |                                      |           |                |                                         |
# |    --------------------------------- |-----------|       color_finder()                        position_finder()
# |    |                                         |
# |  |colour_Generator()|                        |
# |                                              |
# |                                 |While loop for repeated play and stop play|
# |
#create_colours()
#                                                
#                                                
#----------------------------------------------------------------------------------------------------------------------#                                               
# ---------------------------------------------------------------------------------------------------------------------#                                         
#EXECUTING::
#----------------------------------------------------------------------------------------------------------------------#
#for generating random colours random module will help.
import random
#-----------------------------------------------------------------------------------------------------------------------#
import colorama
from colorama import Fore,Back,Style    
#colorama module we can print colored text .
#In which the methods Fore,Back help us to set colour for text and background.
#init(),in which autoreset=True indicate that print colour that we prefer
#and automaticallyback to default colour again.
colorama.init(autoreset=True)
#----------------------------------------------------------------------------------------------------------------------#
import time #time delay function for late printing headlines
#----------------------------------------------------------------------------------------------------------------------#
#FIGLet is a few lines of the code,which creates fancy text,
#in large size with the help of screen characters.FIGLet takes the ordinary
#value as well as ASCII characters as the input.Arrange in pattern and hence they appear as a big fancy text.
import pyfiglet
#-----------------------------------------------------------------------------------------------------------------------#
#PlanI:Making fancy text with the help of pyfiglet and colorama .Each of the text is printing with a time delay 2 second 
def first_look():
    """ Game start with  fancy welcome for real code breaker"""    
    headl_=[]
    #text 'WELCOME TO THE' is allocated at centre in width 110
    L=pyfiglet.figlet_format('WELCOME TO THE',justify='center',width=110)
    L1=pyfiglet.figlet_format('REAL CODE BREAKER', justify='center',width=110)
    headl_.append(L)
    headl_.append(L1)
    headlines=[headl_[0],headl_[1]]
    print(Fore.BLUE+'*'*150) #'*' is getting blue colour
    for i in range(len(headlines)):
        print(Fore.YELLOW+f'{headlines[i]}') 
        time.sleep(2) #time delays 2 seconds
        
    print(Fore.BLUE+'*'*150)
    print(Back.YELLOW+'1.How to play               ')
    print(Back.YELLOW+'2.Lets play                 ')
    print(Back.YELLOW+'3.Quit                      ')

#-----------------------------------------------------------------------------------------------------------------------#
#Plan:II
#------------------------------------------------------------------------------------------------------------------------#
    
def instructions():
    print(Fore.RED+'*'*110)
    print('\t','INSTRUCTIONS:-You are a code breaker,and your goal is to guess the secret code.')
    print(Fore.RED+'*'*110)
    print('(1)Play with alphabets instead of typing colours name on terminal\
    \n(2)5 alphabets represents 5 different colours in given colour codes\
    \n(3)you can play with both upper case and lower case\
    \n(4)Once the 4 colour code is entered,the game will check the players code and give feedback\
    \n(5)The  game will then inform the player the number of colours they have in the right and wrong position\
    \n(6)Each of your guess and feed back will be printed as  corresponding colours\
    \n(7)In your feedback the number of black colour indicates the number of colurs in the right position and\
    \n   number of red colour indicates the number of colours in the wrong position\
    \n(8) Make sure that your background colour of the terminal is white\
    \n(9)Also make sure that you have installed both module colorama and pyfiglet\
    \n(10)Colour codes: B, Y, M, G, C\
    \n    B,b=BLUE\
    \n    Y,y=YELLOW\
    \n    M,m=MAGENTA\
    \n    G,g=GREEN\
    \n    C,c=CYAN\
    \n(11)Feedback colours:\
    \n    feed back is printed in colours:BLACK COLOUR= Colours in the right position\
    \n                                    RED COLOUR = Colours in the wrong position\
    \n(12)You have 10 attempts for guessing a code.Each of your wrong choices reduce the number of attempt.')
    print('\n')

    print(Fore.RED+'*'*110)
    print('\t','WRONG CHOICES:--')
    print(Fore.RED+'*'*110)
    print('(1)No repeated alphabets,spaces,special charecters are allowed in your guess\
    \n(2)No other alphabets other than given colour codes  are allowed in your guess\
    \n(3)Tyiping colour name instead of typing corresponding colour codes also considered as wrong choice\
    \n(4)More than  or less than 4 alphabets also considered as wrong choice')
    print('\n')
    print(Fore.RED+'*'*110)
    print('GOOD LUCK....!!')
    print(Fore.RED+'*'*110)

#------------------------------------------------------------------------------------------------------------------------#
#PlanIII:::plan1 to plan6   
#-------------------------------------------------------------------------------------------------------------------------#
#plan-1:create colour list with the help of colorama module 
#-------------------------------------------------------------------------------------------------------------------------#
def create_colours(x):
    """  """            
    paint=[]
    for c in x:
        if c=='B': #string 'BLUE' will act as a piece of block in which string appear in WHITE   .
            paint.append(Fore.WHITE+Back.BLUE+'BLUE')#and background appear in colour blue
        elif c=='Y': #string'YELL'appear as WHITE and background becomes YELLOW in colour
            paint.append(Fore.WHITE+Back.YELLOW+'YELL')
        elif c=='M': #string 'MGNT'appear as WHITE  and background becomes MAGENTA
            paint.append(Fore.WHITE+Back.MAGENTA+'MGNT')
        elif c=='G': #string 'GREN' appear as  WHITE and background becomes GREEN
            paint.append(Fore.WHITE+Back.GREEN+'GREN')
        elif c=='C': #string 'CYAN' appear as WHITE and background becomes CYAN
            paint.append(Fore.WHITE+Back.CYAN+'CYAN')
        elif c=='b': #string '00'will act as a piece of block in black colour.we coudn't recognice it is 00
            paint.append(Fore.BLACK+Back.BLACK+'00')
        elif c=='r':#string '00' will act as a piece of block in red colour.we couldn't recognice it is 00.
            paint.append(Fore.RED+Back.RED+'00')
    return paint
#------------------------------------------------------------------------------------------------------------------------#
#plan2:Here computer will automatically generate a hidden list of 4 colour codes from the 5 colour code list(col_L)
#------------------------------------------------------------------------------------------------------------------------#
def colour_Generator():
    """generating 4 random colour code from a list of 5 colour code(col_L)"""
    col_L=['B','Y','M','G','C']
    return random.sample(col_L,4) #random.sample helps to generate colour codes without repeating any colour code.
#-------------------------------------------------------------------------------------------------------------------------#
##plan:3--Recieving any 4 colour codes from the given 5 colour code list 
#--------------------------------------------------------------------------------------------------------------------------#
def inpt_values(n):
    """ Taking alphabets from the player and it will convert to uppercase"""
    col_L=['B','Y','M','G','C']
    val=input(f'Guess any 4 colour codes from  given codes(Attempt:{n}):')
    val_1=list(val.upper()) #player getting a chance to type in both upper and lower case.
    return val_1 #listing 4  guessed colour codes.
#--------------------------------------------------------------------------------------------------------------------------#
##plan:3--for giving feed back we need to list  colours in the right position and in the wrong position.
#--------plan3.1:listing colour codes in the right position.--#
#--------------------------------------------------------------------------------------------------------------------------#
def position_finder(lst,lst2):
    """finding colours in the right position that is in the same index"""
    #l=0
    coms=[]
    lenf=len(lst)#length of the hidden code
    for i in range(lenf): 
        if lst[i]==lst2[i]:
            #l=l+1 #counting colours in the right position
            coms.append(lst[i]) #appending colour codes in the right position to the list coms
    return(coms)
#------------------------------------------------------------------------------------------------------------------------#
##----------plan3.2:listing colour codes in the wrong position.---#
#-----------------(a)list  colour codes without the colours in the right position(using list comprehension)
#------------------(b)intersection method which returns common elements in a set
#
#-------------------------------------------------------------------------------------------------------------------------#

def color_finder(lst,lsT):
    """listing colour codes of the player without the colours in the right position"""
    clean_lst=[element for element in lst if element not in position_finder(lst,lsT)]
    leng=set(lsT).intersection(set(clean_lst)) #finding common elements using intersection method
    return list(leng)
#-------------------------------------------------------------------------------------------------------------------------#
##plan4:Taking decision for feedback .In which how many black(right position) .
#And red(wrong position) are there in the players guess.
#---------------------------------------------------------------------------------------------------------------------------#

def feedback(b,r): #
    """Returns a list,in which how many black(right position) and red(wrong position) are there in the players guess.
        Both function position_finder and color_finder is calling here."""
    s=len(position_finder(b,r))*'b'+ len(color_finder(b,r))*'r'# finding number of black and red
    return list(s)
#--------------------------------------------------------------------------------------------------------------------------#
col_L=['B','Y','M','G','C'] #players have a list of  5 colours choice.
f_c=['b','r'] #feedbck colours,b-black,r-red.
#--------------------------------------------------------------------------------------------------------------------------#
#--------------------------------------------------------------------------------------------------------------------------#
##-plan5: while loop for 10 attempt to break the hidden code
#--------each attempt the guesser code and feedback will print in the form of  corresponding colours.
#--------Calling all other functions for executing sucessfully.
#--------------------------------------------------------------------------------------------------------------------------#
def Lets_play():

    Hidden_col=colour_Generator()#random colour codes  listed by computer for  the player to find out.
    print('\n\n')
    print('*'*110)
    print('\t'*6,'Colours corresponding to alphabets','\t\t\t''Black:right position,Red:wrong position')
    print('\n\n')
    #print colours in the terminal
    print('                                                       ',*create_colours(col_L),'\t','\t\t ',*create_colours(f_c))#
    print('\n')
    #printing colour codes in the terminal
    print('Type colour codes corresponding to the above colours:','  ',col_L[0],'  ',col_L[1],'   ',col_L[2],'  ',col_L[3],'  ',col_L[4])
    print('You can also use lower case or both upper and lowercase: b    y     m    g    c')
    print('\t')
    print('*'*110)
    print('\n\n')
    try_no=0
    n=10
    while n>0:
        que=inpt_values(n)
        check_que=[el for el in que if el not in col_L ]
        if len(que)!=4 or len(check_que)!=0 or len(set(que))!=4: #avoiding wrong choices.
            print('\t'*7,'Wrong choice!!..Try again!!')
            print('\n')
            n=n-1 #reducing attempt for each wrong choice
            try_no=try_no+1 #counting numbrt of tries
        else:
            respond=feedback(Hidden_col,que)
            print('\t\t\t\t\t\t\t*')
            print('\t '*7,'YOUR GUESS','\t'*4,'FEEDBACK')
            #printing colurs corresponding to the 4 different alphabets that player guessed
            #Also printing feedback colours ,number of black indicates number of colours in the right position.
            #number of red colour indicates number of colours in the wrong position.
            print('\t'*7,*create_colours(que),'\t'*3,*create_colours(respond))
            try_no=try_no+1
            #criteria for breaking the code,4*b(bbbb),4 black indicate the player breaked the code
            if ''.join(respond)=='bbbb':
                print('*'*110)
                print('\n\n')
                print('\n\n','Congratulations!!!.. YOU BREAK THE CODE','\t\t',*create_colours(Hidden_col))
                print(f'Yon have cracked the code with {try_no} tries')
                break
            n=n-1
    else:
        #if the player failed to crack the code within 10 attempts he will loose the game.
        print('\t' *7,'Sorry YOU LOST!!!..Better Luck next time!!')
        print('\n\n')
        print('\t'*6,'Hidden code is:',*create_colours(Hidden_col))




#-----------------------------------------------------------------------------------------------------------------------------#
#plan6:looping instructions(),Lets_play(),Quit,Also invalid input
#
#------------------------------------------------------------------------------------------------------------------------------#
def main():
    #fancy welcome to the game
    first_look()
    #--------------------------------------------------------------------------------------------------------------------------#
    #input cammand for making user friendly
    Player_option=input('Enter 1,2,3 based prompt given above:')
    #---------------------------------------------------------------------------------------------------------------------------#
    #recieving cammands from the player it direct player to the desired loop with the help of while loop
    while True:
        
        #How to play:It is all about instuctions for playing
        if Player_option=='1':
            
            #Just printing all instuctions with the help of print()
            instructions()
            Player_option=input('Enter 1,2,3 based prompt given above:')#option for going back
    #------------------------------------------------------------------------------------------------------------------------------#
            
        elif Player_option=='2':
            
            #Main Game :playing---,cracking or loosing               
            Lets_play()
            
    #---------------------------------------------------------------------------------------------------------------------------------#
    #after everysuccess or failure in craking here providing option for play again or stop or option for invalid cammand 
    #-------------------------------------------------------------------------------------#
    #"""Loop for Repeated   play: """
            Re_play=input('Do you want to play again :yes/no--:')
            print('\n\n')
            Re=1
            while Re>=0:
                if Re_play=='yes':
                                   
                    Lets_play()#main play for one set of ronud                
                    Re_play=input('Do you want to play again :yes/no--:')
                    print('\n\n')
                    Re=Re+1#infinite play option
                    
                elif Re_play=='no':
                    print('\n\n')
                    print('\t'*7,'Thank You for playing!!!...,Have a Good Day')
                    break
                else:               
                    print('\t'*7,'Invalid Input')               
                    Re_play=input('Do you want to play again :yes/no--:')#play option for each bug
                    Re=Re+1
            break
                    
                        
    #---------------------------------------------------------------------------------------------------------------------------------#   
        elif Player_option=='3':
            #quit option for the player in the initial interface
            print('\t'*7,'Thank You Have A Good Day...')        
            break
        else:
            #after every wrong input giving chance to the initial interface
            print('Invalid Command')        
            Player_option=input('Enter 1,2,3 based prompt given above:')


main()
    #--------------------------------------------------------------------------------------------------------#
    ##########################################################################################################
    #THANK YOU VERY MUCH .....
    ##########################################################################################################
    #--------------------------------------------------------------------------------------------------------#
         
    