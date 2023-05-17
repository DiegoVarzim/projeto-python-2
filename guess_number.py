import random

print('Seja muito bem-vindo ao Guess Number do Diego Varzim!')
choice_number = input('Digite o número teto do desafio: ')

# convertendo o texto digitado em número int(inteiro)
if choice_number.isdigit():
    choice_number = int(choice_number)
# final da conversão
else:
    print('Erro: valor informado não é numérico. Favor execute novamente e informe um número!')
    quit()

random_number = random.randint(0, choice_number)

n_choices = 0

# looping
while True:
    answer_user = input('Adivine o número: ')

    if answer_user.isdigit():
        answer_user = int(answer_user)
    else:
        print('Erro: valor informado não é numérico.  Favor informe um número!')
        continue

    n_choices = n_choices + 1

    if answer_user == random_number:
        print('Acertou!')
        break

    elif answer_user > random_number:
        print('Chutou alto, o número randômico é menor que esse...')
    else:
        print('Chutou baixo, o número randômico é maior que esse...')

print('Número de tentativas: ' + str(n_choices))

    

        