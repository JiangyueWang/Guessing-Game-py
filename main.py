from shuffle_list import shuffle_list
from user_guess import user_guess


def run_game():
    shuffled_list = shuffle_list(['', 'o', ''])
    user_answer = user_guess(shuffled_list)
    if shuffled_list[user_answer] == 'o':
        print('Your guess is correct')
        print(f'shuffled list is {shuffled_list}')
    else:
        print('Your guess is incorrect')
        print(f'shuffled list is {shuffled_list}')


run_game()
