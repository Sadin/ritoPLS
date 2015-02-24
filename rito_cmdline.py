import requests, json, pprint

# Declare some stuff here, Best stuff Declared NA 
cycle = True
error = False
error_message = "Something didnt work cause Sadin is a baddie."

while cycle == True:
    
    # Check if the loop was restarted due to an error.
    if error == False:
        # Ask user from a list of functions what they would like to do.
        user_intention = raw_input("Welcome to ritoCMD, how can I help: ( Type 'help' for a list of options ) ")

    elif error == True:
        user_intention = raw_input("You're request was not recognized, make sure you've entered it correctly \nand try again: ( Type 'help' for a list of options ) ")
    else:
        print error_message
    # Stop the loop and exit,
    if user_intention == "exit":
        print("Bye, Bye!")
        break
    # If the user would like to find details of a Summoner prompt them for the name and verify said name exists.
    elif user_intention == "Summoner":
        summoner_name = raw_input("Enter summoner name: ")

    # Verify the summoner_name input was correct, if not break the loop
        verify = raw_input("Im going to grab details of {}, is that correct? (yes/no) ".format(summoner_name))

        if verify == "yes":
            print("Checking details on {}\n".format(summoner_name))

            payload = {'api_key': 'b0afea27-1602-4ed8-aff5-24caf6bbb2d1'}

            r = requests.get("https://na.api.pvp.net/api/lol/na/v1.4/summoner/by-name/{}".format(summoner_name), params=payload)

            if r.status_code == 200:
                print("Success! The summoner {} was found!\n".format(summoner_name))

                pprint.pprint(r.json())
            else:
                print("Sorry, {} wasnt found. Please try again!".format(summoner_name))

        elif verify == "no":
            print("Okay, Lets try that again!")
    elif user_intention == "Help" or user_intention == "help":
        print "\nHere is a list of valid inputs:\n      Summoner - Prints info about a summoner \n      exit - Exits the program \n"

    # If the user input stored at user_intention makes no sense, restart the loop with error message and reprompt.

    else:
        error = True



 

