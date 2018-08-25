# napisz program wypisujący wszystkie liczby od 0 do 100,podzielne przez 3 lub podzielne przez 5.Wypisz także jak dużó takich liczb wystąpiło w tym przedziale

ile_podzielnych = 0

for i in range(101):
    if i % 3 == 0 or i & 5 == 0:
        ile_podzielnych += 1
        print(i)

print(f'W przedziale 0-100 jest {ile_podzielnych} liczb  podzielnych przez 3 lub 5')
