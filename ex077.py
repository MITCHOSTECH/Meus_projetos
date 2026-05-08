palavras = ('aprende', 'programar', 'linguagem', 'python',
            'curso', 'gratis', 'estudo', 'praticar',
            'trabalhar', 'mercado', 'programador', 'futuro')
for frase in palavras:
    print(f'\nNa palavra \033[1:34m{frase.upper():.>15}\033[m temos', end=' ')
    for letra in frase:
        if letra.lower() in 'aeiou': # procurando vogais com acentuação (áãäàéèêiíoôóuú)
            print(letra, end=' ')