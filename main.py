class Funcionario:
    __CPF=""
    __nomeFuncionario=""
    __temBonus= bool

    def __init__(self,cpf,nome,bonus):
        self.__CPF= cpf
        self.__nomeFuncionario= nome
        self.__temBonus= bonus

    
    def setnomeFuncionario(self,funcionario):
        self.__nomeFuncionario = funcionario

    def setCPF(self,CPF):
        self.__CPF = CPF

    def setTemBonus(self,Bonus):
        self.__temBonus = Bonus
        

    #GETS

    def getnomeFuncionario(self):
        return self.__nomeFuncionario

    def getCPF(self):
        return self.__CPF

    def getTemBonus(self):
        return self.__temBonus

    #metodo

    def obterGanhos(self):
        pass


class FuncionarioCLT(Funcionario):
    __salarioMensal= 0

    def __init__(self, cpf, nome, bonus, salarioMensal):
        super().__init__(cpf, nome, bonus)
        self.__salarioMensal= salarioMensal

    def setSalarioMensal(self, salario):
        self.__salarioMensal= salario

    #GETS

    def getSalarioMensal(self):
        return self.__salarioMensal

    #metodo

    def obterGanhos(self):
        if self.getTemBonus()==True:
            self.__salarioMensal = self.__salarioMensal + (10/100)

        else:
            print(f"Não possui bônus, portanto:",self.__salarioMensal)

        return self.__salarioMensal


class FuncionarioHorista(Funcionario):
    __cargaHoraria= 0
    __valorHora= 0

    def __init__(self, cpf, nome, bonus, cargaHoraria, ganhoHora):
        super().__init__(cpf, nome, bonus)
        self.__cargaHoraria= cargaHoraria
        self.__valorHora= ganhoHora

    def setCargaHoraria(self,cargaH):
        self.__cargaHoraria= cargaH

    def setValorHora(self,valor):
        self.__valorHora= valor
    
    #GETS

    def getValorHora(self):
        return self.__valorHora

    def getCargaHoraria(self):
        return self.__cargaHoraria


    def obterGanhos(self):
        if self.getTemBonus()==True:
            self.__valorHora= self.__valorHora + (10/100)
        
        else:
            print(f"Não possui bônus, portanto: {self.__cargaHoraria*self.__valorHora}")

        return self.__cargaHoraria*self.__valorHora




print("BEM-VINDO AO MENU")
print("-"*30, "\nOPÇÕES:")

print("1 - adicionar FUNCIONARIO HORISTA\n2 - adicionar FUNCIONARIO CONTRATADO\n3 - LISTAR todos os funcionarios")

print("-"*30)
    

try:

    while True:
        pergunta= input("Deseja adiconar ou listar funcionarios (s/n)? ")

        if pergunta=="s":
            perguntaMenu= int(input("Informe a opção: "))

        if perguntaMenu== 1:

            nome= input("Informe o NOME: ")
            cpf= input("Informe o CPF: ")
            bonus= bool("Informe se POSSUI BONUS (True/False): ")
            v= float(input("Informe o VALOR da CARGA HORARIA: "))
            c= int(input("Informe a CARGA HORARIA: "))

            usuario= FuncionarioHorista(cpf,nome,bonus,c,v)

        elif perguntaMenu==2:
            nome= input("Informe o NOME: ")
            cpf= input("Informe CPF: ")
            bonus= bool("Informe se POSSUI BÔNUS (True/False): ")
            salario= float(input("Informe o SALARIO MENSAL: "))

            usuario= FuncionarioCLT(cpf,nome,bonus,salario)

        elif perguntaMenu==3:
            print(FuncionarioCLT,FuncionarioHorista)

            continue

        elif pergunta== "n":
            break
        print("Ate logo!")

        
    
except Exception:
    print("Ocorreu um erro, para que não se repita, faça calmamente")
