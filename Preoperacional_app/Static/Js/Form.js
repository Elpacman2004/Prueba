document.addEventListener('DOMContentLoaded', function() {
    // Encuentra todos los grupos de radio buttons en el formulario
    const radioGroups = document.querySelectorAll('.radio-group');

    radioGroups.forEach(group => {
        const noCumpleRadio = group.querySelector('input[value="NC"]');
        const fotoInput = group.querySelector(`#fotoInput_${noCumpleRadio.id.replace('_NC', '')}`);

        const radios = group.querySelectorAll('input[type="radio"]');
        radios.forEach(radio => {
            radio.addEventListener('change', () => {
                radios.forEach(otherRadio => {
                    if (otherRadio !== radio) {
                        otherRadio.checked = false;
                    }
                });

                if (radio === noCumpleRadio) {
                    fotoInput.style.display = radio.checked ? 'block' : 'none';
                } else {
                    fotoInput.style.display = 'none';
                }
            });
        });

        noCumpleRadio.addEventListener('change', () => {
            fotoInput.style.display = noCumpleRadio.checked ? 'block' : 'none';
        });
    });
});
