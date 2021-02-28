cities = {"Warszawa" : 1700000}
print(cities["Warszawa"])  #wyswietla wartosc ze zmiennej cities dla indexu warszawa
print(len(cities)) #identycznie jak w przypadku stringow i tabel wyswietli ilosc elementow
cities["Wroclaw"] = 643000 #dodaje kolejny klucz do listy. Kazdy klucz podajemy w nawiasach kwadratowych a jego wartosc po znaku rownosci
cities["Poznan"] = 535000
cities["Krakow"] = 780000
cities["Gdansk"] = 582000
cities["Lublin"] = 342000
cities["Szczecin"] = 407000 #przy dodawaniu kolejnych kluczy trzeba za kazdym razem podawac nazwe slownika.Wyswietlanie listy bedzie losowe- nie decyduje tu kolejosc dodawania, alfabetycznosc
cities["Gdansk"] = cities["Gdansk"] + 10000 #zwiekszamy wartosc dla klucza gdansk o 10000
cities["Gdansk"] = cities["Gdansk"] - 50000 ##zmniejszamy wartosc dla klucza gdansk o 50000
cities["Lublin"] = cities["Lublin"] * 2  ##podwajamy liczbe ludnosci Lublina 
cities["Krakow"] = cities["Krakow"] / 2 ##pomniejszamy ludnosc Krakowa o 2
print(cities)
print(cities.get("Wroclaw")) ##pokaze  wkonsoli wartosc klucza Wroclaw.Jesli klucz nie istnieje, wskaze none
print(cities["Warszawa"]/cities["Poznan"]) #podzieli dwa klucze- wtym przypadku wskaze o ile Wawa jest wieksza od poznania

cities_europe = { "Paris" : 2100000 }
cities.update(cities_europe) #metoda dodala do listy cities liste cities_europe
print(cities)
cities.pop("Warszawa")
print(cities)


