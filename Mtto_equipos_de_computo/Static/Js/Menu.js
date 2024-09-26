document.addEventListener('DOMContentLoaded', () => {
    const form = document.getElementById('maintenanceForm');
    const conditionalFields = document.querySelectorAll('.hidden');

    form.addEventListener('change', (event) => {
        const targetField = event.target;
        const targetLabel = targetField.closest('.form-group').querySelector('label').innerText;
        const targetFieldValue = targetField.value;

        console.log(targetLabel, targetFieldValue);

        conditionalFields.forEach(field => {
            console.log(field.id);
            if (targetLabel === field.id.replace('Menu ', '')) {
                if (targetFieldValue === 'No cumple') {
                    field.classList.remove('hidden');
                } else {
                    field.classList.add('hidden');
                }
            }
        });
    });
});