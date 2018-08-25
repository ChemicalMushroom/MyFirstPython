#            0          1          2           3
imiona = ("Robert" , "Kamil" , "Piotrek" , "Karolina")
print(type(imiona))
print(imiona)

print(len(imiona))
print("Robert" in  imiona)
#wynikiem takiej operacji (in) będzie true albno false

for imie in imiona:
    print(imie)

#wybranie pierwszego imienia z listy to:
print("pierwsze imie to :" , imiona[0])
print("przedostatnie imie to :",  imiona[2])
print("ostatnie imie to :" , imiona[-1])