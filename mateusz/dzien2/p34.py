liczby = []
liczby.append(1)
liczby.append(2)
liczby.append(3)

imiona = []
# imiona.append('Adam')
# imiona.append('Ewa') to jest to samo, co:


imiona.extend(['Adam', 'Ewa'])



print(liczby)
print(imiona)

nowalista = [liczby, imiona]

print(nowalista)

