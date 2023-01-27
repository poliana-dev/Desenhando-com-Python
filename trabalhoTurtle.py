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
        self.goto(400,-100)
        
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
        self.setx(250)
        self.sety(160)

        for olhos in range(2):
            self.color("black")
            self.begin_fill()
            self.circle(20,400)
            self.end_fill()
            self.penup()
            self.right(40)
            self.forward(220)

        self.back(385)
        self.color("green")
        self.pendown()
        self.right(50)
        self.circle(40,100)


    def desenharMariaPoliana(self):
        self.penup()
        self.goto(-400,-150)


poli= minhaTartaruga("green")

poli.desenharSapo()