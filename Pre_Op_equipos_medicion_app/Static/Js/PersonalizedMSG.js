document.addEventListener("DOMContentLoaded", function() {

  function Messages() {
  const form = document.getElementById('Pre-Op');
  const formElements = form.elements;

  for (let i = 0; i < formElements.length; i++) {
      const element = formElements[i];

      if (element.type === 'radio') {
          const radioGroup = form.querySelectorAll(`input[name="${element.name}"]`);
          const isChecked = Array.from(radioGroup).some(radio => radio.checked);
          if (!isChecked) {
            console.log(`El grupo de radio buttons con el nombre "${element.name}" está vacío.`);
          }
        }
          else if (!element.value) {
            console.log(`El campo con el nombre "${element.name}" está vacío.`);
            element.required = true;
            element.setCustomValidity("Este campo es obligatorio.");
          } 
          else {
            console.log("Removing required attribute from element:", element);
            element.required = false;
            element.setCustomValidity("");
          }
      }
    };

  Messages();
});