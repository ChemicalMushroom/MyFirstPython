x = [3,1,2]
y = []
min_ = None

for i in x:
    if min_ == None:
        min_ = i
    elif  i < min_:
        min_ = i

print(min_)

#chce zamienić miejscami 3 i 1

print(x.index(3))
print(x.index(1))

y = x[x.index (1)]
y = x[x.index (3)]

x[x.index(1)] = z
x[x.index(3)] = y
