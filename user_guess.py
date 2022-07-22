def user_guess(shuffled_list):
    # let user guess the index of the "o" in the list
    print(
        f'guess location of "o" in the list\nenter a number from {0} - {len(shuffled_list)-1}')
    user_guess = input('Enter here: ')

    return int(user_guess)
