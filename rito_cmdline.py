import requests, json, pprint

cycle = True

while cycle == True:
    # Ask user from a list of functions what they would like to do.
    user_intention = raw_input("Welcome to summoner spyglass, what would you like to do?")

    # If the user would like to find details of a Summoner prompt them for the name and verify said name exists.
    if user_intention == "Summoner":
        summoner_name = raw_input("Enter summoner name: ")

    # Verify the summoner_name input was correct, if not break the loop
        verify = raw_input("Im going to grab details of {}, is that correct? (yes/no)".format(summoner_name))

        if verify == "yes":
            print("Checking details on {}".format(summoner_name))

            payload = {'api_key': 'b0afea27-1602-4ed8-aff5-24caf6bbb2d1'}

            r = requests.get("https://na.api.pvp.net/api/lol/na/v1.4/summoner/by-name/{}".format(summoner_name), params=payload)

            if r.status_code == 200:
                print("Success! The summoner {} was found!".format(summoner_name))
            else:
                print("Sorry, {} wasnt found. Please try again!".format(summoner_name))
        else verify == "no":
            break


        pprint.pprint(r.json())

