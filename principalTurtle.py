def exibirMenu():
    print("_"*30)
    print('BEM-VINDO AO MENU')
    print("-"*30)
    print("A seguir, escolha uma das OPÇOES:")
    print("-"*20)
    print("1 - Para DESENHAR SAPINHO\n2 - Para DESENHAR NOME 'MARIA POLIANA'\n3 - Para DESENHAR MATRÍCULA")
    print("_"*30)

from trabalhoTurtle import minhaTartaruga

t=minhaTartaruga("#993399")
opcao= -1

try:
    while (opcao != 0):
        exibirMenu()
        opcao= int(input("Informe a opção desejada: "))

        if opcao==1:
            t.desenharSapo()

        elif opcao==2:
            t.up()
            t.lt(49)
            t.down()
            t.desenharMariaPoliana()

        elif opcao==3:
            t.up()
            t.rt(90)
            t.down()
            t.desenharMatricula()

        else:
            print("Opção Inválida!")

except ValueError:
    print("Ops, informe APENAS o número da opção")
