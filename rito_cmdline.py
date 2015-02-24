import requests, json, pprint

cycle = True
first_time = True

while cycle == True:
    # Ask user from a list of functions what they would like to do.
    if first_time == True:
        user_intention = raw_input("Welcome to summoner spyglass, how can I help? ( Type 'help' for a list of options ) ")
    elif first_time == False

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
            print("Checking details on {}".format(summoner_name))

            payload = {'api_key': 'b0afea27-1602-4ed8-aff5-24caf6bbb2d1'}

            r = requests.get("https://na.api.pvp.net/api/lol/na/v1.4/summoner/by-name/{}".format(summoner_name), params=payload)

            if r.status_code == 200:
                print("Success! The summoner {} was found!".format(summoner_name))

                pprint.pprint(r.json())
            else:
                print("Sorry, {} wasnt found. Please try again!".format(summoner_name))

        elif verify == "no":
            print("Okay, Lets try that again!")


    # If the user input stored at user_intention makes no sense, restart the loop with error message and reprompt.

    else:
        first_time = False

 

