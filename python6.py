vocales=['a','e','i','o','u']
print(vocales)
for i in range(len(vocales)):
    print(f"{vocales[i]}", end=",")
print(f"Longitud de vocales: {len(vocales)}")
for c in vocales:
    print(f"Vocal: {c}")
for c in vocales:
    if c=='b':
        break
else:
    print('No se ha encontrado el carácter b')