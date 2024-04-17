document.addEventListener('DOMContentLoaded', function() {
    // Encuentra todos los radio buttons de "No Cumple" en el formulario
    const noCumpleRadioButtons = document.querySelectorAll('input[type="radio"][value="NC"]');

    // Oculta todos los inputs de archivo relacionados al inicio
    noCumpleRadioButtons.forEach(radio => {
        const fotoInput = radio.closest('ul').querySelector('input[type="file"]');
        if (fotoInput) {
            fotoInput.style.display = 'none';
        }
    });

    // Añade un evento de cambio a cada radio button para mostrar/ocultar el input de archivo
    noCumpleRadioButtons.forEach(radio => {
        radio.addEventListener('change', function() {
            const fotoInput = radio.closest('ul').querySelector('input[type="file"]');
            if (fotoInput) {
                // Muestra el input de archivo solo si el radio button de "No Cumple" está seleccionado
                fotoInput.style.display = radio.checked ? 'block' : 'none';
            }
        });
    });

    // Añade un evento de cambio a cada grupo de radio buttons para verificar que al menos una opción esté seleccionada
    const radioGroups = document.querySelectorAll('ul[data-group]');
    radioGroups.forEach(group => {
        const radioButtons = group.querySelectorAll('input[type="radio"]');
        radioButtons.forEach(radio => {
            radio.addEventListener('change', function() {
                if (!this.checked && !group.querySelector('input[type="radio"]:checked')) {
                    alert('Debe seleccionar al menos una opción en este grupo.');
                }
            });
        });
    });
});