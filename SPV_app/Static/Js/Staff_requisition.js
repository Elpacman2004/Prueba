document.addEventListener('DOMContentLoaded', function() {
    const radioGroup = document.querySelectorAll('input[name="Reason"]');
    const otherInputDiv = document.getElementById('Which');

    radioGroup.forEach((radio) => {
        radio.addEventListener('change', () => {
            if (radio.value === 'Other') {
                otherInputDiv.style.display = radio.checked ? 'block' : 'none';
            } else {
                otherInputDiv.style.display = 'none';
            }
        });

        if (radio.checked && radio.value !== 'Other') {
            otherInputDiv.style.display = 'none';
        }
    });

    const form = document.querySelector('form');

    form.addEventListener('submit', function(event) {
        const otherRadio = document.querySelector('input[name="Reason"][value="Other"]');
        const otherInput = document.querySelector('input[name="Which"]');

        if (otherRadio && otherRadio.checked && (!otherInput || otherInput.value === '')) {
            event.preventDefault();
            alert('Debes ingresar un valor en el campo "¿Cual?" para continuar con el formulario.');
        }
    });
});