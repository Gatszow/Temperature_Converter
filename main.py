# -*- coding: utf-8 -*-

print("#"*80, end="")
print("To program przeliczający stopnie (C)elcjusza na:\n- stopnie (F)ahrenheita \n!! lub/i !!"
      "\n- na (K)elwiny\nJest też możliwość przeliczania odwrotnego :)")
print("#"*80, end="")

in_ = input("Zmiana z: (C/F/K) - ").upper()

value = str(input("Ile stopni? - ")).replace(",", ".")

try:
    value = int(value)
except ValueError:
    value = float(value)

choice = input("Napisz: \n- \"Tak\"(T), jeśli chcesz przeliczyć na dwie pozostałe jednostki\n- \"Nie\"(N), "
               "jeśli chcesz przeliczyć jedynie na jedną konkretną jednostkę\nWybór - ").upper()

if choice == "TAK" or choice == "T":
    choice = True
    print("#"*80, end="")
    print("Podaj jedynie jedną literke:")

elif choice == "NIE" or choice == "N":
    choice = False

else:
    print("Niewłaściwe dane, przypuszczam więc, że nie chcesz")
    choice = False

out_ = input("Zmiana na: (C/F/K) - ").upper()
print("#"*80, end="")

if in_ == "C":
    if choice is False:
        if out_ == "C":
            print("Wynik:\nHa, przewidziałem to! \nNie ma sensu przeliczać, wynik jest ten sam - {} stopni Celcjusza"
                  .format(value))

        elif out_ == "F":
            print("Wynik:\n{:.2f} stopni Fahrenheita".format((value*9/5)+32))

        elif out_ == "K":
            print("Wynik:\n{:.2f} Kelwinów".format(value+273.15))

        else:
            print("Zła literka")

    elif choice is True:
        if out_ == "C":
            print("Wynik:\nHa, przewidziałem to! \nNie ma sensu przeliczać, wynik jest ten sam - {} Celcjuszy"
                  "\nA jeżeli jednak to była pomyłka, to:\nStopnie Fahrenheita - {:.2f}"
                  "\nKelwiny - {:.2f}".format(value, (value*5/9)+32, value+273.15))

        elif out_ == "F" or "K":
            print("Wynik:\n{:.2f} stopni Fahrenheita\n{:.2f} Kelwinów".format((value*9/5)+32, value+273.15))

        else:
            print("Zła literka")


elif in_ == "F":
    if choice is False:
        if out_ == "F":
            print("Wynik:\nHa, przewidziałem to! \nNie ma sensu przeliczać, wynik jest ten sam - {} stopni Fahrenheita"
                  .format(value))

        elif out_ == "C":
            print("Wynik:\n{:.2f} stopni Celcjusza".format(5/9*(value-32)))

        elif out_ == "K":
            print("Wynik:\n{:.2f} Kelwinów".format((5/9*(value-32))+273.15))

        else:
            print("Zła literka")

    elif choice is True:
        if out_ == "F":
            print("Wynik:\nHa, przewidziałem to! \nNie ma sensu przeliczać, wynik jest ten sam - {} stopni Fahrenheita"
                  "\nA jeżeli jednak to była pomyłka, to:\nStopnie Celcjusza - {:.2f}\nKelwiny - {:.2f}"
                  .format(value, 5/9*(value-32), (5/9*(value-32)+273.15)))

        elif out_ == "C" or "K":
            print("Wynik:\n{:.3f} stopni Celcjusza\n{:.3f} Kelwinów".format(5/9*(value-32), (5/9*(value-32))+273.15))

        else:
            print("Zła literka")


elif in_ == "K":
    if choice is False:
        if out_ == "K":
            print("Wynik:\nHa, przewidziałem to! \nNie ma sensu przeliczać, wynik jest ten sam - {} Kelwinów"
                  .format(value))

        elif out_ == "C":
            print("Wynik:\n{:.2f} stopni Celcjusza".format(value-273.15))

        elif out_ == "F":
            print("Wynik:\n{:.2f} stopni Fahrenheita".format(((value-273.15)*9/5)+32))

        else:
            print("Zła literka")

    elif choice is True:
        if out_ == "K":
            print("Wynik:\nHa, przewidziałem to! \nNie ma sensu przeliczać, wynik jest ten sam - {} Kelwinów"
                  "\nA jeżeli jednak to była pomyłka, to:\nStopnie Celcjusza - {:.2f}"
                  "\nStopnie Fahrenheita - {:.2f}".format(value, value-273.15, ((value-273.15)*9/5)+32))

        elif out_ == "C" or "F":
            print("Wynik:\n(:.2f} stopni Celcjusza\n{:.2f} stopni Fahrenheita"
                  .format(value-273.15), ((value-273.15)*9/5+32))

        else:
            print("Zła literka")

else:
    print("Zła literka")

print("#"*80, end="")
input("Program zakończył działanie\n")
