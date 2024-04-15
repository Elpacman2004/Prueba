document.addEventListener('DOMContentLoaded', function() {
    const checkboxGroups = document.querySelectorAll('.checkbox-group');

    checkboxGroups.forEach(group => {
        const checkboxes = group.querySelectorAll('input[type="checkbox"]');
        const noCumpleCheckbox = group.querySelector('input[name*="_NoCumple"]');
        const fotoInput = group.querySelector(`#fotoInput_${noCumpleCheckbox.id.replace('_NoCumple', '')}`);

        checkboxes.forEach(checkbox => {
            checkbox.addEventListener('change', () => {
                checkboxes.forEach(cb => {
                    if (cb !== checkbox) {
                        cb.checked = false;
                    }
                });

                const fotoInputForCheckbox = group.querySelector(`#fotoInput_${checkbox.id.replace('_Cumple', '')}`);
                if (checkbox === noCumpleCheckbox) {
                    fotoInput.style.display = checkbox.checked ? 'block' : 'none';
                } else {
                    fotoInputForCheckbox.style.display = 'none';
                }
            });
        });

        // Asignar evento 'change' al checkbox 'No cumple' para mostrar u ocultar el campo de foto
        noCumpleCheckbox.addEventListener('change', () => {
            fotoInput.style.display = noCumpleCheckbox.checked ? 'block' : 'none';
        });
    });

    // Validación del formulario
    const form = document.querySelector('form');
    form.addEventListener('submit', (event) => {
        let isValid = true;
        let missingFields = [];

        checkboxGroups.forEach(group => {
            const checkboxes = group.querySelectorAll('input[type="checkbox"]');
            let isChecked = false;
            let missingGroupFields = [];

            checkboxes.forEach(checkbox => {
                if (checkbox.checked) {
                    isChecked = true;

                    if (checkbox === group.querySelector('input[name*="_NoCumple"]')) {
                        const fieldName = checkbox.name.replace('_NoCumple', '');
                        const fotoField = form.querySelector(`input[name="foto_${fieldName}"]`);
                        
                        if (!fotoField || !fotoField.files || fotoField.files.length === 0) {
                            missingGroupFields.push(`${fieldName} y subir una foto`);
                        }
                    }
                }
            });

            if (!isChecked) {
                missingGroupFields.push('al menos una opción');
            }

            if (missingGroupFields.length > 0) {
                isValid = false;
                missingFields.push(`Debes completar ${missingGroupFields.join(', ')} en este grupo.`);
            }
        });

        // Mostrar alerta si hay campos faltantes
        if (!isValid) {
            event.preventDefault(); // Evitar envío del formulario si hay errores
            alert(missingFields.join('\n')); // Mostrar mensaje con todos los campos faltantes
        }
    });
});
