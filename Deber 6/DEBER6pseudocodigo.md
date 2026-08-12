ALGORITMO Evaluacion_Formativa_Docentes

    INICIO

    // 1. Inicio de sesión
    MOSTRAR "Bienvenido a la App de Evaluación Formativa"
    SOLICITAR usuario
    SOLICITAR contraseña

    SI credenciales_correctas ENTONCES

        MOSTRAR "Inicio de sesión exitoso"

        // 2. Seleccionar competencia digital
        MOSTRAR "Seleccione una competencia digital:"
        MOSTRAR "1. Seguridad digital"
        MOSTRAR "2. Inteligencia Artificial"
        MOSTRAR "3. Comunicación digital"
        MOSTRAR "4. Tecnologías de la Información"
        MOSTRAR "5. Entornos virtuales de aprendizaje"

        LEER competencia

        // 3. Seleccionar tipo de evaluación
        MOSTRAR "Seleccione el tipo de evaluación:"
        MOSTRAR "1. Tema de investigación"
        MOSTRAR "2. Actividad práctica"

        LEER tipo_evaluacion

        // 4. Generar actividad mediante IA
        actividad <- IA_Generar_Actividad(
                        competencia,
                        tipo_evaluacion
                     )

        rubrica <- IA_Generar_Rubrica(
                        competencia,
                        actividad
                   )

        MOSTRAR actividad
        MOSTRAR rubrica

        // 5. El docente desarrolla la actividad
        MOSTRAR "Ingrese su respuesta:"
        LEER respuesta_docente

        // 6. Evaluar respuesta mediante IA
        resultado <- IA_Evaluar(
                        actividad,
                        respuesta_docente,
                        rubrica
                     )

        puntuacion <- resultado.puntuacion
        justificacion <- resultado.justificacion
        fortalezas <- resultado.fortalezas
        debilidades <- resultado.debilidades
        sugerencias <- resultado.sugerencias

        // 7. Verificar cumplimiento de criterios
        SI puntuacion >= 7 ENTONCES

            estado <- "CUMPLE CON LOS CRITERIOS"

        SINO

            estado <- "REQUIERE MEJORA"

        FIN SI

        // 8. Generar retroalimentación
        retroalimentacion <- IA_Generar_Retroalimentacion(
                                puntuacion,
                                fortalezas,
                                debilidades,
                                sugerencias
                             )

        // 9. Mostrar resultados
        MOSTRAR "========== RESULTADOS =========="
        MOSTRAR "Competencia: ", competencia
        MOSTRAR "Puntuación: ", puntuacion
        MOSTRAR "Estado: ", estado
        MOSTRAR "Justificación: ", justificacion
        MOSTRAR "Fortalezas: ", fortalezas
        MOSTRAR "Aspectos por mejorar: ", debilidades
        MOSTRAR "Sugerencias: ", sugerencias
        MOSTRAR "Retroalimentación: ", retroalimentacion

        // 10. Guardar historial
        historial <- CREAR_REGISTRO(
                        usuario,
                        competencia,
                        tipo_evaluacion,
                        actividad,
                        respuesta_docente,
                        puntuacion,
                        justificacion,
                        sugerencias
                     )

        GUARDAR historial

        // 11. Continuar aprendiendo
        MOSTRAR "¿Desea realizar otra actividad?"
        LEER opcion

        SI opcion = "SI" ENTONCES
            VOLVER A seleccionar competencia
        SINO
            MOSTRAR "Gracias por utilizar la aplicación"
        FIN SI

    SINO

        MOSTRAR "Usuario o contraseña incorrectos"

    FIN SI

    FIN

FIN ALGORITMO