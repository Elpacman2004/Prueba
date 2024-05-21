document.addEventListener('DOMContentLoaded', function() {
    const radioGroups = ['Transportation_Allowance', 'Travel_Allowance', 'Other'];
    const valueInputs = ['Value_Transportation_Allowance', 'Value_Travel_Allowance', 'Which'];

    radioGroups.forEach((group, index) => {
        const yesRadio = document.querySelector(`input[name="${group}"][value="Yes"]`);
        const noRadio = document.querySelector(`input[name="${group}"][value="No"]`);
        const valueInputDiv = document.getElementById(valueInputs[index]);

        [yesRadio, noRadio].forEach(radio => {
            radio.addEventListener('change', () => {
                if (radio === yesRadio) {
                    valueInputDiv.style.display = radio.checked ? 'block' : 'none';
                } else {
                    valueInputDiv.style.display = 'none';
                }
            });
        });

        if (noRadio.checked) {
            valueInputDiv.style.display = 'none';
        }
    });

    const form = document.querySelector('form');

    form.addEventListener('submit', function(event) {
        let isValid = true;
        let missingFields = [];

        radioGroups.forEach((group, index) => {
            const yesRadio = document.querySelector(`input[name="${group}"][value="Yes"]`);
            const valueInput = document.querySelector(`input[name="${valueInputs[index]}"]`);

            if (yesRadio && yesRadio.checked && (!valueInput || valueInput.value === '')) {
                isValid = false;
                missingFields.push(`Debes ingresar un valor en el campo ${group} para continuar con el formulario.`);
            }
        });

        if (!isValid) {
            event.preventDefault();
            alert(missingFields.join('\n'));
        }
    });
});