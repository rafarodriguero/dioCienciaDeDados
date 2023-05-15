nome = 'Rafael'

for letter in nome:
    if nome.lower().count(letter.lower()) > 1:
        print(True)
        break
    print(False)