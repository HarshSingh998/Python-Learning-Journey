
import random
com = random.randint(1,100)

tries = 0

while True:
    tries = tries + 1
    hum = int(input("Guess Your Number Between 1 - 100 :- "))

    if hum == com:
        print(f"Congratulation You Have WON in {tries} tries !")
        break

    elif hum > com:
        print("Sorry Wrong Guess - Go Lower")

    elif hum < com:
        print("Sorry Wrong Guess - Go Higher")
