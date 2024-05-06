document.addEventListener('DOMContentLoaded', function() {
    const radioGroups = document.querySelectorAll('.radio-group');

    radioGroups.forEach(group => {
        const radios = group.querySelectorAll('.form-check-input');
        const noCumpleRadio = group.querySelector('.radio-input');
        const fotoInput = group.querySelector('.file-input');

        radios.forEach(radio => {
            radio.addEventListener('change', () => {
                if (radio === noCumpleRadio) {
                    if (radio.checked) {
                        fotoInput.parentElement.style.display = 'block';
                    } else {
                        fotoInput.parentElement.style.display = 'none';
                    }
                } else {
                    fotoInput.parentElement.style.display = 'none';
                }
            });
        });
    });

    const form = document.querySelector('form');

    form.addEventListener('submit', function(event) {
        const radioGroups = document.querySelectorAll('.radio-group');
        let isValid = true;
        let missingFields = [];

        radioGroups.forEach(group => {
            const noCumpleRadio = group.querySelector('input[value="NC"]');
            const fotoInput = group.querySelector('.Menu-de-Imagen input[type="file"]');

            if (noCumpleRadio && noCumpleRadio.checked && (!fotoInput || !fotoInput.files || fotoInput.files.length === 0)) {
                isValid = false;
                if (group.dataset.groupName) {
                    missingFields.push(`Debes subir una foto en el campo ${group.dataset.groupName} para continuar con el formulario.`);
                }
            }
        });

        if (!isValid) {
            event.preventDefault();
            alert(missingFields.join('\n'));
        }
    });
});