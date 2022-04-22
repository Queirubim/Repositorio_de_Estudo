algoritmo "Triangulo"
var
 L1, L2, L3:Inteiro
 EQ, ES, Tri:Logico
inicio
  Escreva ("Digite o primeiro lado: ")
   Leia (L1)
  Escreva ("Digite o segundo lado: ")
   Leia (L2)
  Escreva ("Digite o terceiro lado:")
   Leia (L3)
   Tri<- (L1 < L2 + L3) e (L2 < L1 + L3) e (L3 < L1 + L2)
  EQ <- (L1 = L2) e (L2 = L3)
  ES <- (L1 <> L2)  e (L1 <> L3) e (L2 <> L3)
  Escreval ("Isso é um triangulo? ",Tri)
  Escreval ("O triangulo e EQUILATERO? ", EQ)
  EScreva  ("o triangulo e ESCALENO? ",ES)

fimalgoritmo