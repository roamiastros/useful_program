import time
import random
import os
import subprocess
import webbrowser
import keyboard

def pleaseRunThisCommandForMeSoIdontHaveToRunThisInCommandPrompt(command):
    subprocess.run(str(command),shell=True)
    
def iWantToGoToThisWebpagePlease(web):
    webbrowser.open(str(web))

def mathFunctionToAddNumbersThatGivesTheRightAnswerSometimes(*args):
    answer=0
    for e in args:
        answer+=e
    print(f'The answer i got was: {random.randrange(0,e*2)}')
    
def checkIfIhavePythonOnThisComputerSinceISomehowDontKnow():
    e=subprocess.check_output('python3 --version')
    e2=subprocess.check_output('python --version')
    e=str(e)
    if e[9]=='3' or e2[9]=='3':
        print('Yes! You DO have python on this device')
    else:
        print('NO! You DO NOT have python on this device (or there is a issue with python, which is more likely because this is a python script)')
        
def rollMeANonRandomDieWithANumberOfFacesDeterminedByTheNumberInTheParentheses(faces):
    if faces==0:
        print(f'Dice roll was: {0}')
    else:
        print(f'Dice roll was: {faces**0}')
        
def iNeedAEssayRightNowPleaseAiGenerateOneForMeThankYouSoMuch():
    print('enter essay to type since i cant ai generate stuff')
    ch=input('here: ')
    print('press space to type')
    keyboard.wait('space')
    randomN=random.randrange(0,2)
    if randomN==0:
        keyboard.write('ngl im too lazy to type this just like you')
    else:
        keyboard.write(ch)
        
def iLikeGamblingSoGiveMeAGamblingMinigamePleaseAndMakeItGood():
    print('COINFLIP GAMBLING SIM')
    print('you have 10 coins')
    optionList=['heads','tails']
    coins=10
    gambling=True
    high=False
    
    ch=input('enable HIGH STAKES MODE? (plz only y for yes or n for no) :')
    if ch == 'y':
        high=True
        
    while gambling:
        #print(high)
        optionList=['heads','tails']

        ch=input('continue gambling (y/n)? : ')
        if ch == 'n' or ch =='no':
            gambling=False
            print(f'you have {coins} coins')
            
        picked=False
        money=False

        while not money:
            ch=input("how much do you want to gamble: ")
            try:
                gambled=int(ch)
                if gambled>coins:
                    raise ValueError
                money=True
            except ValueError:
                print('invalid option, please enter valid option')

        while not picked:
            ch=input('heads or tails? plz only input h for heads or t for tails: ')
            if ch == 'h' or ch == 't':
                picked=True
            else:
                print('invalid option, please enter valid option')
            print()
        
        rando=random.randrange(1,3)
        
        if (coins>=20 or high) and ch=='h' and rando==1:
            optionList.append('tails')
        elif (coins>=20 or high) and ch=='t' and rando==1:
            optionList.append('heads')
                
        
        flip=random.choice(optionList)
        
        if flip == 'heads' and ch == 'h':
            if high:
                coins+=gambled
                print(f'The flip was HEADS. You get {gambled} coin(s) and have {coins} coins')
            elif not high:
                coins+=gambled
                print(f'The flip was HEADS. You get {gambled} coin(s) and have {coins} coins')
                
        elif flip == 'tails' and ch == 't':
            if high:
                coins+=gambled
                print(f'The flip was TAILS. You get {gambled} coin(s) and have {coins} coins')
            elif not high:
                coins+=gambled
                print(f'The flip was TAILS. You get {gambled} coin(s) and have {coins} coins')
        else:
            coins-=gambled
            print(f'the flip was {flip}. you lose {gambled} coin(s) and have {coins} coins')
            
        if coins==0 and high:
            print('you lose in high stakes mode. we will shutdown your computer in 30 sec')
            subprocess.run('shutdown -f -s -t 30')
            gambling=False
            
        if coins==0 and not high:
            print('you lose. :(')
            gambling=False
            
        print()
        
def iNeedMyKeyboardRandomlyMashedForSomeReasonAndICantDoItMyself(num=50):
    letters=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    print('press space to start mashing')
    keyboard.wait('space')
    for i in range(num):
        keyboard.press(random.choice(letters))

def meowTimeBaby(min_interval=30,max_interval=60):
    subprocess.Popen(f"pythonw meow.py {min_interval} {max_interval}", cwd="meow")

def executeThisFunctionForMePleaseBecauseIAmLazyAndCantDoItMyself(execute):
    execute()
    #print(execute)

def help():
    with open('README.md','r') as f:
        print(f.read())

if __name__ == '__main__':
    pass
        
        
        

    
