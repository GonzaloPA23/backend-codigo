import express from "express";
import Prisma, { NivelAcademico, TipoGrupoSanguineo } from "@prisma/client";
import Joi from "joi";
import swaggerUI from "swagger-ui-express";
import archivoSwagger from "./swagger.json" assert { type: "json" };
import cors from "cors";

const conexion = new Prisma.PrismaClient();

const servidor = express();

const seccionSchema = Joi.object({
  nombre: Joi.string().required(),
});

const alumnoSchema = Joi.object({
  nombre: Joi.string().required(),
  apellido: Joi.string().required(),
  correo: Joi.string().email().required(),
  telefonoEmergencia: Joi.string().pattern(new RegExp("^[0-9]")).required(),
  grupoSanguineo: Joi.string()
    .valid(
      TipoGrupoSanguineo.AB_NEGATIVO,
      TipoGrupoSanguineo.AB_POSITIVO,
      TipoGrupoSanguineo.A_NEGATIVO,
      TipoGrupoSanguineo.A_POSITIVO,
      TipoGrupoSanguineo.B_NEGATIVO,
      TipoGrupoSanguineo.B_POSITIVO,
      TipoGrupoSanguineo.O_NEGATIVO,
      TipoGrupoSanguineo.O_POSITIVO
    )
    .optional(),
});

const anioLectivoSchema = Joi.object({
    alumnoId: Joi.string().uuid({
        version: "uuidv4"
    }).required(),
    gradoId: Joi.string().uuid({version: "uuidv4"}).required(),
    seccionId: Joi.string().uuid({version: "uuidv4"}).required(),
    anio: Joi.string().required(),
    nivel: Joi.string()
        .valid(NivelAcademico.PRIMARIA, NivelAcademico.SECUNDARIA)
        .required(),
});

servidor.use(
  cors({
    origin: [
      "http://localhost:3000",
      "http://127.0.0.1.3000",
      "https://mifrontend.com",
    ],
    // lOS METODOS QUE SE PUEDEN HACER PETICIONES
    methods: ["GET", "POST", "PUT", "DELETE"],
    // las cabeceras permitidas para que puedan ser enviadasa al backend
    allowedHeaders: ['Authorization','Content-Type','Accept']
  })
);
servidor.use("/docs", swaggerUI.serve, swaggerUI.setup(archivoSwagger));
servidor.use(express.json());

const PORT = 3000;

servidor
  .route("/grados")
  .post(async (req, res) => {
    const { body: data } = req; // cuerpo de la peticion  // destructuracion de objetos req.body ahora sera data
    try {
      const resultado = await conexion.grado.create({
        data,
        // {
        //     nombreNumerico: body.nombreNumerico,
        //     nombreTexto: body.nombreTexto,
        // }
      });
      console.log(resultado);
      res.json({
        message: "Grado creado exitosamente",
      }),
        201;
    } catch (error) {
      res.json({
        message: "Error al crear el grado",
      });
      400;
    }
  })
  .get(async (req, res) => {
    const resultado = await conexion.grado.findMany();

    res.json({
      content: resultado,
    });
  });

servidor
  .route("/grado/:id")
  .all(async (req, res, next) => {
    // se viene a comportar como un intermediario (MIDDLEWARE)
    console.log("yo me ejecuto");
    const { id } = req.params;
    try {
      // await conexion.grado.findFirst(); -> finFirst se utiliza si la columna no es única
      const gradoEncontrado = await conexion.grado.findUniqueOrThrow({
        where: { id: id },
      });

      req.grado = gradoEncontrado;
    } catch (error) {
      if (error instanceof Prisma.PrismaClientKnownRequestError) {
        // Error para cualquier consulta erronea a la base de datos
        return res.status(400).json({
          message: "ID del grado invalido",
        });
      }
      return res.status(400).json({
        message: "Error al buscar el curso",
      });
    }
    next();
  })
  .get(async (req, res) => {
    console.log(req.grado);

    return res.json({
      content: req.grado,
    });
  })
  .put(async (req, res) => {
    const { body } = req;

    const respuesta = await conexion.grado.update({
      where: { id: req.grado.id },
      data: body,
    });

    return res.json({
      message: "Grado actualizado exitosamente",
      content: respuesta,
    });
  })
  .delete(async (req, res) => {
    const respuesta = await conexion.grado.delete({
      where: { id: req.grado.id },
    });

    return res.json({
      message: "Grado eliminado exitosamente",
      content: respuesta,
    });
  });

servidor
  .route("/secciones")
  .post(async (req, res) => {
    const { body } = req;
    // value > la información correctamente validada
    // error > los errores
    // Si hay error no hay value y si hay value no hay error
    const { value, error } = seccionSchema.validate(body);

    if (error) {
      return res.status(400).json({
        message: "Error al crear la seccion",
        content: error,
      });
    }

    const seccionCreada = await conexion.seccion.create({ data: value });

    return res.json({
      message: "Seccion creada exitosamente",
      content: seccionCreada,
    });
  })
  .get(async (req, res) => {
    const resultado = await conexion.seccion.findMany();
    return res.json({
      content: resultado,
    });
  });

servidor.route("/alumnos").post(async (req, res) => {
  const { error, value } = alumnoSchema.validate(req.body);

  if (error) {
    return res.json({
      message: "Error al crear alumno",
      content: error.details,
    });
  }

  const respuesta = await conexion.alumno.create({ data: value });
  return res.status(201).json({
    message: "Alumno creado exitosamente",
    content: respuesta,
  });
});

servidor.route("/anio-lectivo").post(async(req,res)=>{
    const {error,value} = anioLectivoSchema.validate(req.body);
    if(error){
        return res.json({
            message: "Error al crear el año lectivo",
            content: error.details,
        });
    }

    // TODO: VALIDAR QUE EL ALUMNOID, GRAOID Y SECCIONID existan, sino existe no permitir la creacion del año lectivo

    await conexion.anioLectivo.create({data: value});
    return res.status(201).json({
        message: "Año lectivo creado exitosamente"
    })

})

servidor.listen(PORT, () => {
  console.log(`Servidor corriendo exitosamente en el puerto ${PORT}`);
});
