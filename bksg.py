import random
userscore=0
computerscore=0
for i in range(0,99):

    list_cards=["spade", "hearts", "diamonds", "club"]
    dict_cards= {"spade":0, "hearts":1, "diamonds":2, "clubs":3}
    print("")
    print("Welcome to Bhikar-Savkar game, Select your card color")
    print("")
    print("")
    print(dict_cards)
    print("")
    print("")

    y= int(input("Enter  card color you want to select:" ))
    print("")
    print("")
    print("")


    print(" player1 has selected" , list_cards[y])
    print("")
    print("")

    x=random.randint(0,3)
    print("Computer plays:",list_cards[x])
    print('')
    if x==y:
    
        print("Computer wins")
        computerscore+=1
    else:
        print("player1 wins")
        userscore+=1
    print ("Final Scores: " + "Computer " , str(computerscore) + "  Player1 ", str(userscore) )
    print("")
    z = input("press any key to play again  Or press q to quit")
    if z=="q":
        break
    else:
        continue