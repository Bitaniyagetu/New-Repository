if_continue = 1
def chapter_one_loss():
    print("you fall")
def chapter_two_loss():
    print("you drown")
def chapter_three_loss():
    print("you burn")

def chapter_one():
    player_health = 3
    #question 1
    print("You find yourself at the entrance of the dungeon. pick 1 or 2")
    print("1. Knock on the door.")
    print("2. Sneak into the dungeon.")
    answer = int(input(""))
    if answer == 1:
        print("The dragon hears you and attacks. You lose one health point.")
        player_health = player_health-1
    elif answer == 2:
        print("You have succesfully entered the dungeon.")
    #question 2
    print("Question 2")
    print("option 1")
    print("option 2")
    answer = int(input(""))
    if answer == 1:
        print("The dragon hears you and attacks. You lose one health point.")
        player_health = player_health-1
    elif answer == 2:
        print("You have succesfully entered the dungeon.")
    #question 3
    print("question 3")
    print("1")
    print("2")
    answer = int(input(""))
    if answer == 1:
        print("The dragon hears you and attacks. You lose one health point.")
        player_health = player_health-1
    elif answer == 2:
        print("You have succesfully entered the dungeon.")
        
    return(player_health)

def chapter_two():
    player_health = chapter_one()
    if player_health >= 1:
        #question 1
        print("question 1")
        print("1")
        print("2")
        answer = int(input(""))
        if answer == 1:
            print("The dragon hears you and attacks. You lose one health point.")
            player_health = player_health-1
        elif answer == 2:
            print("You have succesfully entered the dungeon.")
        if player_health < 1:
            chapter_two_loss()
        else:
            #QUESTION 2
            print("question 2")
            print("1")
            print("2")
            answer = int(input(""))
            if answer == 1:
                print("The dragon hears you and attacks. You lose one health point.")
                player_health = player_health-1
            elif answer == 2:
                print("You have succesfully entered the dungeon.")
            if player_health < 1:
                chapter_two_loss()
            else:
                #QUESTION 3
                print("question 3")
                print("1")
                print("2")
                answer = int(input(""))
                if answer == 1:
                    print("The dragon hears you and attacks. You lose one health point.")
                    player_health = player_health-1
                elif answer == 2:
                    print("You have succesfully entered the dungeon.")
                if player_health < 1:
                    chapter_two_loss()
        
    else:
        chapter_one_loss()
    return(player_health)

def chapter_three():
    player_health = chapter_two()
    if player_health >= 1:
        #question 1
        print("question 1")
        print("1")
        print("2")
        answer = int(input(""))
        if answer == 1:
            print("The dragon hears you and attacks. You lose one health point.")
            player_health = player_health-1
        elif answer == 2:
            print("You have succesfully entered the dungeon.")
        if player_health < 1:
            chapter_three_loss()
        else:
            #QUESTION 2
            print("question 2")
            print("1")
            print("2")
            answer = int(input(""))
            if answer == 1:
                print("The dragon hears you and attacks. You lose one health point.")
                player_health = player_health-1
            elif answer == 2:
                print("You have succesfully entered the dungeon.")
            if player_health < 1:
                chapter_three_loss()
            else:
                #QUESTION 3
                print("question 3")
                print("1")
                print("2")
                answer = int(input(""))
                if answer == 1:
                    print("The dragon hears you and attacks. You lose one health point.")
                    player_health = player_health-1
                elif answer == 2:
                    print("You have succesfully entered the dungeon.")
                if player_health < 1:
                    chapter_three_loss()
                else:
                    print("You have", player_health,"health left.")
                    print("You Win!")
while if_continue == 1:
    print("Once upon a time there was a land made of pure Gold. It was dominated by leprecons that lived happily.")
    print("As time passed on though, gold started becoming a scarcity. Humans started stealing their gold until finally there")
    print("was only left enough to supply every leprecon citizen with so many. When they saw this, every leprecon started taking their share.")
    chapter_three()
    if_continue = int(input("Do you want to continue playing? (press 1 for 'yes' and 2 for 'no')"))
