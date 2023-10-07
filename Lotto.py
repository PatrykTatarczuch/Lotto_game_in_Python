import random

rand = (random.sample(range(1, 50), 6))
list = (rand)
list_loss = []
x = 1
list_cor = 0
while x <= len(list):
    x += 1
    print("Write a number between 1 and 49")
    try:
        loss = int(input())
    except ValueError:
        print("The value provided must be an integer")
        x -= 1
        continue
    if loss in list_loss:
        print("Numbers cannot be repeated")
        x -= 1
    elif loss < 1:
        x -= 1
        print("Select a number with a higher value")
    elif loss > 49:
        x -= 1
        print("Select a number with a lower value")
    elif 1 <= loss <= 49 and list[0] != loss and list[1] != loss and list[2] != loss and list[3] != loss and list[4] != loss and list[5] != loss:
        print("The entered number:", loss)
        list_loss += [loss]
    else:
        if loss not in list_loss:
            list_loss += [loss]
            list_cor += 1
            print("The entered number:", loss)

print("Your numbers", sorted(list_loss))
print("Numbers in the pool:", list)
print("You spent PLN 3 on a coupon")
if list_cor == 0:
    print("Unfortunately, you failed to guess the number :(")
    print("Next time you will succeed")
elif list_cor == 1:
    print("You guessed", list_cor, "number")
    print("it will be better next time")
else:
    print("You guessed", list_cor, "number")
    if list_cor == 6:
        print("Wow!!! You earned PLN 7,000,000 million")
    elif list_cor == 5:
        print("Wow!!! You earned PLN 6,000")
    elif list_cor == 4:
        print("Great! You earned PLN 205")
    elif list_cor == 3:
        print("Not bad! You earned PLN 24")
    else:
        print("You were very close to winning!")
