# Aprovar o imprestimo Bancário para compra de Casa
nome_comprador = str(input('Digite o seu nome : ')).strip()
valor_casa = float(input('Digite o valor da casa: '))
salario_comprador = float(input('Digite o s' 'eu salário mensal: '))
validade_casa = int(input('Digite quantos anos vais pagar a casa: '))

casa = validade_casa * 12
pagamento_casa = valor_casa / casa
requesitos_pagamento = salario_comprador * 0.3

if pagamento_casa >= requesitos_pagamento:
    print('O Sr. {}, Não pode efectuar esta operação, porque o valor da casa por mës é de {:.2f}€ é superior a 30% do seu salário que é de {}€'.format(nome_comprador,pagamento_casa,requesitos_pagamento))
else:
    print('O Sr. {} é aprovado ao imprestimo da casa com a validade de {} anos TEM O PAGAMENTO DE {}'.format(nome_comprador,validade_casa,pagamento_casa))
print('Sr. {}, agradeçemo'.format(nome_comprador))