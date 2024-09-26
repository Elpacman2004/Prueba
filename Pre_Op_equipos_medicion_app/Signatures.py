import base64
from openpyxl.drawing.image import Image
from django.core.files.base import ContentFile
import io
from PIL import Image as PILImage

def Proces_signatures(request, sheet):
    Firma = request.POST['firmaData']	
    format, imgstr = Firma.split(';base64,')
    ext = format.split('/')[-1]
    data = ContentFile(base64.b64decode(imgstr), name='temp.' + ext)

    # Guarda los datos en un BytesIO para poder leerlos varias veces
    data_io = io.BytesIO(data.read())

    image = PILImage.open(data_io)

    if image.getbbox():
        with open(f'signature.png', 'wb') as f:
            # Retrocede el puntero del BytesIO al principio
            data_io.seek(0)
            f.write(data_io.read())

            # Retrocede el puntero del BytesIO al principio
            data_io.seek(0)
            img = PILImage.open(data_io)

            # Cambia el tamaño de la imagen
            img = img.resize((300, 75))

            # Guarda la imagen en un archivo
            img.save(f'signature.png')

            # Cargar la imagen usando openpyxl
            signature_img = Image('signature.png')

    sheet.add_image(signature_img, 'M45')
