import base64
from PIL import Image
from django.core.files.base import ContentFile
import io


def Proces_signatures(request):
    def save_signature_image(base64_str, filename):
        format, imgstr = base64_str.split(';base64,')
        ext = format.split('/')[-1]
        data = ContentFile(base64.b64decode(imgstr), name='temp.' + ext)

        # Guarda los datos en un BytesIO para poder leerlos varias veces
        data_io = io.BytesIO(data.read())

        image = Image.open(data_io)

        if image.getbbox():
            with open(filename, 'wb') as f:
                # Retrocede el puntero del BytesIO al principio
                data_io.seek(0)
                f.write(data_io.read())

                # Retrocede el puntero del BytesIO al principio
                data_io.seek(0)
                img = Image.open(data_io)

                # Cambia el tamaño de la imagen
                img = img.resize((130, 50))

                # Guarda la imagen en un archivo
                img.save(filename)

    firma1_path = 'firma1.png'
    firma2_path = 'firma2.png'
    save_signature_image(request.POST['firmaData'], firma1_path)
    save_signature_image(request.POST['firmaData2'], firma2_path)

    return firma1_path, firma2_path

