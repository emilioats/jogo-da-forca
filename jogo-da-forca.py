palavra = 'drakai'
tentativas = []
chances = 3

# Saudações
print()
print('Seja bem-vindo(a) ao jogo da foca em python :)')
print('Lembre-se você começa com 3 chances!')
print()

while True:

    # Código
    if chances == 0:
        print()
        print('### Suas chances acabaram!')
        print('### Você perdeu...  ')
        print()
        print(f'### A Palavra era "{palavra.upper()}"')
        print()
        break

    letra = input('Chute uma letra: ')

    if letra.isupper():
        letra = letra.lower()

    if len(letra) > 1:
        print('### Só é permitido 1 letra!')
        continue

    if letra == '':
        print('### Informe 1 letra!')
        continue

    if letra in tentativas:
        print(f'### Você já informou essa letra! ({letra})')
        continue

    tentativas.append(letra)

    if letra in palavra:
        print()
        print(f'### Parabéns você acaba de acertar 1 letra! ({letra})')
    else:
        chances -= 1
        print()
        print(f'### Você só tem mais {chances} chances!')
        tentativas.pop()

    palavra_temporaria = ''
    for letra_secreta in palavra:
        if letra_secreta in tentativas:
            palavra_temporaria += letra_secreta
        else:
            palavra_temporaria += '*'

    if palavra_temporaria == palavra:
        print()
        print('### Parabéns por ter ganhado o jogo! :)')
        print(f'### A Palavra: {palavra_temporaria.upper()}')
        print()
        break
    else:
        print(f'### A Palavra: {palavra_temporaria.upper()}')
        print()
