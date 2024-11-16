from PIL import Image
import os
from tkinter import Tk
from tkinter.filedialog import askopenfilename

def convert_webp_to_png(input_path):
    # Obtener el nombre del archivo sin extensión y la ruta
    output_path = os.path.splitext(input_path)[0] + ".png"
    # Abrir la imagen en formato WebP
    with Image.open(input_path) as img:
        # Cambiar formato a PNG y guardar
        img.save(output_path, "PNG")
    print(f"Conversión completada: Imagen guardada como {output_path}")

# Configurar ventana de selección de archivo
Tk().withdraw()  # Ocultar la ventana principal de Tkinter
input_path = askopenfilename(
    title="Selecciona una imagen en formato WebP",
    filetypes=[("Imagen WebP", "*.webp")],
    initialdir=os.getcwd()  # Carpeta donde se ejecuta el script
)

# Convertir la imagen si se seleccionó un archivo
if input_path:
    convert_webp_to_png(input_path)
else:
    print("No se seleccionó ninguna imagen.")
