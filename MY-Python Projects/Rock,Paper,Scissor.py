import random
inp=("R","P","S")
s="S"
p="P"
r="R"
print("                            The Game is ")
print("                        ROCK, PAPER, SCISSOR"              )
print("                        ____________________")
print()
print("|||||||||||||||||||||||||||||||||||||||||||||||||||||||")
print("                                                      |")
print("                      THE RULE                        |")
print("                You Have only 10 life                 |")


print("            ROCK-----------> Give capital R           |")
print("            PAPER----------> Give capital P           |")
print("            SCISSOR--------> Give capital S           |")
print("   If you not Follow the  Rules ,you loSS your life   |")
print("                                                      |")
print("|||||||||||||||||||||||||||||||||||||||||||||||||||||||")

print()

for i in range(1,11):
    user = input("Enter Your Choice:")
    print("+++++++++++++++++++++")

    a = random.choice(inp)
    if s ==user:
        if s==a:
            print("'Tie' Both are gave Scisssor")

        elif s!=a and p==a:
            print("You are WIN")
            print("Computer was give Paper")
        elif r == a:
            print("You are LOSS")
            print("Computer was give Rock")



    elif r == user:

        if r == a:
            print("'Tie' Both are gave Rock")
        elif r!= a and s==a :
            print("You are WIN")
            print("Computer was gave Scissor")
        elif p==a :
            print("You are LOSS")
            print("Computer was gave Paper")



    elif p == user:

        if p == a:
            print("'Tie' Both are gave Paper")
        elif p!= a and r==a:
            print("You are WIN")
            print("Computer was gave Rock")
        elif s== a:
            print("You are LOSS")
            print("Computer was gave Scissor")

    else:
        print("Please Follow the RULE ")
    i = 10-i
    print(f"The remaining |LIFE is:{i}|")
    print()
