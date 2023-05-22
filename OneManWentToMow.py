total = int(input("Enter the number of mowers: "))
for verse in range(1,total+1):
    if verse == 1:
        man = "man"
    else:
        man = "men"
    print(verse, man, "went to mow,\n went to mow a meadow,")
    for i in range(verse,0,-1):
        if i > 1:
            print (i, "men, ")
        else:
            print ("1 man and his dog, spot")
    print ("went to mow a meadow",end="\n\n")