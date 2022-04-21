// tipos primitivos
//bolean 
var off = false;
console.log(typeof(off));

//number
var numero = 1;
console.log(typeof(numero));

//string 
var frase = "qualquercoisa";
console.log(typeof(frase));

//fybction
var funcao =function() {}
console.log(typeof(funcao));

// como declarar var e let
// var é usada em escopo global
// let é usada em escopo local
// Ao não serem declaradas tem valor nulo
// Podem ser alteradas
var variavel = 'allan';
variavel = 'soares';
console.log(variavel)

let variavel2 = 'Soares';
variavel2 =  'allan'
console.log(variavel2)

//Cons não pode ser alterada na execução
//E tem que atribuir um valor Inicial.

const constante = 24;
console.log(constante)

var escopoglobal = 'global';
console.log(escopoglobal);

function escopolocal() {
    let escopolocalinterno = 'Local';
    console.log(escopolocalinterno)
}

escopolocal();

var compara = "0" == 0; 
console.log(compara)

var compara2 = '0' === 0; 
console.log(compara2)

var maiorigual = 5 >= 5;
console.log(maiorigual);

//os dois verdadeiros pra dar verdadeiro
var e = false && false;
console.log(e)
//qualquer um verdadeiro pra dar verdadeiro
var ou = true || false;
console.log(ou)
// inverte o valor
var nao = ! false;
console.log(nao)

