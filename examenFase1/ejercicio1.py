#%% SUMA DE N PRIMEROS FIBONACCI
n = int(input("cuantos numeros fibonacci?"))
a = 0
b = 1
d = 0
for x in range(n):
    c = b+a
    a = b
    d += a
    b = c    
    print (a)
print (f'Suma total {d}')
