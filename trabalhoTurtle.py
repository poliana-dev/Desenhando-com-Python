from turtle import Turtle


class minhaTartaruga(Turtle):
    __nome = " Maria Poliana"
    __matricula= "20211181110016"

    def __init__(self,cor):
        super().__init__("turtle")
        self.color(cor)
        self.penup()
        self.pendown()
        self.pensize(2)
        self.shape("turtle")
       

    def getNome(self):
        return self.__nome

    def getMatricula(self):
        return self.__matricula


    def desenharSapo(self):

        #ajustando posicao
        self.penup()
        self.goto(0,-100)
        
        self.pendown()

        #primeira parte do corpo
        self.circle(150,130)
        self.right(85)
        self.circle(45,190)
        self.right(73)
        self.circle(260,35)

        #segunda parte do corpo
        self.right(73)
        self.circle(45,190)
        self.right(85)
        self.circle(150,130)
        self.forward(70)

        #organizando 
        self.penup()
        self.forward(40)
        self.backward(170)
        self.right(100)
        self.setx(-115)
        self.back(8)
        self.left(10)
        
        for perninhas in range(2):
            self.pendown()    
            self.circle(50,130)
            self.right(80)
        
            

       
            


            

        


        

        

        



poli= minhaTartaruga("green")
poli.desenharSapo()