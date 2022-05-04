function start () {

    $("#inicio").hide();
    $("#fundoGame").append("<div id='jogador'class= 'anima1'></div>");
    $("#fundoGame").append("<div id='inimigo1'class= 'anima2'></div>");
    $("#fundoGame").append("<div id='inimigo2'></div>");
    $("#fundoGame").append("<div id='amigo'class='anima3'></div>");
    $("#fundoGame").append("<div id='placar'></div>");
    $("#fundoGame").append("<div id='energia'></div>");

    var somDisparo=document.getElementById("somDisparo");
    var somExplosao=document.getElementById("somExplosao");
    var musica=document.getElementById("musica");
    var somGameover=document.getElementById("somGameover");
    var somPerdido=document.getElementById("somPerdido");
    var somResgate=document.getElementById("somResgate");

    var disparoLivre = true;
    var fimdejogo = false;
    var jogo = {};
    var pontos = 0;
    var perdidos = 0;
    var salvos = 0;
    var velocidade = 5;
    var energiaAtual = 3;
    var positionY = parseInt(Math.random() *344);
    var TECLA = {
        w:87,
        s:83,
        e:69
    }




    jogo.timer =setInterval(loop,30);
    jogo.checaTecla = []; 

    function loop () {
        moveFundo();
        moveJogador();
        moveInimigo1();
        moveInimigo2();
        moveAmigo();
        colisao();
        placar();
        energia();
        

        musica.addEventListener("ended", function(){ musica.currentTime = 0; musica.play(); }, false);musica.play();
    }

    function moveFundo (){
        esquerda = parseInt($("#fundoGame").css("background-position"));
        $("#fundoGame").css("background-position",esquerda-1);
    }


    $(document).keydown(function (e) { 
        jogo.checaTecla[e.which] = true
    });

    $(document).keyup(function (e) { 
        jogo.checaTecla[e.which] = false
    });

    function moveJogador() { 
        if (jogo.checaTecla[TECLA.w]) {
            var move = parseInt($("#jogador").css("top"));
            $("#jogador").css("top",move-10);
            if (move <= 5) {
                $("#jogador").css("top",move+10);
            }
        }

        if (jogo.checaTecla[TECLA.s]) {
            var move = parseInt($("#jogador").css("top"));
            $("#jogador").css("top",move+10);
            if (move >= 434) {
                $("#jogador").css("top",move-10);
            }
        }
        
        if(jogo.checaTecla[TECLA.e]){
            disparo();
        }
    }


    function moveInimigo1(){
        positionX = parseInt($("#inimigo1").css("left"));
        $("#inimigo1").css("left",positionX-velocidade);
        $("#inimigo1").css("top",positionY);

        if(positionX <= 0) {
            positionY = parseInt(Math.random() * 334);
            $("#inimigo1").css("left",694);
            $("#inimigo1").css("top",positionY);
        }
    }

    function moveInimigo2() {
        positionX = parseInt($("#inimigo2").css("left"));
        $("#inimigo2").css("left",positionX - 3);

        if (positionX <=0) {
            $("#inimigo2").css("left",775);
        }


    }


    function moveAmigo(){
        positionX = parseInt($("#amigo").css("left"));
        $("#amigo").css("left",positionX + 1);

        if (positionX > 906) {
            $("#amigo").css("left",0);
        }
    }

    function disparo(){
        if (disparoLivre == true){
            somDisparo.play();
            disparoLivre = false;

            move = parseInt($("#jogador").css("top"));
            posicaonX = parseInt($("#jogador").css("left"));
            tiroX = posicaonX + 190;
            topoTiro=move+37;

            $("#fundoGame").append("<div id = 'disparo'></div");
            $("#disparo").css("top", topoTiro);
            $("#disparo").css("left",tiroX);

            var tempoDisparo = window.setInterval(executaDisparo,30);
        }

        function executaDisparo (){
            posicaonX = parseInt ($("#disparo").css("left"));
            $("#disparo").css("left",posicaonX+15);
    
            if (posicaonX > 900){
                window.clearInterval(tempoDisparo);
                tempoDisparo=null;
                $("#disparo").remove();
                disparoLivre = true;
            }
        } 
    }//fecha disparo


    function colisao () {
        var colisao1 = ($("#jogador").collision($("#inimigo1")));
        var colisao2 = ($("#jogador").collision($("#inimigo2")));
        var colisao3 = ($("#disparo").collision($("#inimigo1")));
        var colisao4 = ($("#disparo").collision($("#inimigo2")));
        var colisao5 = ($("#jogador").collision($("#amigo")));
        var colisao6 = ($("#inimigo2").collision($("#amigo")));
        

        if (colisao1.length > 0) {
            energiaAtual --;
            inimigo1X =($("#inimigo1").css("left"));
            inimigo1Y =($("#inimigo1").css("top"));
            explosao1(inimigo1X,inimigo1Y);

            positionY = parseInt(Math.random() * 334);
            $("#inimigo1").css("left",694);
            $("#inimigo1").css("top",positionY);
        }
        if (colisao2.length > 0) {
            energiaAtual--;
            inimigo2X =($("#inimigo2").css("left"));
            inimigo2Y =($("#inimigo2").css("top"));
            explosao2(inimigo2X,inimigo2Y);

            $("#inimigo2").remove();
            reposicionaInimigo2();
        }

        if (colisao3.length>0){
            pontos += 100;
            velocidade += 0.3;
            inimigo1X =($("#inimigo1").css("left"));
            inimigo1Y =($("#inimigo1").css("top"));
            explosao1(inimigo1X,inimigo1Y);
            $('#disparo').css("left",950);
            positionY = parseInt(Math.random() * 334);
            $("#inimigo1").css("left",694);
            $("#inimigo1").css("top",positionY);


        }

        if (colisao4.length>0){
            pontos += 50;
            inimigo2X =($("#inimigo2").css("left"));
            inimigo2Y =($("#inimigo2").css("top"));
            $("#inimigo2").remove();

            explosao2(inimigo2X,inimigo2Y);
            $('#disparo').css("left",950);
            reposicionaInimigo2();
        }

        if (colisao5.length>0) {
            salvos++;
            somResgate.play();
            reposicionaAmigo();
            $("#amigo").remove();
        }

        if (colisao6.length>0) {
            perdidos++;
            if (pontos < 150){pontos -= pontos;} else {pontos -= 150;}
            amigoX =($("#amigo").css("left"));
            amigoY =($("#amigo").css("top"));
            explosao3(amigoX,amigoY);
            $("#amigo").remove();

            reposicionaAmigo();
        }

    }

    function explosao1 (inimigo1X,inimigo1Y){
        somExplosao.play();
        $("#fundoGame").append("<div id = 'explosao1'></div");
        var div =$("#explosao1");
        div.css("top",inimigo1Y);
        div.css("left",inimigo1X);
        div.animate({width:200, opacity:0},"slow");

        var tempoExplosao=window.setInterval(removeExplosao,1000);

        function removeExplosao () {
            div.remove();
            window.clearInterval(tempoExplosao);
            tempoExplosao = null;
        }
    }

    function explosao2 (inimigo2X,inimigo2Y){
        somExplosao.play();
        $("#fundoGame").append("<div id = 'explosao2'></div");
        let div =$("#explosao2");
        div.css("top",inimigo2Y);
        div.css("left",inimigo2X);
        div.animate({width:200, opacity:0},"slow");

        let tempoExplosao=window.setInterval(removeExplosao,1000);

        function removeExplosao () {
            div.remove();
            window.clearInterval(tempoExplosao);
            tempoExplosao = null;
        }
    }

    function explosao3(amigoX,amigoY) {
        somPerdido.play();
        $("#fundoGame").append("<div id = 'explosao3' class ='anima4'></div");
        let div =$("#explosao3");
        div.css("top",amigoY);
        div.css("left",amigoX);

        let tempoExplosao3=window.setInterval(removeExplosao3,1000);

        function removeExplosao3 () {
            div.remove();
            window.clearInterval(tempoExplosao3);
            tempoExplosao3 = null;
        }
    }

    function reposicionaInimigo2(){
        var tempoColisao4=window.setInterval(reposiciona4,5000);

        function reposiciona4() {
            window.clearInterval(tempoColisao4);
            tempoColisao4=null;

            if (fimdejogo == false){
                $("#fundoGame").append("<div id=inimigo2></div");

            }
        }
    }

    function reposicionaAmigo () {
        var tempoAmigo=window.setInterval(reposiciona6,5000);

        function reposiciona6() {
            window.clearInterval(tempoAmigo);
            tempoAmigo=null;

            if (fimdejogo == false){
                $("#fundoGame").append("<div id='amigo'class='anima3'></div");

            }
        }
    }

    function placar(){
        $("#placar").html("<h2>Pontos: " + pontos + " Salvos: " + salvos + " Perdidos: " + perdidos + "</h2>");
    }

    function energia (){
        if (energiaAtual === 3) {
            $("#energia").css("background-image", "url(./arquivos/imgs/energia3.png)")
        }
        if (energiaAtual === 2) {
            $("#energia").css("background-image", "url(./arquivos/imgs/energia2.png)")
        }
        if (energiaAtual === 1) {
            $("#energia").css("background-image", "url(./arquivos/imgs/energia1.png)")
        }
        if (energiaAtual === 0) {
            $("#energia").css("background-image", "url(./arquivos/imgs/energia0.png)")
            gameOver();
        }
    }

    function gameOver() {
        fimdejogo=true;
        musica.pause();
        somGameover.play();
        
        window.clearInterval(jogo.timer);
        jogo.timer=null;
        
        $("#jogador").remove();
        $("#inimigo1").remove();
        $("#inimigo2").remove();
        $("#amigo").remove();
        
        $("#fundoGame").append("<div id='fim'></div>");
        
        $("#fim").html("<h1> Game Over </h1><p>Sua pontuação foi: " + pontos + "</p>" + "<div id='reinicia' onClick=reiniciaJogo()><h3>Jogar Novamente</h3></div>");
        }
}

function reiniciaJogo(){
    somGameover.pause();
    $("#fim").remove();
    start();
}
