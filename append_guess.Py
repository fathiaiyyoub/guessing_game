def append_guess():
    
    list_of_numbers = [1, 11, 7, 8, 12, 6, 15, 30, 5, 3, 2]
    guessed = set()

    ''' Game rules'''
        
        print("Welcome to the Number Guessing Game!")
        print("Game Rules: You have to guess (11) numbers between (1-30)")
        print("You cannot guess the same number twice")
        print("The Game is programmed to delete any duplicate values")
        print("Hint --- Total of all (11) numbers is (100)")
        print("Happy Guessing")
    
    while len(guessed) != len(list_of_numbers):
        
        ''' Game logic'''
        
        n = int(input("Enter an integer between 1-30 >> "))
        if n in list_of_numbers:
            print("right guess")
            guessed.add(n)
            print(guessed)
            
        elif n not in list_of_numbers:
            print("Wrong Guess - Keep Trying!! ")
        
    print("Great Job! You have Guessed All numbers!")
    print("You have completed the Guessing Game!!")
       
append_guess()