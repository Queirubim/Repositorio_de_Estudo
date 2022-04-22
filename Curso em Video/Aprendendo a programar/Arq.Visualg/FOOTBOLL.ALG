algoritmo "Footboll"
var

 T1, T2, P: Inteiro

inicio

 Escreval ("-----------------------------")
 Escreval ("          PLACAR")
 Escreval ("-----------------------------")
 Escreva ("Quantos gols o time 1 fez? :")
 Leia (T1)
 Escreva ("Quantos gols o time 2 fez? :")
 Leia (T2)
 Escreval ("-----------------------------")
 Se T1 > T2 então
    P <- (T1 - T2)
 senão
    P <- (T2 - T1)
 Fimse
 Escolha P
         Caso 1,2,3
         Escreval ("      JOGO ACIRRADO")
         Caso 4,5,6,7,8,9,10
         Escreval ("          GOLEADA")
         Caso 0
         EScreval ("           EMPATE")
 Fimescolha
 Escreval ("------------------------------")
         



fimalgoritmo