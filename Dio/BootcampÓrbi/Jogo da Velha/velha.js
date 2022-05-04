var jogador,vencedor = null;
var jogadorSelecionado = document.getElementById ('Jogador-selecionado');
var jogadorVencedor = document.getElementById ('Jogador-Vencedor');
var matizquadrado = document.getElementsByClassName('quadrado');

mudarjogador('X');


function escolherquadrado(id) {

    if (vencedor != null){
        return
    }

    var quadrado = document.getElementById(id);
    if (quadrado.innerHTML !== '-') {
        return;
    }


    quadrado.innerHTML = jogador;
    quadrado.style.color= '#000';
    console.log(id);

    if (jogador === 'X'){
        jogador = 'O';
    } else{
        jogador = 'X';
    }

    mudarjogador(jogador);
    checaVencedor();

}


function mudarjogador(valor){
    jogador = valor;
    jogadorSelecionado.innerHTML = jogador;
}

function checaVencedor(){
    var quadrado1 = document.getElementById(1);
    var quadrado2 = document.getElementById(2);
    var quadrado3 = document.getElementById(3);
    var quadrado4 = document.getElementById(4);
    var quadrado5 = document.getElementById(5);
    var quadrado6 = document.getElementById(6);
    var quadrado7 = document.getElementById(7);
    var quadrado8 = document.getElementById(8);
    var quadrado9 = document.getElementById(9);

    if(checa(quadrado1, quadrado2, quadrado3 )){
        mudacor(quadrado1,quadrado2,quadrado3);
        mudarVencedor(quadrado1);
        return;
    }
    if(checa(quadrado4, quadrado5, quadrado6 )){
        mudacor(quadrado4,quadrado5,quadrado6);
        mudarVencedor(quadrado4);
        return;
    }
    if(checa(quadrado7, quadrado8, quadrado9 )){
        mudacor(quadrado9,quadrado8,quadrado9);
        mudarVencedor(quadrado7);
        return;
    }
    if(checa(quadrado1, quadrado4, quadrado7 )){
        mudacor(quadrado1,quadrado4,quadrado7);
        mudarVencedor(quadrado1);
        return;
    }
    if(checa(quadrado2, quadrado5, quadrado8 )){
        mudacor(quadrado2,quadrado5,quadrado8);
        mudarVencedor(quadrado5);
        return;
    }
    if(checa(quadrado3, quadrado6, quadrado9 )){
        mudacor(quadrado3,quadrado6,quadrado9);
        mudarVencedor(quadrado6);
        return;
    }
    if(checa(quadrado1, quadrado5, quadrado9 )){
        mudacor(quadrado1,quadrado5,quadrado9);
        mudarVencedor(quadrado1);
        return;
    }
    if(checa(quadrado3, quadrado5, quadrado7 )){
        mudacor(quadrado3,quadrado5,quadrado7);
        mudarVencedor(quadrado5);       
    }
}

function mudacor(quadrado1,quadrado2,quadrado3){
    quadrado1.style.backgroundColor = '#0f0';
    quadrado2.style.backgroundColor = '#0f0';
    quadrado3.style.backgroundColor = '#0f0';
}

function mudarVencedor(quadrado) {
    vencedor = quadrado.innerHTML
    jogadorVencedor.innerHTML = vencedor
}

function checa (quadrado1, quadrado2,quadrado3) {
    var eigual = false;

    if(quadrado1.innerHTML !='-' && quadrado1.innerHTML == quadrado2.innerHTML && quadrado2.innerHTML == quadrado3.innerHTML ) {
        return true;
    }

    return eigual;
}

function reset () {
    vencedor = null
    jogadorVencedor.innerHTML = '';

    for (let i = 1; i <= 9; i++) {
        var quadrado = document.getElementById(i);
        quadrado.style.backgroundColor = 'rgb(185,183,183)';
        quadrado.style.color = 'rgb(185, 183, 183)';
        quadrado.innerHTML = '-';
    }

    mudarjogador('X');
}