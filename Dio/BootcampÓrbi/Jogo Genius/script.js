let ordem = [];
let clickOrdem = [];
let score = 0;

const blue =document.querySelector('.blue')
const red =document.querySelector('.red')
const yellow =document.querySelector('.yellow')
const green =document.querySelector('.green')

//cria ordem aleatoria de cores
function random (){
    let c = Math.floor(Math.random() * 4);
    ordem[ordem.length] = c;
    clickOrdem =[];

    for(let i in ordem) {
        let elementColor = criaCorElemento(ordem[i]);
        ligthColor(elementColor,Number(i)+ 1);
    }
}
//acende a proxima cor
function ligthColor (elemento,numero){
    numero = numero * 500
    setTimeout(()=> {
        elemento.classList.add('selected');
    },numero - 250);

    setTimeout(()=> {
        elemento.classList.remove('selected')
    });
}
//checa a equivalencia entre os botões clicados e a ordem
function checaOrdem () {
    for(let i in clickOrdem){
        if (clickOrdem[i] != ordem[i]){
            perdeu()
            break
        }
    }
    if (clickOrdem.length == ordem.length){
        alert(`Pontuação: ${score}\nVoce acertou! Iniciando proximo nível`)
        proximoLevel();
    }
}

//
function click (color) {
    clickOrdem[clickOrdem.length]=color;
    criaCorElemento(color).classList.add('selected');

    setTimeout(() => {
        criaCorElemento(color).classList.remove('selected');
        checaOrdem();
    },250)

}

//
function criaCorElemento(color) {
    if(color == 0) {
        return green;
    } else if (color == 1){
        return red;
    }else if (color == 2){
        return yellow;
    }else if (color == 3){
        return blue;
    }
}

//
function proximoLevel (){
    score ++;
    random();
}

//Game-Over
function perdeu (){
    alert(`Pontuação: ${score}\nVocê perdeu o jogo!\nClirque em ok para reiniciar!`)
    ordem =[];
    clickOrdem =[];

    iniciar();
}

function iniciar(){

    score = 0;
    proximoLevel();
}

green.addEventListener('click',click(0));
red.addEventListener('click',click(1));
yellow.addEventListener('click',click(2));
blue.addEventListener('click',click(3));

green.onclick =() => click(0)
red.onclick =() => click(1)
yellow.onclick =() => click(2)
blue.onclick =() => click(3)

iniciar();

