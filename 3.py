translation = {
    "PL" : {"Welcome" : "Cześć"},
    "DE" : {"Welcome" : "Hallo"},
    "FR" : {"Welcome" : "Bonjour"},
    "IT" : {"Welcome" : "Buongiorno"},
    "ES" : {"Welcome" : "Buenos dias"} 
    }

print(translation ["DE"] ["Welcome"]) #wyswietli z listy translation, podtablicy de wartość dla welcome

print(
    {"PL":["Cześć", "Witam" , "Hejka"]} #tablica
)

print(
    {"PL":["Cześć", "Witam" , "Hejka"] , 5:9 } #tablica i number.Python nie sortuje w dictionary-wyswietlanie bedzie losowe
)

s = (1,2) #tuple
print(s)
#s[1]=4 #wystapi blad-w tuple nie ma mozliwosci nadpisania, dodania, usuniecia elementow.zmienna const.
print(s) 