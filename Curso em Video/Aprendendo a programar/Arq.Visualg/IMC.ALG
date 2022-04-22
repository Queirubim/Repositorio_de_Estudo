algoritmo "imc"
var

    P, IMC ,A: Real

inicio

      Escreval ("Esse é um teste para saber seu IMC e dizer se vc esta obeso ou não")
      Escreval ("Diga qual o seu peso em KG !")
      Leia (P)
      Escreval ("Agora diga sua altura em M !")
      Leia (A)
      IMC <- P / (A^2)
      Escreval ("Seu imc é " , IMC:5:2)
      Se (IMC <= 25) e (IMC >= 18.5) então
         Escreval ("Voce não esta Obeso")
      Senão
         Escreval ("Você esta obeso pare de tomar cerveja")
      Fimse

fimalgoritmo