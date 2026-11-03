n1 = float(input("Diga a primeira nota: "))
n2 = float(input("Diga a segunda nota: "))
n3 = float(input("Diga a terceira nota: "))
n4 = float(input("Diga a quarta nota: "))
media = (n1+n2+n3+n4)/4
print(media)

notas = []

for i in range(4):
    bi = input(f"Diga sua {i+1}° nota: ")
    notas.append(bi)

print(f"Sua nota é: {sum(notas)/4}")