// ECMAScript
import express from "express";

// CommonJs
// const express = require('express');

const productos = [];
const servidor = express();

// antes de cualquier peticion o controlador para que antes de que llegue a ese controlador pase por esta funcionabilidad
servidor.use(express.json()); // para que el servidor entienda el formato json

servidor.get("/", (req, res) => {
  // toda la información del cliente estará en el req
  res.json({
    nessage: "Bienvenido a mi API de Express",
  });
});

servidor
  .route("/productos")
  .post((req, res) => {
    console.log(req.body); // el cuerpo de mi petición
    const data = req.body;
    productos.push(data);

    res.json({
      nessage: "Producto creado exitosamente",
    });
  })
  .get((req, res) => {
    res.json({
      nessage: "Lista de productos",
      content: productos,
    });
  });


// el metodo listen siempre debe ser el ultimo
servidor.listen(3000, () => {
  console.log("Servidor corriendo exitosamente");
});
