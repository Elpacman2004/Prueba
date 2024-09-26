// Archivo: Elements.js

// Función para inicializar elementos
function initializeElements() {
    console.log("Inicializando elementos...");
    const id_equipment = document.getElementById("id_id_eqipment");

    function validateField() {  
        if (id_equipment.value === 'EDP-XXX') {
            id_equipment.required = true;
            id_equipment.setCustomValidity("Es necesario que cambies el valor 'EDP-XXX' por el id del equipo.");
        }
        else if (id_equipment.value === '') {
            id_equipment.required = true;
            id_equipment.setCustomValidity("Este campo es obligatorio.");
        }
        else {
            id_equipment.required = false;
            id_equipment.setCustomValidity("");
        }
    }
    validateField();
    id_equipment.addEventListener('input', validateField);

}
// Llamada a la función de inicialización cuando el DOM esté completamente cargado
document.addEventListener("DOMContentLoaded", function() {
    initializeElements();
});