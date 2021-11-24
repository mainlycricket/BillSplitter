import random   # Importing the random module

# Reading input from the user to know the number of friends joining the party:
count_friends = int(input("Enter the number of friends joining (including you):\n> "))

friends = {}    # declaring an empty dictionary

i = 1       # while loop initializer

# checking if at least one member is joining the party:

if count_friends <= 0:
    print("\nNo one is joining for the party")

# in case there is at least one member in the party:

else:
    print("\nEnter the name of every friend (including you), each on a new line:")

    while i <= count_friends:
        friend = input("> ")
        friends[friend] = 0
        i += 1

    bill_value = float(input("\nEnter the total bill value:\n"))    # Bill value

    # Enable the lucky feature in case there are more than one members

    if count_friends > 1:

        lucky_feature = input('\nDo you want to use the "Who is lucky?" feature? Write Yes/No:\n')  # User's wish

        # Lucky feature enabled

        if lucky_feature == 'Yes':
            friends_list = list(friends.keys())
            lucky_friend = random.choice(friends_list)
            print()
            print(lucky_friend, "is going to be lucky\n")
            individual_contribution = round(bill_value / (count_friends - 1), 2)
            for keys, values in friends.items():
                friends[keys] = individual_contribution
            friends[lucky_friend] = 0
            print(friends, end="")

        # Lucky feature not enabled:

        else:
            print("\nNo one is going to be lucky\n")
            individual_contribution = round(bill_value / count_friends, 2)
            for keys, values in friends.items():
                friends[keys] = individual_contribution
            print(friends, end="")

    # Lucky feature unavailable in case there is only one member
        
    else:
        individual_contribution = round(bill_value / count_friends, 2)
        for keys, values in friends.items():
            friends[keys] = individual_contribution
            print()
            print(friends, end="")