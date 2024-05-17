// Función para validar el formulario de inicio de sesión
function validarInicioSesion() {
    var email = document.getElementById('email').value;
    var password = document.getElementById('password').value;

    // Verificar si ambos campos están completos
    if (email.trim() !== '' && password.trim() !== '') {
        return true; // Si ambos campos están completos, se puede enviar el formulario
    } else {
        return false; // Si falta alguno de los campos, no se puede enviar el formulario
    }
}
