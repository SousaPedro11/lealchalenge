const button = document.querySelector("div input")
const nome = document.getElementById('nome')
const sigla = document.getElementById('sigla')
const cep = document.getElementById('cep')
const numero = document.getElementById('numero')

if (nome && sigla) {
    button.disabled = true;
    nome.onkeyup = function () {
        button.disabled = true;
        button.disabled = nome.value.length === 0 || sigla.value.length !== 2;
    }
    sigla.onkeyup = function () {
        button.disabled = true;
        button.disabled = sigla.value.length !== 2 || nome.value.length === 0;
    }
}else if (nome && cep){
    button.disabled = true;
    nome.onkeyup = function (){
        button.disabled = true;
        button.disabled = nome.value.length === 0 || cep.value.length !==8;
    }
    cep.onkeyup = function () {
        button.disabled = true;
        button.disabled = cep.value.length !==8 || nome.value.length === 0;
    }
}else if (nome){
    button.disabled = true;
    nome.onkeyup = function () {
        button.disabled = true;
        button.disabled = nome.value.length === 0;
    }
}
if(numero){
    if (numero.value.length === 0){
        numero.value = 'S/N'
    }
    numero.onchange = function () {
        if (numero.value.length === 0){
            numero.value = 'S/N';
        }
    }
}
