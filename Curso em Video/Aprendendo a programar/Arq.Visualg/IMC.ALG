algoritmo "imc"
var

    P, IMC ,A: Real

inicio

      Escreval ("Esse � um teste para saber seu IMC e dizer se vc esta obeso ou n�o")
      Escreval ("Diga qual o seu peso em KG !")
      Leia (P)
      Escreval ("Agora diga sua altura em M !")
      Leia (A)
      IMC <- P / (A^2)
      Escreval ("Seu imc � " , IMC:5:2)
      Se (IMC <= 25) e (IMC >= 18.5) ent�o
         Escreval ("Voce n�o esta Obeso")
      Sen�o
         Escreval ("Voc� esta obeso pare de tomar cerveja")
      Fimse

fimalgoritmo