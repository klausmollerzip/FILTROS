from PIL import Image
import os

def convert_to_jpg():
    # Directorio específico donde están las imágenes
    img_dir = r"C:\Users\evigl\Documents\PRESTO\WEB\FILTROS\img"
    print(f"Trabajando en el directorio: {img_dir}")
    
    # Verificar si el directorio existe
    if not os.path.exists(img_dir):
        print(f"Error: El directorio {img_dir} no existe")
        return
    
    # Contar archivos procesados
    converted = 0
    errors = 0
    
    # Listar todos los archivos
    for filename in os.listdir(img_dir):
        # Solo procesar webp y png
        if filename.lower().endswith(('.webp', '.png')):
            try:
                print(f"\nProcesando: {filename}")
                
                # Rutas completas
                input_path = os.path.join(img_dir, filename)
                new_filename = filename.rsplit('.', 1)[0] + '.jpg'
                output_path = os.path.join(img_dir, new_filename)
                
                # Abrir imagen
                img = Image.open(input_path)
                
                # Convertir y guardar
                if img.mode in ('RGBA', 'LA'):
                    # Crear fondo blanco para imágenes con transparencia
                    background = Image.new('RGB', img.size, (255, 255, 255))
                    background.paste(img, mask=img.split()[-1])
                    background.save(output_path, 'JPEG', quality=90)
                else:
                    img.convert('RGB').save(output_path, 'JPEG', quality=90)
                
                # Cerrar imagen
                img.close()
                
                # Eliminar original
                os.remove(input_path)
                
                print(f"Convertido exitosamente a: {new_filename}")
                converted += 1
                
            except Exception as e:
                print(f"Error procesando {filename}: {str(e)}")
                errors += 1
    
    # Mostrar resumen
    print(f"\nProceso completado:")
    print(f"- Archivos convertidos: {converted}")
    print(f"- Errores: {errors}")

if __name__ == "__main__":
    try:
        convert_to_jpg()
    except Exception as e:
        print(f"Error general: {str(e)}")
    
    input("\nPresiona Enter para cerrar...")