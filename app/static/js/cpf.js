const input = document.getElementById('entrada');
const button = document.getElementById('submit');

button.disabled = true
input.onkeyup = function () {
    input.style.color = "black";
    button.disabled = true;
    button.disabled = input.value.length !== 11;

    if (!isNumeric(input.value) || input.value.indexOf('.') > -1) {
        input.value = input.value.substr(0, input.value.length - 1);
    }
    let max_char = 11;
    if (input.value.length > max_char) {
        input.value = input.value.substr(0, max_char);
        button.disabled = false;
    }else if (input.value.length < max_char){
        input.style.color = "red";
    }else {
        input.style.color = 'black';
    }
}

function isNumeric(n) {
    return !isNaN(parseFloat(n)) && isFinite(n);
}

