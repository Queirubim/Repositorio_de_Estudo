const BASE_URL = 'https://thatcopy.pw/catapi/rest/';
const botGatinho = document.getElementById('carrega-gato')
const imgGatinho = document.getElementById('gato')

const carreGatinho = async () => {
    try {
        const data = await fetch (BASE_URL);
        const json = await data.json();

    return json.webpurl;
    } catch (e) {
        console.log((e.message));
    }
};

const carregaimg = async () => {
    imgGatinho.src = await carreGatinho ();
}

botGatinho.addEventListener('click', carregaimg);

carregaimg();