fruits=["Banana","Orange"]


def printlist():
    for z in fruits:
        print(z)
    option ()

def option():
    inp=int(input("\nPress\n1: Enter a fruit in list\n2: Remove a fruit from list\n3: Print the list\n4: Exit\n\n"))
    if inp == 1:
        app()
    elif inp == 2:
        rem()
    elif inp == 3:
        printlist()
    elif inp == 4:
        exit
    else:
        print ("\nnot a valid response\n")
        option()


def app():
    like=input("\nPlease enter a fruit you like:\n")
    if like in fruits:
        print ("\nItem already in list\n")
        option()
    else:
        fruits.append(like)
        option()

def rem():
    dislike=input("\nPlease enter a fruit you dislike:\n")
    if dislike in fruits:
        fruits.remove(dislike)
        option()
    else:
        print ("\nItem is not in list\n")
        option()

option ()


