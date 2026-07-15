import random
from colorama import Fore,init
# init()

# a=random.choices(range(1,35),k=3)

# n=int(input("sonni kriting: "))

while(1):
    init()
    a=random.choices(range(1,35),k=3)
    n=int(input("sonni kriting: "))
    if n in a:
        print(Fore.MAGENTA+'GOLIBSIZ')
        print(a)
        break
    else:
        print(Fore.LIGHTRED_EX+"Yutqazding<<<<")
        print(a)
