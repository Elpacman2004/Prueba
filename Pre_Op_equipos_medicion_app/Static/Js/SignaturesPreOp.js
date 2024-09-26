const canvas = document.getElementById('firmaCanvas');
console.log("SignaturesG.js loaded");
const ctx = canvas.getContext('2d');
let isDrawing = false;
let lastX = 0;
let lastY = 0;

function resizeCanvas() {
    canvas.width = canvas.offsetWidth;
    canvas.height = canvas.offsetHeight;
    }

    window.addEventListener('resize', resizeCanvas);
    resizeCanvas();

    // Events for mouse
    canvas.addEventListener('mousedown', (e) => {
        isDrawing = true;
        [lastX, lastY] = [e.offsetX, e.offsetY];
    });

    canvas.addEventListener('mousemove', (e) => {
        if (isDrawing) {
            draw(e.offsetX, e.offsetY);
        }
    });

    canvas.addEventListener('mouseup', () => {
        isDrawing = false;
    });

    // Events for touch (mobile)
    canvas.addEventListener('touchstart', (e) => {
        isDrawing = true;
        const touch = e.touches[0];
        const rect = canvas.getBoundingClientRect();
        [lastX, lastY] = [
            (touch.clientX - rect.left) * (canvas.width / rect.width),
            (touch.clientY - rect.top) * (canvas.height / rect.height)
        ];
        e.preventDefault();  // Prevent scrolling while drawing
    });

    canvas.addEventListener('touchmove', (e) => {
        if (isDrawing) {
            const touch = e.touches[0];
            const rect = canvas.getBoundingClientRect();
            draw(
                (touch.clientX - rect.left) * (canvas.width / rect.width),
                (touch.clientY - rect.top) * (canvas.height / rect.height)
            );
            e.preventDefault();  // Prevent scrolling while drawing
        }
    });

    canvas.addEventListener('touchend', () => {
        isDrawing = false;
});

function draw(x, y) {
    ctx.lineWidth = 2;
    ctx.lineCap = 'round';
    ctx.strokeStyle = 'var(--primary)';

    ctx.beginPath();
    ctx.moveTo(lastX, lastY);
    ctx.lineTo(x, y);
    ctx.stroke();
    [lastX, lastY] = [x, y];
}

function validateSignatures() {
    var canvas = document.getElementById('firmaCanvas');
    var firmaData = document.getElementById('firmaData');

    if (isCanvasBlank(canvas)) {
        alert('Por favor, ponga su firma.');
        return false;
    }

    firmaData.value = canvas.toDataURL();

    return true;
}

function saveSignature() {
    const firmaData = document.getElementById('firmaData');
    firmaData.value = canvas.toDataURL('image/png');
}

function isCanvasBlank(canvas) {
    var blank = document.createElement('canvas');
    blank.width = canvas.width;
    blank.height = canvas.height;
    return canvas.toDataURL() == blank.toDataURL();
}

function clearCanvas() {
    ctx.clearRect(0, 0, canvas.width, canvas.height);
}

function validateAndSaveSignatures() {
    if (validateSignatures()) {
        saveSignature();
        return true; // Permite el envío del formulario
    }
    return false; // Previene el envío del formulario si la validación falla
}