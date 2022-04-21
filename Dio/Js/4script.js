/*
var jogador1 = 0
var jogador2 = 0
var placar;
jogador1 != -1 && jogador2 != -1 ? console.log('os jogadores são validos'): console.log('Jogadores invalidos');
if (jogador1 || jogador2 > 0 ){
    placar = jogador1 > jogador2
}
else {
    console.log("Ninguem marcou pontos");
}
switch (placar){
    case placar == true:
        console.log('Jogador 1 venceu')
        break
    case placar == false:
        console.log('Jogador 2 venceu')
        break
    default:
        console.log('deu empate')
        break

} 
*/


let vetor = [ 'v1' , 'v2','v3','v4','v5' ];
let objeto = {p1: 'v1', p2: 'v2', p3:'v3'}
/*
for(let indice = 0; indice < vetor.length; indice ++){
    console.log(indice);
}

for (let i in vetor ) {
    console.log(i);
}


for (i in objeto) {
    console.log(i)
}


for (i of vetor) {
    console.log(i)
}


for (i of objeto.p1) {
    console.log(i);
}
*/
var a = 0;

// faz ate condição for verdade
// confere antes da execução

while (a < 10 ) {
    a++; 
    console.log(a);
}

// faz ate condição for falsa
// confere depois da execução
do {
    a--
    console.log(a);
}while (a > 1);
