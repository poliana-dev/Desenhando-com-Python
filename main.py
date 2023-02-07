from trabalho import * 


print("BEM-VINDO AO MENU")
print("-"*30, "\nOPÇÕES:")

print("1 - adicionar FUNCIONARIO HORISTA\n2 - adicionar FUNCIONARIO CONTRATADO\n3 - LISTAR todos os funcionarios")

print("-"*30)
    

try:

    nomeFuncionarios=[]

    bonus=bool

    while True:

        pergunta= input("Deseja adicionar ou listar funcionarios (s/n)? ") #deveria dar erro se colocasse numero? ele apenas continua rodando

        print("-"*20)

        if pergunta == "s":
            perguntaMenu= int(input("Informe o número opção: "))

            if perguntaMenu== 1:

                nome= input("Informe o NOME: ")
                cpf= int(input("Informe o CPF: "))
                bonus= bool(input("Informe se POSSUI BÔNUS (True/False): "))#ele deveria dar erro
                v= float(input("Informe o VALOR da CARGA HORARIA: "))
                c= int(input("Informe a CARGA HORARIA: "))
                print("-"*20)

                usuario= FuncionarioHorista(cpf,nome,bonus,c,v)
                nomeFuncionarios.append(usuario.getnomeFuncionario())

            elif perguntaMenu==2:
                nome= input("Informe o NOME: ")
                cpf= int(input("Informe CPF: "))
                bonus= bool(input("Informe se POSSUI BÔNUS (True/False): ")) #ele deveria dar erro 
                salario= float(input("Informe o SALARIO MENSAL: "))
                print("-"*20)

                usuario= FuncionarioCLT(cpf,nome,bonus,salario)
                nomeFuncionarios.append(usuario.getnomeFuncionario())

            elif perguntaMenu==3:
                print(f"Nome de todos os funcionários da Empresa: {nomeFuncionarios}")
                print("-"*30)

                continue

        elif pergunta=="n":
            break
    print("Ate logo!")

 

except ValueError:
    print("Ops, você informou algo errado pode ter sido uma letra ou número. Tente novamente")