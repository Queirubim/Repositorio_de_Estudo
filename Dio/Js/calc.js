
function calculador(){
    const operac = Number(prompt("Escolha uma operação: \n 1- soma (+)\n 2 - Subtração (-) \n 3 - Multiplicação (*) \n 4 - Divisão (/)\n 5 - Divisão Inteira (%) \n 6 - Potenciação (**) "));
    if (!operac ||operac>= 7 ){
    alert('Erro operação invalida');
    calculador();
    } else{
        let n1 = Number(prompt('Insira o primeiro valor '));
        let n2 = Number(prompt('Insira o segundo valor '));
        let resultado;

        if (!n1 || !n2){
            alert("Erro 404");
            calculador();
        } else {
            function soma (){
            resultado = n1 + n2;
            alert(`${n1} + ${n2} = ${resultado}`)
            novaoperacao();
        }
        function subtracao (){
            resultado = n1 - n2;
            alert(`${n1} - ${n2} = ${resultado}`)
            novaoperacao();
        }
        function multiplicacao (){
            resultado = n1 * n2;
            alert(`${n1} * ${n2} = ${resultado}`)
            novaoperacao();
        }
        function divisao (){
            resultado = n1 / n2;
            alert(`${n1} / ${n2} = ${resultado}`)
            novaoperacao();
        }
        function divisaoint (){
            resultado = n1 % n2;
            alert(`O resto da divisão entre ${n1} % ${n2} = ${resultado}`)
            novaoperacao();
        }
        function potenciacao (){
            resultado = n1 ** n2;
            alert(`${n1} ^ ${n2} = ${resultado}`)
            novaoperacao();
        }

        function novaoperacao(){
            let opera = prompt("Deseja fazer uma nova operação ?\n 1 - Sim \n 2 - Não")

            if (opera == 1 ){
                calculador();
            } else if(opera == 2) {
                alert('Ate Logo!')
            } else {
                alert('Digite uma opção valida')
                novaoperacao();
            }
        }

        
        }

        if (operac == 1) {
            soma ();
        } else if (operac == 2){
            subtracao();
        } else if (operac == 3){
            multiplicacao();
        } else if (operac == 4){
            divisao();
        } else if (operac == 5){
            divisaoint();
        } else if (operac == 6){
            potenciacao();
        }

    }

}

calculador()
