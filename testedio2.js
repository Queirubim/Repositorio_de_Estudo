const gets = require("prompt-sync")();
const print = console.log()

/*
let valoresPares = 0;
let valoresImpares = 0;
let valoresPositivos = 0;
let valoresNegativos = 0;

for (var i = 0; i < 5; i++) {
  const valorInformadoPeloUsuario = parseInt(gets());

 if (valorInformadoPeloUsuario != 0){
        if (valorInformadoPeloUsuario % 2 == 0 ) {
            valoresPares++;
        } else {
            valoresImpares++;
        }
    } else {valoresPares++}

  if (valorInformadoPeloUsuario > 0) {
    valoresPositivos++;
  } else if (valorInformadoPeloUsuario < 0) {
    valoresNegativos++;
  }

}

console.log(`${valoresPares} par(es)`);
console.log(`${valoresImpares} impar(es)`);
console.log(`${valoresPositivos} positivo(s)`);
console.log(`${valoresNegativos} negativo(s)`);


let n = parseInt(gets("Diga um numero : "));
for (let i = 1; i < n+1; i++) {
    if (i% 2 == 0){
      console.log(i);
    }
  }


//TODO: Complete os espaços em branco com uma solução possível para o problema.

let limit = parseInt(gets());

for (let i = 1; i <= limit; i++) {
  let x =(i*i);
  let y = (x*i);

  console.log( i,x,y);
}


var participantes = gets("patt: ");
var criancas;
var array = [];
for(let i = 0; i < participantes; i++){
  criancas = gets("criança: ").split(' ');
  array.push(criancas);
  console.log (array)
}

const meninos = array.filter(f => f[1] == 'M').length;
const meninas = array.filter(f => f[1] == 'F').length;
console.log(`${meninos} carrinhos\n${meninas} bonecas`);
*/

let part = gets();
let alunos;
let matricula = [];

for(let i = 0;  i <   part ; i++ ){
  alunos = gets();
  alunos = alunos.split(" ")
  console.log(alunos)

  if (i == 0){
    matricula = (alunos)
  }else if (parseFloat(    alunos[1]   )>=  matricula[1]){
    matricula = (alunos);
  }

}

if(matricula[1] >= 8   )
 console.log(   matricula[0]   )
else
  console.log("Minimum note not reached")