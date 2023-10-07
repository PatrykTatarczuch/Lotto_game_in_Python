import random

rand = (random.sample(range(1, 50), 6))
list = (rand)
list_loss = []
x = 1
list_cor = 0
while x <= len(list):
    x += 1
    print("Wylosuj liczbę w przedziale od 1 do 49: ")
    try:
        loss = int(input())
    except ValueError:
        print("Podana wartość musi byc liczbą całkowitą")
        x -= 1
        continue
    if loss in list_loss:
        print("Liczby nie mogą się powtarzać")
        x -= 1
    elif loss < 1:
        x -= 1
        print("Wybierz liczbę o większej wartości")
    elif loss > 49:
        x -= 1
        print("Wybierz liczbę o mniejszej wartości")
    elif 1 <= loss <= 49 and list[0] != loss and list[1] != loss and list[2] != loss and list[3] != loss and list[4] != loss and list[5] != loss:
        print("Wylosowana liczba:", loss)
        list_loss += [loss]
    else:
        if loss not in list_loss:
            list_loss += [loss]
            list_cor += 1
            print("Wylosowana liczba:", loss)



print("Twoje liczby: ", sorted(list_loss))
print("Liczby w puli: ", list)
print("Wydałeś 3zł na kupon")
if list_cor == 1:
    print("Udało Ci się zgadnąć", list_cor, "liczbę")
    print("Niestety nie udało Ci się nic zarobić")
elif list_cor == 0:
    print("Niestety nie udało Ci się zgadąć ani jednej liczby :(")
    print("Następnym razem Ci się uda")
elif list_cor == 6 or list_cor == 5:
    print("Udało Ci się zgadnąć", list_cor, "liczb")
    if list_cor == 6:
        print("Wow!!! Zarobiłeś 7.000.000 milionów zł")
    elif list_cor == 5:
        print("Wow!!! Zarobiłeś 6.000 zł")
else:
    print("Udało Ci się zgadnąć", list_cor, "liczby")
    if list_cor == 3:
        print("Nieźle! Zarobiłeś 24 zł")
    elif list_cor == 4:
        print("Super! Zarobiłeś 205 zł")
    else:
        print("Byłeś bardzo blisko wygranej!")
