import random

def rollTheDice():
  faces = [1, 2, 3, 4, 5, 6]
  face = random.choice(faces)
  if face == 1:
    print('''
      ***********
      *         *
      *    *    *
      *         *
      ***********
      ''')
  elif face == 2:
    print('''
      ***********
      *         *
      *  *   *  *
      *         *
      ***********
      ''')
  elif face == 3:
    print('''
      ***********
      *  *      *
      *    *    *
      *      *  *
      ***********
      ''')
  elif face == 4:
    print('''\r
      ***********
      *  *   *  *
      *         *
      *  *   *  *
      ***********
      ''')
  elif face == 5:
    print('''
      ***********
      * *     * *
      *    *    *
      * *     * *
      ***********
      ''')

  else:
    print('''
      ***********
      *  *   *  *
      *  *   *  *
      *  *   *  *
      ***********
      ''')
      

while True:
  user = input('roll the dice (y/n): ')
  user.lower()
  if user == 'y':
    rollTheDice()
  elif user == 'n':
    print('<= Thank You for playing! =>')
    break
  else:
    print('Invalid choice!')
