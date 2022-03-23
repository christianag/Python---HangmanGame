import random
import string
from words import words

def get_valid_word(words):
    word = random.choice(words)
    while '-' in word or ' ' in word: #the JSON file i'm using has words with spaces and dashes in them, making them invalid
        word = random.choice(words)
    return word

def hangman():
    word = get_valid_word(words).upper() 
    word_letters = set(word) #stores non-duplicate values
    alphabet = set(string.ascii_uppercase)
    used_letters = set() #store the user's guesses in here 
    lives = 6

    while len(word_letters) > 0 and lives > 0:
        
        word_list = [letter if letter in used_letters else '-' for letter in word] 
        # if the letter is guessed - show the letter. otherwise show a dash
        
        print('\nTHE WORD IS: ', ' '.join(word_list))
        print('You have used these letters: ', ' '.join(used_letters))
        print(f'You have {lives} left.')
        user_letter = input('Guess a letter: ').upper()

        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            else:
                print(f'\nYour letter {user_letter} is not in the word.')
                lives -= 1
        elif user_letter in used_letters:
            print('\nYou already used that letter. Try another one!')
        else:
            print('\nThat is not a valid letter')
    
    if lives == 0:
        print(f'\nSorry, you are out of guesses. You lose! The word was {word}')
    else:
        print(f'\nYou win! The word is {word}'))


if __name__ == '__main__':
    hangman()
