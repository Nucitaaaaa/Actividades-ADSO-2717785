
( function() {
    var formulario = document.getElementsByName('formulario')[0],
    campos = formulario.elements,
    boton = document.getElementById('boton');

    var validarNombre = function(e){
        if (formulario.nombre.value === ""){
            alert('El campo "Nombre" no puede estar vacío');
            e.preventDefault();
        }
    };

    var validarApellido = function(e){
        if (formulario.apellido.value === ""){
            alert('El campo "Apellido" no puede estar vacío');
            e.preventDefault();
        }
    };

    var validarCorreo = function(e){
        if (formulario.email.value === ""){
            alert('El campo "Correo Electrónico" no puede estar vacío');
            e.preventDefault();
        }
    };

    var validarContraseña = function(e){
        if (formulario.contrasena.value === ""){
            alert('El campo "Contraseña" no puede estar vacío');
            e.preventDefault();
        }
    };

    var confirmarContraseña = function(e){
        if (formulario.confirmar_contrasena.value === ""){
            alert('El campo "Confirmar Contraseña" no puede estar vacío');
            e.preventDefault();
        } else if (formulario.confirmar_contrasena.value !== formulario.contrasena.value) {
            alert('Las contraseñas no coinciden');
            e.preventDefault();
        }
    }; 

    var validarTerminos = function(e){
        if(!formulario.terminos.checked){
            alert('Debe estar de acuerdo con los términos y condiciones');
            e.preventDefault();
        }
    };

    var validar = function(e) {
        validarNombre(e);
        validarApellido(e);
        validarCorreo(e);
        validarContraseña(e);
        confirmarContraseña(e);
        validarTerminos(e);
    };

    formulario.addEventListener("submit", validar);

})();



