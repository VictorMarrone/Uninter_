/* for (let i =0; i<=10; i++) {
    console.log(i)
} */

/*  let x = 1
while (x < 9) {
    console.log(x)
    x += 1
} */

/* let continua = false
let contador = 1

while (!continua) {
    continua =!confirm(`[${contador++}] mais um loop?`)
} */

/* let num = 0;

do {
    console.log(num);
    num += 10;
}
while (num < 90); */

/* let raio = prompt("Qual o raio do circulo?");
raio = parseFloat(raio);
let area = (Math.PI*raio**2);
console.log(`O circulo de raio ${raio} possuí uma area de ${area.toFixed(2)}`); */

/* let sexo = prompt("Informe seu sexo: (M/F)")
sexo = sexo.toUpperCase();

switch(sexo) {
    case "M":
        console.log("Sexo Masculino");
        break;
    case "F":
        console.log("Sexo Feminino");
        break;
    default:
        console.log("Sexo inválido!");
        break;
} */

function calcularPorcentagens() {
    let quantidadeHomens = parseInt(document.getElementById("quantidade-homens").value);
    let quantidadeMulheres = parseInt(document.getElementById("quantidade-mulheres").value);
    

let totalAlunos = quantidadeHomens + quantidadeMulheres;
let percentualHomens = (quantidadeHomens / totalAlunos) * 100;
let percentualMulheres = (quantidadeMulheres / totalAlunos) * 100;

let tabela = "<table>";
tabela += "<tr><th></th><th>Quantidade</th><th>Percentual</th></tr>";
tabela += "<tr><td>Homens</td><td>" + quantidadeHomens + "</td><td>" + percentualHomens.toFixed(2) + "%</td></tr>";
tabela +=  "<tr><td>Mulheres</td><td>" + quantidadeMulheres + "</td><td>" + percentualMulheres.toFixed(2) + "%</td></tr>";
tabela += "</table>";


document.getElementById("tabela-porcentagens").innerHTML = tabela;

}