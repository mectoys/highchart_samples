

function Ajax_HighChart(formData, url) {
    return new Promise(function (resolve, reject) {
        // Realizar solicitud AJAX usando jQuery
        $.ajax({
            // Configurar solicitud POST
            type: 'POST',
            // Especificar la URL
            url: url,
            // Establecer el tipo de contenido
            contentType: 'application/json;charset=UTF-8',
            // Convertir objeto a JSON
            data: JSON.stringify(formData),

            success: function (response) {
                // Resuelve la promesa con la respuesta del servidor

                resolve(response);
            },
            error: function (error) {
                // Rechaza la promesa con el error recibido.

                reject(error);
            },
            complete: function () {
                // Agregar código que se ejecutará después de la solicitud
            }
        });
    });
}