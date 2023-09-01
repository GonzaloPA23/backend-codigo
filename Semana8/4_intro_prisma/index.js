import  express from "express";
import  Prisma  from "@prisma/client";

const conexion = new Prisma.PrismaClient();

const servidor = express();

servidor.use(express.json());

const PORT = 3000;

servidor.route("/grados").post(async (req,res)=>{
    const {body:data}  = req; // cuerpo de la peticion  // destructuracion de objetos req.body ahora sera data
    try {
        const resultado = await conexion.grado.create({
            data,
            // {
            //     nombreNumerico: body.nombreNumerico,
            //     nombreTexto: body.nombreTexto,
            // }
        })
        console.log(resultado);
        res.json({
            message: "Grado creado exitosamente",
        }), 201;
    } catch (error) {
        res.json({
            message: "Error al crear el grado",
        }); 400;            
    }
}).get(async(req,res)=>{
    const resultado = await conexion.grado.findMany();

    res.json({
        content: resultado,
    })
})


servidor.listen(PORT,()=>{
    console.log(`Servidor corriendo exitosamente en el puerto ${PORT}`)
})