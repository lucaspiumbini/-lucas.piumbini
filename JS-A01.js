//[JS-A01] Considere três notas (n1, n2, n3) e seus respectivos pesos (p1, p2, p3). Calcule a média ponderada das notas e atribua o resultado à variável 
//"media". Após o cálculo, exiba a média ponderada no console.
//OBS: Para calcular a média ponderada multiplica os valores das notas pelos valores dos pesos, e 
//divide pelas somas de todos os pesos. Lembre-se de declarar valores para os pesos e para as notas.

let notasLista = [8, 6, 6];
let pesoLista = [2, 1, 1]
let cont = 0;
let med = 0;
let soma = 0;
let peso = 0;

while (notasLista[cont] != null) {
    soma = soma + (notasLista[cont] * pesoLista[cont]);
    peso = peso + pesoLista[cont]
    cont +=1;
}


med = soma / peso;

console.log(`soma: ${soma}`)
console.log(`peso: ${peso}`)
console.log(`Média ponderada: ${med}`)
