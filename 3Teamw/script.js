// script.js
window.onload = function() {
    document.getElementById("button1").addEventListener("click", function() {
        var input = document.getElementById("inputField").value;
        document.getElementById("outputField").innerText = input;
    });
};

