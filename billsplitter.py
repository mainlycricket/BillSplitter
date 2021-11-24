import random

count_friends = int(input("Enter the number of friends joining (including you):\n"))
friends = {}
i = 1

if count_friends <= 0:
    print("\nNo one is joining for the party")

else:
    print("\nEnter the name of every friend (including you), each on a new line:")

    while i <= count_friends:
        friend = input()
        friends[friend] = 0
        i += 1

    bill_value = float(input("\nEnter the total bill value:\n"))

    lucky_feature = input('\nDo you want to use the "Who is lucky?" feature? Write Yes/No:\n')

    if lucky_feature == 'Yes':
        friends_list = list(friends.keys())
        lucky_friend = random.choice(friends_list)
        print()
        print(lucky_friend, "is going to lucky\n")
        individual_contribution = round(bill_value / (count_friends - 1), 2)
        for keys, values in friends.items():
            friends[keys] = individual_contribution
        friends[lucky_friend] = 0
        print(friends, end="")

    else:
        print("\nNo one is going to be lucky\n")
        individual_contribution = round(bill_value / count_friends, 2)
        for keys, values in friends.items():
            friends[keys] = individual_contribution
        print(friends, end="")