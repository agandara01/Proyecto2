console.log("Saludo")

function editar(nombre,correo,id,contrasenia){
    $("#correo").val(correo)
    $("#nombre").val(nombre)
    $("#id").val(id)
    $("#contrasenia").val(contrasenia)
    $('#formulario').attr('action', 'registro/editar');
}