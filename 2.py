#Zapytania/warunki  if if/else

if True:
    print("tak, to prawda")


if 2 < 5:
    print("dwa jest mniejsze od 5")

a= 2*4
if a>5:
    print(a , "jest większe od 5")


b = 4
liste = [ 1, 2, 3, 4 ]

if len(liste) == b:
    print("długość listy wynosi 4")

if len(liste) != b: #inne niż 4
    print("długośc listy jest inna niż 4")

#krótszy zapis z else:

if len(liste) == b:
    print("długość listy wynosi 4")

else:
    print("długośc listy jest inna niż 4")


c = 4
liste = [ 1, 2, 3, 4, 5 ]
if len(liste) == c:
    print("długość listy C wynosi 4")
else:
    if len(liste) == 5:
        print("długość listy C wynosi 5")
    else:
        print("długośc listy C jest inna niż 4 i 5")

#krótszy zapis z if/else z elif:

liste = [ 22, 3, 44, 12 ]
if len(liste) == 4:
    print("długość listy D wynosi 4")
elif len(liste) == 5:
    print("długość listy D wynosi 5")
else:
    print("długośc listy D jest inna niż 4 i 5")


# jeśli masz mniej niż 5000-kupujesz szafę, 
# jeśli więcej niż 8000 jedziesz na wakacje, 
# jeśli masz gotówkę w przedziale zamknietym 5000 - 8000


a = 6000
if a < 5000:
    print("Kupujesz szafę")
elif a > 8000:
        print("Kupujesz telewizor")
else:
    print("Jedziesz na wakacje")



# for 

    a = ["jabłko", "banan", "gruszka", "kiwi"]