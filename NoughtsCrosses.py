def gameplay():
    player = "X"
    A1 = A2 = A3 = B1 = B2 = B3 = C1 = C2 = C3 = " "
    while True: 
        print   ("\n", A1 ,"|", B1 ,"|", C1, "\n-----------\n", A2, "|", B2, "|", C2, "\n-----------\n", A3, "|", B3, "|", C3, "\n")
        Row = int(input("Write your Row: "))
        Column = int(input("Write your Column: "))
        if Row > 3 or Column > 3 or Row < 1 or Column < 1:
            print("Invalid input, please try again")
        else:
            if Row == 1:
                if Column == 1:
                    if A1 == " ":
                        if player == "X":
                            A1 = "X"
                            player = "O"
                        else:
                            A1 = "O"
                            player = "X"
                    else:
                        print("Invalid input, please try again")
                elif Column == 2:
                    if A2 == " ":
                        if player == "X":
                            A2 = "X"
                            player = "O"
                        else:
                            A2 = "O"
                            player = "X"
                    else:
                        print("Invalid input, please try again")
                elif Column == 3:
                    if A3 == " ":
                        if player == "X":
                            A3 = "X"
                            player = "O"
                        else:
                            A3 = "O"
                            player = "X"
                    else:
                        print("Invalid input, please try again")
            elif Row == 2:
                if Column == 1:
                    if B1 == " ":
                        if player == "X":
                            B1 = "X"
                            player = "O"
                        else:
                            B1 = "O"
                            player = "X"
                    else:
                        print("Invalid input, please try again")
                elif Column == 2:
                    if B2 == " ":
                        if player == "X":
                            B2 = "X"
                            player = "O"
                        else:
                            B2 = "O"
                            player = "X"
                    else:
                        print("Invalid input, please try again")
                elif Column == 3:
                    if B3 == " ":
                        if player == "X":
                            B3 = "X"
                            player = "O"
                        else:
                            B3 = "O"
                            player = "X"
                    else:
                        print("Invalid input, please try again")
            elif Row == 3:
                if Column == 1:
                    if C1 == " ":
                        if player == "X":
                            C1 = "X"
                            player = "O"
                        else:
                            C1 = "O"
                            player = "X"
                    else:
                        print("Invalid input, please try again")
                elif Column == 2:
                    if C2 == " ":
                        if player == "X":
                            C2 = "X"
                            player = "O"
                        else:
                            C2 = "O"
                            player = "X"
                    else:
                        print("Invalid input, please try again")
                elif Column == 3:
                    if C3 == " ":
                        if player == "X":
                            C3 = "X"
                            player = "O"
                        else:
                            C3 = "O"
                            player = "X"
                    else:
                        print("Invalid input, please try again")
            if A1 == A2 == A3 == "X" or B1 == B2 == B3 == "X" or C1 == C2 == C3 == "X" or A1 == B1 == C1 == "X" or A2 == B2 == C2 == "X" or A3 == B3 == C3 == "X" or A1 == B2 == C3 == "X" or A3 == B2 == C1 == "X":
                print("Player 1 wins")
                print   ("\n", A1 ,"|", B1 ,"|", C1, "\n-----------\n", A2, "|", B2, "|", C2, "\n-----------\n", A3, "|", B3, "|", C3, "\n")
                return()
            elif A1 == A2 == A3 == "O" or B1 == B2 == B3 == "O" or C1 == C2 == C3 == "O" or A1 == B1 == C1 == "O" or A2 == B2 == C2 == "O" or A3 == B3 == C3 == "O" or A1 == B2 == C3 == "O" or A3 == B2 == C1 == "O":
                print("Player 2 wins")
                print   ("\n", A1 ,"|", B1 ,"|", C1, "\n-----------\n", A2, "|", B2, "|", C2, "\n-----------\n", A3, "|", B3, "|", C3, "\n")
                return()
            elif (A1 != " " and A2 != " " and A3 != " " and B1 != " " and B2 != " " and B3 != " " and C1 != " " and C2 != " " and C3 != " "):
                print("Draw")
                print   ("\n", A1 ,"|", B1 ,"|", C1, "\n-----------\n", A2, "|", B2, "|", C2, "\n-----------\n", A3, "|", B3, "|", C3, "\n")
                return()
            else:
                print("Player ", player, "'s turn")



print("Welcome to Noughts and Crosses")
print("This is a two player game")
while True:
    gameplay()
    if input("Do you want to play again? (Y/N): ") == "N":
        break