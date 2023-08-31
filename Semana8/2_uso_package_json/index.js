import  sumar  from "./funcionabilidad.js";
// cuando si se le coloca llaves (destructuracion) se estara utilizando las funciones, clases, etc que no son por default
import {restar} from "./funcionabilidad.js";
// cuando a la importancion no se coloca llaves se esta importando la funcion, clase, etc, por default
import isOdd from "is-odd-num";

const resultado = sumar(1, 2);
console.log(resultado); // 3

resultado = isOdd(10);
console.log(resultado); // false