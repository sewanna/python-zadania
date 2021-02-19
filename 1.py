
#Zadanie 1
# Stworzyć tabelę x 5 liczb, usunąć z niej elementy od 2 do 4. Z wyniku pomnożyć 1 i 3 element odjąć od niego 4.
# Zamienić wynik na string i dodać na koniec znak *.
# Stworzyć tabelę y 3 liczb, pomnożyć 1 i 3 element przez 3 wynik zamienić na string
# Stworzyć string z obu wyników, a następnie podzielić na tabelę.

# Stworzyć tabelę y 3 liczb, pomnożyć 1 i 3 element przez 3, wynik zamienić na string
#stworzyć string z obu wyników, a następnie podzielić na tabelę.


x=[ 2 , 4 , 3 , 1, 5]
del x[2:4] #usuwa element 2-3
print (x)
y=(x[1]) * (x[2]) # mnoży el. 1 i el.2 z tabeli pomniejszonej o el 2-3  
print(y) 
z= y-4  #odejmuje 4
t=str(z) + ("*") # zamienia na string i  dodaje dodatkowego stringa
print(t)

a=[3,6,9,6] #utworzona druga tabela
b=a[2] * a[3] # pomnożony 2 i 3  el. tabeli
print(b)
c=str(b) #zamienony number na string
print(b)

d = (c + " " + t) # dodane oba utworzone stringi 
print(d)

e=d.split() # stringi zamienione na tabelę
print(e)

