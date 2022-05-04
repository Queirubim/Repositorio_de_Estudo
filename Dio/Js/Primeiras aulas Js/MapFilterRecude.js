/*
const maca = {
    value: 2,
}
const laranja = {
    value: 3,
}

function mapthis(vetor, thisArg){
    return vetor.map(function(item){
        return item * this.value;
    }, thisArg);
}

const num =[1,2];

console.log('this -> maçã', mapthis(num,maca))
console.log('this -> laranja', mapthis(num,laranja))
*/

// .map  gerencia array 

/*
function mapsemthis (vetor){
    return vetor.map(function(item){
        return item * 2;
    });
}

const num = [2,4,5,6,8,10];

console.log(num);

console.log(mapsemthis(num));
 */

// .filter filtra algo especifico do array

/*
function filtraQP(array){
    return array.filter(callback)
}

function callback (item){
    return Math.sqrt(item) % 1 === 0;
}

const quadrados = [2,4,6,8,10,12,14,16,20,25,31,36,42,49]

console.log(filtraQP(quadrados));
*/
// const obg = ['copo vidro','caneca vidro','prato vidro','chicara porcelana', 'prato porcelana']
/*
function soma(arr){
    return arr.reduce(function(anterior, atual) {
        console.log({anterior});
        console.log({atual});
        return anterior + atual;
    },0);

}
const arr = [3,2];
console.log(soma(arr));
*/

const lista = [ {
    nome: 'sabao em po',
    preco: 8,
    },
    {
    name : 'Caneca',
    preco: 24,
    },
    {
    name : 'Filtro de linha',
    preco: 100,
    },
];

const saldo = 400;

function calculasaldo (saldo, lista){
    return lista.reduce(function(ant,atu, index) {
        console.log("rodada", index +1);
        console.log({ant});
        console.log({atu});
        return ant - atu.preco;
    },saldo);
}

console.log(calculasaldo(saldo,lista))