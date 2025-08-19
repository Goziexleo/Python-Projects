import random
from collections import Counter
someWords = '''apple banana mango strawberry orange grape pineapple apricot lemon coconut watermelon cherry papaya berry peach lychee muskmelon'''

someWords = someWords.split(' ')

word = random.choice(someWords)

if __name__ == '__main__':
    print('Guess the word!. HINT; a fruit')
    for i in word:
        print('_', end=' ')
    print()

    playing = True
    letterGuessed = ''
    chances = len(word)+2
    correct = 0
    flag = 0
    try:
        while chances != 0 and flag == 0:
            print()
            chances -= 1

            try:
                guess = str(input('Enter a letter to guess:'))
            except:
                print('Only alphabets allowed, try a letter instead')
                continue
            if not guess.isalpha():
                print('LETTERS only')
                continue
            elif len(guess) > 1:
                print('Enter only 1 letter')
                continue
            elif guess in letterGuessed:
                print("You've already guessed that letter")
                continue
            if guess in word:
                k = word.count(guess)
                for _ in range(k):
                    letterGuessed += guess
            for char in word:
                if char in letterGuessed and (Counter(letterGuessed)) != Counter(word):
                    print(char, end=' ')
                elif (Counter(letterGuessed)) == Counter(word):
                    print(f'The word is: {word}')
                    flag = 1
                    print('Congratulations, You Won')
                    break
                else:
                    print('_', end=' ')
        if chances <= 0 and (Counter(letterGuessed) != Counter(word)):
            print()
            print(f'You lost, better luck next time.\nThe word was {word}')
    except KeyboardInterrupt:
        print()
        print("Bye!, try again later")
        exit()
