// 1. sin usar la libreria is-odd-num como podriamos saber si un numero es par o impar

const esParOImpar = (num) => {
    if(num % 2 === 0){
        return console.log('es par');
    }else{
        return console.log('es impar')
    }
}

esParOImpar(5);

// 2. se tiene el siguiente arreglo
notas = [12, 7, 14, 8, 4, 8, 18];
// Filtar solo las notasc que son mayores a 10

const notasMayoresA10 = notas.filter((nota)=>{
    return nota > 10;
})

console.log(notasMayoresA10);

// 3. se tiene el siguiente arreglo
alumnos = [
  {
    nombre: "edu",
    notas: 18,
  },
  {
    nombre: "juan",
    notas: 10,
  },
  {
    nombre: "mari",
    notas: 11,
  },
  {
    nombre: "yuli",
    notas: 8,
  },
];
// devolver en otro arreglo las notas
// resultado: [18, 10, 11, 8]

const arreglo2 = alumnos.map((alumno) => {
    return alumno.notas;
})

console.log(arreglo2);