const input = document.getElementById('entrada');
const button = document.getElementById('submit');

button.disabled = true;
input.onkeyup = function () {
    button.disabled = input.value.length === 0
}

