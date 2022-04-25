function tamanhoCerto (vetor,tamanho){
    try {
        if (!vetor && !tamanho) 
        throw new ReferenceError("Envie os Parametros ");
        if (typeof vetor !== 'object') 
        throw new TypeError("Envie Parametros Validos");
        if (tamanho !== 'number') 
        throw new TypeError("Envie Parametros Validos");
        if(vetor.length !== tamanho) 
        throw new RangeError ("Tamanho do Vetor Incorreto");

        return vetor;
    } catch (e) {
        if (e instanceof ReferenceError){
            console.log('Esse erro é um ReferenceErro!')
            console.log(e.message)
        } else if (e instanceof TypeError){
            console.log("Esse erro é um TypeErroErro!")
            console.log(e.message)
        } else if (e instanceof RangeError){
            console.log("Esse erro é um RangeErro!")
            console.log(e.message)
        } else {
            console.log("Erro 404 Erro não encontrado"+ e)
        }
    }
}

console.log(tamanhoCerto([1,2,3,4,5],5));