const suaNave = document.querySelector('.nave');
const areaJogo = document.querySelector('#main-play-area');
const inimigosImg = ['img/inimigo 1.png','img/inimigo 2.png','img/inimigo 3.png'];
const instrucoes = document.querySelector('.game-intruction');
const startButton = document.querySelector('.start-button');
let ai;

//Ações da Nave
function voaNave(evento){
    if(evento.key === 'ArrowUp'){
        evento.preventDefault();
        moveUp();
    } else if(evento.key === 'ArrowDown') {
        evento.preventDefault();
        moveDown();
    } else if (evento.key === " "){
        evento.preventDefault();
        atirar();
    }
}


//Subir
function moveUp(){
    let topPosition = getComputedStyle(suaNave).getPropertyValue('top');
    if(topPosition === "0px") {
        return
    } else {
        let possition = parseInt(topPosition);
        possition -= 50;
        suaNave.style.top = `${possition}px`;
    }
}

//desce
function moveDown() {
    let topPosition = getComputedStyle(suaNave).getPropertyValue('top');
    if(topPosition === "510px") {
        return
    } else {
        let possition = parseInt(topPosition);
        possition += 50;
        suaNave.style.top = `${possition}px`;
    }
}

//função de tiro
function atirar(){
    let laser = criaLaser();
    areaJogo.appendChild(laser);
    moveLaser(laser);
}

function criaLaser() {
    let possitionX = parseInt(window.getComputedStyle(suaNave).getPropertyValue('left'));
    let possitionY = parseInt(window.getComputedStyle(suaNave).getPropertyValue('top'));
    let novoLaser = document.createElement('img');
    novoLaser.src = './img/shoot.png';
    novoLaser.classList.add('laser');
    novoLaser.style.left = `${possitionX}px`; 
    novoLaser.style.top = `${possitionY- 30}px`;
    return novoLaser;
}

function moveLaser(laser){
    let intervaloLaser = setInterval(() => {
        let pX = parseInt(laser.style.left);
        let aliens = document.querySelectorAll('.alien');

        aliens.forEach((alien) =>{
            if(colisao(laser,alien)){
                alien.src = './img/explosao.png';
                alien.classList.remove('alien');
                alien.classList.add('alien-morreu');
            }
        })

        if(pX >= 700) {
            laser.remove();
        } else {
            laser.style.left =`${pX + 8}px`;
        }
    }, 10);
}

function criaInimigos() {
    let novoAlien = document.createElement('img');
    //sorteia Imagens
    let alienSprite = inimigosImg[Math.floor(Math.random() * inimigosImg.length)];
    novoAlien.src = alienSprite;
    novoAlien.classList.add('alien');
    novoAlien.classList.add('alien-transition');
    novoAlien.style.left ='370px';
    novoAlien.style.top = `${Math.floor(Math.random() * 330)+ 30}px`;
    areaJogo.appendChild(novoAlien);
    moveAlien(novoAlien); 
}

function moveAlien(alien){
    let moveAlienInterval = setInterval(() => {
        let possitionX = parseInt(window.getComputedStyle(alien).getPropertyValue('left'));
        if(possitionX <=50){
            if(Array.from(alien.classList).includes('alien-morreu')){
                alien.remove();
            } else  {
                gameOver();
            }
        } else {
            alien.style.left =`${possitionX - 4}px`;
        }
    },30);
}

function colisao (laser,alien){
    let laserTop =parseInt(laser.style.top);
    let laserLeft = parseInt(laser.style.left);
    let laserBot = laserTop -20;
    let alienTop =parseInt(alien.style.top);
    let alienLeft = parseInt(alien.style.left);
    let alienBot = alienTop -30;

    if(laserLeft != 340 && laserLeft + 40 >= alienLeft){
        if(laserTop <= alienTop && laserTop>=alienBot){
            return true;
        } else {
            return false;
        }
    } else {
        return false;
    }
    
}
startButton.addEventListener('click',(evento) =>{
    playGame();
})

function playGame(){
    startButton.style.display = 'none';
    instrucoes.style.display = 'none';
    window.addEventListener('keydown',voaNave);
    ai = setInterval(() => {
        criaInimigos();
    }, 2000);
}

function gameOver (){
    window.removeEventListener('keydown',voaNave);
    clearInterval(ai);
    let aliens = document.querySelectorAll('.alien');
    aliens.forEach((alien) => alien.remove());
    let laser = document.querySelectorAll('.laser');
    laser.forEach((laser)=>laser.remove());
    setTimeout(()=>{
        alert('Game Over');
        suaNave.style.top ="250px";
        startButton.style.display = "block";
        instrucoes.style.display = "block";
    });
}
