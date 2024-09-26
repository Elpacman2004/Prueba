function initializeCanvas(canvasId, clearButtonId) {
    console.log('Initializing canvas', canvasId, clearButtonId);
    const canvas = document.getElementById(canvasId);
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

    function draw(x, y) {
        ctx.beginPath();
        ctx.moveTo(lastX, lastY);
        ctx.lineTo(x, y);
        ctx.stroke();
        [lastX, lastY] = [x, y];
    }

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
        }
    });

    canvas.addEventListener('touchend', () => {
        isDrawing = false;
    });

    // Clear canvas function
    function clearCanvas() {
        ctx.clearRect(0, 0, canvas.width, canvas.height);
    }

    document.getElementById(clearButtonId).addEventListener('click', clearCanvas);

    // Check if canvas is empty
    function isCanvasEmpty() {
        const blank = document.createElement('canvas');
        blank.width = canvas.width;
        blank.height = canvas.height;
        return canvas.toDataURL() === blank.toDataURL();
    }

    return { isCanvasEmpty };
}

// Initialize both canvases
const canvas1 = initializeCanvas('firmaCanvas', 'clearButton');
const canvas2 = initializeCanvas('firmaCanvas2', 'clearButton2');

// Form submission validation
document.querySelector('form').addEventListener('submit', function(event) {
    if (canvas1.isCanvasEmpty() || canvas2.isCanvasEmpty()) {
        event.preventDefault();
        alert('Por favor, firme ambos campos antes de enviar el formulario.');
    }
});