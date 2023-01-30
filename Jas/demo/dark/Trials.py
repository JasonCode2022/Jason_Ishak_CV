import random
while True:
    r=random.randint(1,10)
    noot=3
    print(f"try to guess a number between 1 and 10, you have {noot} trials.")
    print(r)
    while noot >= 1:
        g = int(input("enter your guess: "))
        if g==r:
            print("you win")
            break
        elif g<r:
            if noot>1:
                print("try higher number")
        else:
            if noot>1:
                print("try lowe number")
        noot = noot -1
    else:
        print("you lost, you're out of trials. The answer was",r)

    ans=input("play again yes or no: ")
    if ans.lower()=="no":
        break
#