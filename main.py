import random

print("    Dice simulator v0.0")
print("(=========================)")
print("██████╗░██╗░█████╗░███████╗")
print("██╔══██╗██║██╔══██╗██╔════╝")
print("██║░░██║██║██║░░╚═╝█████╗░░")
print("██║░░██║██║██║░░██╗██╔══╝░░")
print("██████╔╝██║╚█████╔╝███████╗")
print("╚═════╝░╚═╝░╚════╝░╚══════╝")
print("(=========================)")

repeat = False

def rolldice():
    print(" ")
    print(" ")
    print("How many sides does your dice have?")
    sides = input()
    sides = int(sides)
    print("How many dice are you using?")
    numdice = input()
    numdice = int(numdice)
    answerd1 = random.randrange(1, sides)
    answerd2 = random.randrange(1, sides)
    total = answerd1 + answerd2
    total = str(total)
    answerd1 = str(answerd1)
    answerd2 = str(answerd2)
    print("Your results are " + answerd1 + " and " + answerd2 + " (" + total + ").")

rolldice()

