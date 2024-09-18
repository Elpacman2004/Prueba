document.addEventListener('DOMContentLoaded', function() {
    const radioGroups = document.querySelectorAll('.radio-group');
    const DateElements = {
        'botiquin_primeros_auxilios': 'id_First_Aid_Kit_LI',
        'extintor': 'id_Fire_Extinguisher_ED',
        'kit_derrames': 'id_Spill_Kit_LI'
    };

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

    form.addEventListener('change', (event) => {     
        const target = event.target;
        const targetName = target.name;
        if (targetName === 'botiquin_primeros_auxilios' || targetName === 'extintor' || targetName === 'kit_derrames') {
            const mappedValue = DateElements[targetName];
            const specificElement = document.getElementById(mappedValue);
            if (specificElement) {
                if (target.value === 'NC' || target.value === 'NA') {
                    specificElement.required = false;
                }
                else {
                    specificElement.required = true;
                }
            }
        }
    });
});