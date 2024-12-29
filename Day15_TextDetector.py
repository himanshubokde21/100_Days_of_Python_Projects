import os
import time

def isText(text, file):
    with open(f'data\{file}', 'r') as txtFile:
        fileContent = txtFile.read()
    return True if text in fileContent.lower() else False

if __name__ == '__main__':
    text = input('Enter text to detect: ')
    textCount = 0
    dirContent = os.listdir('data/')
    for content in dirContent:
        if content.endswith('txt'):
            flag = isText(text, content)
            print(f'Detecting {text} in {content}...', end='\r')
            time.sleep(.4)
            if flag: 
                print(f'{text} is detected in {content}!')
                textCount += 1
            else: print(f'{text} is not detected in {content}!')
    print(f"--- '{text}' found in {textCount} files! ---")
