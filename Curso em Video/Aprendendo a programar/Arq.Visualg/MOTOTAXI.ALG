algoritmo "QUANTO EU PRECISO PARA PASSAR DE ANO"
var

  U1 ,U2 ,U3, R: Real
  
  
inicio

    Escreval("----------------------------------------")
    Escreval("    QUANTO PRECISO PARA SER APROVADO")
    Escreval("----------------------------------------")
    ESCREVAl(" Diga sua nota da primeira unidade")
    Leia (U1)
    Escreval(" Diga sua nota da segunda unidade")
    Leia (U2)
    Escreval(" Diga sua nota da terceira unidade")
    Leia (U3)
    R <- (((U1 + U2 + U3)-28)* -1)
    Escreval("Voçê precisar tirar ", R ," para ser aprovado")
    Escreval("----------------------------------------")
    
fimalgoritmo