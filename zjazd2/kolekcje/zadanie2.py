# napisz program obliczający średnią wartość z podanych przez użtkownika liczb.Do przechowywania liczb użyj listy.Pozwól na wprowadzenie maksymalnie 10 liczb.Skorzystaj z funkcji wbudowanej sum()

liczby = []

while len (liczby) < 10:
    nowa_liczba = input("podaj nową liczbe lub wpisz 'k' aby zakończyć")
    if nowa_liczba =='k':
        break
    else:
        nowa_liczba = int(nowa_liczba)
        liczby.append(nowa_liczba)
srednia = sum(liczby) / len (liczby)

print(f'średnia liczb {liczby} to :{srednia}')