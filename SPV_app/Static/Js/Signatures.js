document.addEventListener("DOMContentLoaded", function() {
    var pads = [1, 2, 3, 4, 5, 6].map(function(i) {
        var canvas = document.getElementById('signature-pad-' + i);
        canvas.width = canvas.offsetWidth;
        canvas.height = canvas.offsetHeight;
        var button = document.getElementById('clear-' + i);
        var signaturePad = new SignaturePad(canvas);

        button.addEventListener('click', function() {
            signaturePad.clear();
        });

        return signaturePad;
    });

    document.getElementById('save').addEventListener('click', function(e) {
        e.preventDefault();

        pads.forEach(function(pad, i) {
            document.getElementById('signature-input-' + (i + 1)).value = pad.toDataURL('image/png');
        });

        e.target.form.submit();
    });
});

var signaturePad1 = new SignaturePad(document.getElementById('signature-pad-1'));
document.getElementById('clear-1').addEventListener('click', function () {
    signaturePad1.clear();
});

var signaturePad2 = new SignaturePad(document.getElementById('signature-pad-2'));
document.getElementById('clear-2').addEventListener('click', function () {
    signaturePad2.clear();
});

var signaturePad3 = new SignaturePad(document.getElementById('signature-pad-3'));
document.getElementById('clear-3').addEventListener('click', function () {
    signaturePad3.clear();
});

var signaturePad4 = new SignaturePad(document.getElementById('signature-pad-4'));
document.getElementById('clear-4').addEventListener('click', function () {
    signaturePad4.clear();
});

var signaturePad5 = new SignaturePad(document.getElementById('signature-pad-5'));
document.getElementById('clear-5').addEventListener('click', function () {
    signaturePad5.clear();
});

var signaturePad6 = new SignaturePad(document.getElementById('signature-pad-6'));
document.getElementById('clear-6').addEventListener('click', function () {
    signaturePad6.clear();
});

document.getElementById('save').addEventListener('click', function () {
    var data1 = signaturePad1.toDataURL('image/png');
    document.getElementById('signature-input-1').value = data1;

    var data2 = signaturePad2.toDataURL('image/png');
    document.getElementById('signature-input-2').value = data2;

    var data3 = signaturePad3.toDataURL('image/png');
    document.getElementById('signature-input-3').value = data3;

    var data4 = signaturePad4.toDataURL('image/png');
    document.getElementById('signature-input-4').value = data4;

    var data5 = signaturePad5.toDataURL('image/png');
    document.getElementById('signature-input-5').value = data5;

    var data6 = signaturePad6.toDataURL('image/png');
    document.getElementById('signature-input-6').value = data6;

});