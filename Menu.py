from tkinter import N
import Funktioner

menuItems = ["Velkommen til regnemaskinen","Vælg en af nedenstående muligheder(1-3):","1. Se skattetakster", "2. Se rabat", "3. Benyt regnemskine"]
stateOptions = ["UT","NV","TX","AL","CA"]
stateTax = [1.0685,1.08,1.0625,1.04,1.0825]

for items in menuItems:
    print(items)

userInput = int(input("Indtast menuvalg:"))

if userInput == 1:
    #Præsenter skattetakster
    Funktioner.presentTax()
elif userInput == 2:
    #Præsenter rabat
    Funktioner.presentDiscount()
elif userInput == 3:
    #Regnemaskinefunktion
    price = int(input("Indtast pris pr. vare i $: "))
    amount = int(input("Indtast antal vare: "))
    userZipcode = input("Indtast statskode: ")


    total = price * amount

    if total >= 1000 and total < 5000:
        total = total * 0.97
    elif total >= 5000 and total < 7000:
        total = total * 0.95
    elif total >= 7000 and total < 10000:
        total = total * 0.93
    elif total >= 10000 and total < 50000:
        total = total * 0.90
    elif total >= 50000:
        total = total * 0.85
    
    print("Din pris efter rabat:", total)

    n = -1

    for element in stateOptions:
        n = n + 1
        if element == userZipcode:
            currentTax = stateTax[n]
            total = total * currentTax
    
    if userZipcode in stateOptions:
        print("Din pris efter rabat og tilføjet skat", total)
    else:
        print("Din stat genkendes ikke, du er fritaget for skat")




else:
    print("DU SKAL INDTASTE ET TAL FRA 1 til 3!!!")