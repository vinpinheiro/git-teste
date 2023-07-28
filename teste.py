import os
import time


alunos = []
notas = []
matricula = []
senha_p1 = 'senha123'

def organizador(a, mf=False):
    try:
        a = float(a)
        a = (f'{a:.2f}')
    except:
        pass
    xy = list(a)
    num = len(xy)
    ndd = (16 - num) // 2
    for fg in range(0, ndd):
        xy.insert(0, ' ')
    for gf in range(0, ndd):
        xy.append(' ')
    if len(xy) == 15:
        xy.append(' ')
    if mf and float(a) < 6:
        print(f'\033[1;31m')
    elif mf and float(a) >= 6:
        print(f'\033[1;32m')
    return ''.join(xy)

def tabela():
     print('+----------------+----------------+----------------+----------------+----------------+\n'
                      '|     alunos     |   Matemática   |    Português   |    Ciências    |   Média Final  |\n'
                      '+----------------+----------------+----------------+----------------+----------------+', end='')

print('\033[1;38m-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
print('SEJA BEM VINDO À ÁREA RESTRITA!')
print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-==-=-=-=-=-')
print('preencha as informações a seguiur para acessar o conteudo:')

while True:
    liberado_p = False
    liberado_a = False
    print('__________________________________________________________')
    nome = input('nome: ').lower()

    print('__________________________________________________________')
    id = int(input('professor[1]\naluno[2]:\n'
    '__________________________________________________________\nRespota: '))
    print('__________________________________________________________')

    while True:
        if id == 1:
            senha_p2 = input('digite a senha do professor: ')
            if senha_p2 == senha_p1:
                liberado_p = True
                print('acesso liberado')
                break
            else:
                print('senha incorreta')
                break
        elif id == 2:
            nm = input('digite seu número de matricula: ')
            try:
                pos = matricula.index(nm)
                if nome == alunos[pos]:
                    liberado_a = True
                    print('acesso liberado')
                    break
            except:
                print('nome ou matricula invalida(o)')
                break
    while True:
        if liberado_p:
            op = input('[1] ver notas dos alunos\n'
                       '[2] resgistrar notas + aluno\n'
                       '[3] sair\n')
            if op == '2':
                mat = []
                al = input('aluno: ')
                mt = input('matricula: ')
                m = int(input('nota de matematica: '))
                p = int(input('nota de português: '))
                c = int(input('nota de Ciências: '))
                med = (m + p + c) / 3
                alunos.append(al)
                matricula.append(mt)
                mat.append(m)
                mat.append(p)
                mat.append(c)
                mat.append(med)
                notas.append(mat[:])
            elif op == '1':
                tabela()
                for a in alunos:
                    b = alunos.index(a)
                    print(f'|{organizador(a)}|{organizador(notas[b][0])}|{organizador(notas[b][1])}|{organizador(notas[b][2])}|{organizador(notas[b][3], mf=True)}|\033[1;38m\n'
                          '+----------------+----------------+----------------+----------------+----------------+', end='')
                print('')
            elif op == '3':
                break
        elif liberado_a:
            tabela()
            posicao = alunos.index(nome)
            print(f'|{organizador(nome)}|{organizador(notas[posicao][0])}|{organizador(notas[posicao][1])}|{organizador(notas[posicao][2])}|{organizador(notas[posicao][3], mf=True)}|\033[1;38m\n'
                          '+----------------+----------------+----------------+----------------+----------------+', end='')
            input('\npressione enter para sair')
            break
        else:
            break
    print('__________________________________________________________')
    print('perfil desconectado')
    time.sleep(3)
    for loop in range(0, 10000):
        print('\n')


