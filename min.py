#https://edabit.com/challenge
# 
# #Convert Minutes into Seconds
# #Write a function that takes an integer minutes and converts it to seconds.
def mintosec(min):
    sec = 60*min
    return sec
t=mintosec(60)    
print('Liczba sekund w 60 minut= ',t)

# napisz funkcje ktora zwraca x^2 dla x 


def kwadrat(x):
    liczba = x * x
    return liczba
print("Kwadrat liczby 2 wynosi: " , kwadrat(2) )
print("Kwadrat liczby 5 wynosi: " , kwadrat(5) )

# geometry #math #numbers
# Write a function that takes the base and height of a triangle and return its area.

def triangle(x, y):
    #liczba1 = x * y / 2
    #return liczba1 lub
    return x * y / 2
print ( triangle(2,6) )




