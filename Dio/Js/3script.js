//vetores arrays e objetos

// array pode ter outros arrays dento de si

let array =['string',1,true,['array2'],['array3'],['array4']];
console.log(array[2])
/*
forEach() - itera um array, ou seja repete cada item do array;
push() - add item no final do array;
pop() - remove item no final do array;
shift() - remove item no início do array;
unshift() - add item no início do array;
indexOf() - retorna o índice de um valor;
splice() - remove ou substitui um item pelo índice;
slice () - retorna uma parte de um array existente;
*/

/*array.forEach(function(item, index){console.log(item,index) });*/
/*
//joga um novo dado por final do array
array.push('novo item');
console.log(array)

//remove o ultimo dado do array
array.pop();

//remove o primeiro itemdo array
array.shift();

//adiciona um item no inicio
array.unshift();

//retorna o indice do array
console.log(array.indexOf(true));

array.splice(0 , 3);
console.log(array);

let novoarray = array.slice(0,7);
console.log(novoarray);

*/

//objetos


let celular = { nome: 'celular', quantidade: 3 ,booleano:true, array:['varias coisas'], objetoInterno: {nome: 'bateria'}};
console.log(celular.quantidade)

var nome = (celular.nome)
console.log(nome)