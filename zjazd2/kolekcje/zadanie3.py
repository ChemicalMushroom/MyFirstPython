#napisz program zliczający wystąpienia liczb dodatnich i ujemnych w zadanej liście liczb całkowitych.

lista = []

liczby_dodatnie = 0
liczby_ujemne = 0

for liczba in lista :
    if liczba > 0:
        liczby_dodatnie += 1
    elif liczba < 0 :
        liczby_ujemne += 1

print(f"ujemnych: {liczby_ujemne} , dodatnich:{liczby_dodatnie}:" )


















