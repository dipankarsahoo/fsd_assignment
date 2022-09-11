'''Problem Statement: You have to write a Word Puzzle Game in which the user has to form the correct word out of a given set of characters. In the game the user has to solve this
puzzle for 5 words, one at a time. Problem words are stored in a list and appear to the user  in random sequence. Give the user score +1 for each correct answer and give 
-1 for each wrong answer. At last print the final score. You can store any number of words in the list, but in each round of the game only 5 words are shown to the user.

Sample output of the game:
Arrange the letters to form a valid word:
RAEHTF
Father
Correct
Arrange the letters to form a valid word:
KABRE
Barke
Wrong
Arrange the letters to form a valid word:
CYROTNU
Cry
Wrong
Arrange the letters to form a valid word:
RENEG
green
Correct
Arrange the letters to form a valid word:
OAERELANP
aeroplane
Correct
Net Score is 1'''

import random

class wordPuzzleGame:
    
    # initialize score to 0 for a game and word list to fixed values
    def __init__(self):
        self.score = 0
        self.wordList = ['beginner', 'business', 'education', 'afternoon', 'sentence', 'meaningful', 'sequence', 'ancestors']
    
    # select 5 unique random words from word list
    def selectJumbledWords(self):
        return random.sample(self.wordList, 5)
    
    # return jumbled alphabets for a word
    def randomizeJumbledList(self, word):
            return ''.join(random.sample(word, len(word)))
     
    # increase score by 1 for correct answer       
    def incrementScore(self):
        self.score +=1
     
    # decrease score by 1 for wrong answer   
    def decrementScore(self):
        self.score -=1
        
    # retrun current score of the game    
    def getScore(self):
        return self.score
            
startGame = wordPuzzleGame()

# Get user preference to play the game
if input('Do you want to play the word puzzle game ? [y/n]') == 'y':
    words = startGame.selectJumbledWords()
    for word in words:
        
        # get user input for the jumbled word
        userAnswer = input(f'What is the rearranged word for {startGame.randomizeJumbledList(word).capitalize()}\n')
        
        if userAnswer.lower() == word.lower():
            print('Correct')
            startGame.incrementScore()
        else:
            print('Wrong')
            startGame.decrementScore()
    
    # Print the score as this is the end of game        
    print(f'Your score for the game is {startGame.getScore()}')
        