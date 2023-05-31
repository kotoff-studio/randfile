import os
import random

aCap = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
aLet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
aDig = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

combinations = [
f"{random.choice(aCap)}{random.choice(aDig)}{random.choice(aLet)}{random.choice(aCap)}{random.choice(aDig)}{random.choice(aLet)}", 
f"{random.choice(aDig)}{random.choice(aCap)}{random.choice(aLet)}{random.choice(aDig)}{random.choice(aDig)}{random.choice(aCap)}",
f"{random.choice(aDig)}{random.choice(aDig)}{random.choice(aCap)}{random.choice(aLet)}{random.choice(aLet)}{random.choice(aDig)}",
f"{random.choice(aLet)}{random.choice(aCap)}{random.choice(aLet)}{random.choice(aDig)}{random.choice(aDig)}{random.choice(aCap)}"
]

def crypt(file: str):
    if os.path.isfile(f'{file}'):
        with open(f'{file}', 'r+') as forcrypt:
            content = forcrypt.read()
            with open(f'{random.choice(combinations)}.{random.choice(aLet)}{random.choice(aLet)}', 'a+') as ac_crypted:
                ac_crypted.write(content)
                print('success')
                    
    else:
        print('The file does not exist!')
