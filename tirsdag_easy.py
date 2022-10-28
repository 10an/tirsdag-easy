from ast import While
from cProfile import label
from matplotlib import pyplot as plt
from numpy import empty, number 



word1 = 2
word2 = 4
word3 = 6
word4 = -2
word5 = 10


## Oppgave 1##

word1 = 2
word2 = 4
word3 = 6
word4 = -2
word5 = 10

'''Opprett en while loop som kan:

1.-Opprett en lista med de variablene ovenfor 
2.-Summere verdien til alle variablene
3.-Printe verdien i terminalen.'''

numbers = []
while True:
    numbers.extend((word1, word2, word3, word4, word5))
    print("Summen er " + str(sum(numbers)))
    break






## Oppgave 2##

'''
finn en funksjon (Det finnes flere) 
som printer variablene
ovenfor sortert fra det 
minste til det største. 
'''
numbers.sort()
for number in numbers:
    print(number)





## Oppgave 3##
## bruk gjerne eksempel som ligger på teams

'''
lag en diagram (pie type) som viser elementene til variabel "countries" og kunsumprisindeks med farge. 

'''
countries  = ["Nicaragua", "Cuba", "Kina", "Østerrike", "Nederland", "Norge", "Chile", "Brasil","Venezuela"]
konsumprisindeks = [3.4, 1.2, 3.7, 5.3, 4.9, 6.9, 8.1, 7.2, 3.4 ]
colors = [ "yellow", "red", "blue", "silver", "deeppink", "brown", "grey", "cyan", "darksalmon"]

plt.pie(konsumprisindeks,
    labels=countries,
    colors=colors,
    startangle=90,
    autopct="%.1f%%"
)

plt.title("Konsumprisindex")
plt.show() 






## Oppgave 4##

'''
Lag en while loop som legger til tall fra 0 til 50. Deretter må løkken summere alle elementene. Opprett en ny variabel 
som tar imot resultatet til forrige operasjonen. Bruk print() for vise vedien til den nye variabelen.

'''
seatNumber = []
num = 1
total = 0

while len(seatNumber) != 50:
    seatNumber.append(num)
    num += 1
    total += num
print(seatNumber)
print("Summen er: " + str(total))






""" 
seatNumber = []
num = 0
total = 0
numbers = range(0,50)

while num < len(numbers):
    seatNumber.extend((numbers))
    num += 1
    total += num
print("Summen er: " + str(total))
print(seatNumber) """