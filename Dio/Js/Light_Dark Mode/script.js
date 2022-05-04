function changeMode () {
    console.log('cliquei')
}


const button = document.getElementById('mode-selector');
const h1= document.getElementById('page-title');
const body = document.getElementsByTagName('body')[0];
const footer = document.getElementsByTagName('footer')[0];

console.log(body);

button.addEventListener('click', changeMode);
    