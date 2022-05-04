const dino = document.querySelector('.dino');
const fundo = document.querySelector('.fundo');
let isJump = false;
let positionDino = 0;

function checaTecla (event) {
    if(event.keyCode === 32){
        if(!isJump){
            jump();
        }
    }
}

function jump(){
    isJump = true;
    let upInterval = setInterval(() => {
        if(positionDino >= 150){
            clearInterval(upInterval);

            let dowInterval = setInterval(function() {
                if (positionDino <=0){
                    clearInterval(dowInterval);
                    isJump = false;
                } else  {
                    positionDino -=20;
                    dino.style.bottom = `${positionDino}px`;
                }
            }, 20);
        } else {
            positionDino += 20;
            dino.style.bottom = `${positionDino}px`;
        }
    },20);
}


function criaCatus () {
    const cactus = document.createElement('div');
    let cactusPosition = 1200;
    let randomTime = Math.random() * 6000;
    
    fundo.appendChild(cactus);
    cactus.classList.add('cactus');
    cactus.style.left = 1000 + 'px';
    
    
    let leftInterval = setInterval(function() {
        if(cactusPosition < -60 ) {
            clearInterval(leftInterval);
            fundo.removeChild(cactus);
        } else if (cactusPosition > 0 && cactusPosition < 60 && positionDino < 60) {
            clearInterval(leftInterval);
            document.body.innerHTML = '<h1 class = "game-over">Fim de Jogo</h1>'
        } else {
            cactusPosition -= 10;
            cactus.style.left = cactusPosition + 'px';
        }
    }, 20);

    setTimeout(criaCatus,randomTime);
}

criaCatus();
document.addEventListener('keyup',checaTecla);