import random 
import re 

def hangmanGame():
  numSp = random.choice([4, 5, 6, 7, 8])
  words = {
    4: ['dark', 'game', 'bird'], 
    5: ['error', 'event', 'power'], 
    6: ['laptop', 'friend', 'forest'], 
    7: ['biology', 'mystery', 'harmony'], 
    8: ['beautiful', 'infinite', 'internet']
  }
  
  word = random.choice(words[numSp])
  GBoard = ['_'] * numSp
  redHearts = '❤️  ' 
  blackHearts = '🖤  '
  PTAgain = ''
  redCount, blackCount = 3, 0
  checkList = []
  print(GBoard)
  print(f'Hearts: {redHearts*redCount} {blackHearts*blackCount} \n')
  
  while True:
    
    if ''.join(GBoard) == word:
      print('<== You win! ==>')
      while PTAgain != 'y' and PTAgain != 'n':
        PTAgain = input('play again? (y/n): ')
        PTAgain.lower()
      break
      
    elif redCount <= 0 or blackCount >= 3:
      print('<== You loose! ==>')
      while PTAgain != 'y' and PTAgain != 'n':
        PTAgain = input('try again? (y/n): ')
        PTAgain.lower()
      break
      
    guess = input('guess a character: ')
    guess.lower()
    
    if len(guess) > 1 or not re.match(r'[a-z]', guess):
      print('Invalid Guess!\n')
      continue 
      
    elif guess in word and guess not in checkList:
      checkList.append(guess)
      index = [i for i, e in enumerate(word) if e == guess]
      for idx in index:
        GBoard[idx] = guess
      print('correct guess!')
      print(GBoard)
      print(f'Hearts: {redHearts*redCount} {blackHearts*blackCount} \n')
      
    else:
      redCount -= 1
      blackCount += 1
      print('incorrect guess!')
      print(GBoard)
      print(f'Hearts: {redHearts*redCount} {blackHearts*blackCount} \n')
      
  if PTAgain == 'y':
    hangmanGame()
  else:
    print('Thank You for playing!')

user = input("Enter your name: ")
print(f'good luck! {user}')
hangmanGame()
