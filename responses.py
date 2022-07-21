#Respuestas del bot
intents = [
    [
        r"se me ha caido el internet|No tengo internet|No me va el internet|No tengo línea|No tengo red| se ha caido internet",
        ["Sentimos ese fallo, puede probar a reiniciar su router. En caso de que siga teniendo problemas dígame su nombre y apellidos por favor",]
    ],
    [
        r"mi nombre es (.*)| me llamo (.*)",
        ["Perfecto %1 un operario se pondrá en contacto con usted lo antes posible",]
    ],
    [
        r"cuando se paga la factura|cuando tengo que pagar la factura| cuando me pasan los recibos |cuando tengo que pagar |cuando pago",
        ["Le pasan la factura el primero de cada mes",]
    ],
    [
        r"promociones|información de promociones|ofertas|quiero saber ofertas|descuentos|quiero ver descuentos|ver descuentos|ver ofertas|ver promociones",
        ["Si tiene un teléfono móvil contratado con nosotros, puede vincularlo a su factura de fibra y le hacemos un 15 por ciento durante el mes de agosto",]
    ],
    [
        r"hola|hey|buenas|buenas tardes|buenos dias|saludos",
        ["Hola", "¿en qué puedo ayudarte?",]
    ],
    [
        r"Necesito soporte|necesito ayuda|soporte|soporte tecnico|ayuda tecnica",
        ["Puede contactarnos en el telefono 647563746, estaremos encantados de ayudarle",]
        
    ],
    [
        r"queja|quiero poner una queja|estoy descontento|reclamacion|quiero poner una reclamacion",
        ["Sentimos que no esté contento con nuestros servicios, mande un correo a soporte@soport.com y allí le guiarán en todo el proceso",]
    ],
    [
        r"finalizar|adios|gracias|hasta otra|hasta luego",
        ["Adios","recuerda que puedes ver más información de nuestros servicios en www.serviciointernet.net"]
],
]