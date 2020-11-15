import words
import random

print("Let's play Hangman")
print('')
print('''Rules are simple: 
1) You just have to guess the secret word.
2) You have only 6 chances 
3) If your letter or word does not match the secret word then you will lose a chance                            
              ''')

def play():
    word = random.choice(words.word_list).upper()
    hidden = len(word) * '_'
    guess = False
    guessed = list(hidden)
    l = list(word)
    guessed_letters = []
    tries = 0

    while guess == False and tries < 6:
        print(words.figure[tries])
        for o in guessed:
            print(o,end='')
        print('')
        print('')
        inp = input('Please make a guess: ').upper()
        print('')

        if len(inp) == len(word):
            if inp == word:
                print(f'YOU WIN!! You guessed the word, {inp}')
                guess = True
            else:
                print(f'{inp} is not the secret word')

        elif len(inp) == 1:

            if inp in guessed_letters:
                print('You have already guessed this letter', inp)

            if inp in word:
                #here first we enumerate word
                #and in list of index if the input = letter in list then we take the index of that
                index = list(enumerate(word))
                for k in index:
                    if inp in k:
                        indice = k[0]
                        guessed[indice] = inp
                guessed_letters.append(inp)

            if guessed == l:
                print(words.figure[tries])
                for o in guessed:
                    print(o,end='')
                print('')
                print(f'YOU WIN!! You guessed the word!')
                guess = True


            if inp not in word:
                print(f'{inp} is not in the secret word')
                guessed_letters.append(inp)
                tries += 1

        else:
            print('Not a valid guess!')
            guessed_letters.append(inp)
            tries += 1

        if tries == 6:
            print(words.figure[-1])
            for o in guessed:
                print(o,end='')
            print('')
            print(f'{word} is the secret word')
            print('')
            print('')
            print('YOU LOSE!!')

def start():
    print('')
    again = input('DO YOU WANT TO PLAY AGAIN? PRESS y/n: ').upper()
    if again == 'Y':
        play()
    else:
        quit()

play()
while True:
    start()
