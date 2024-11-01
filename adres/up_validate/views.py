from django.shortcuts import render
import csv
import re
from .forms import CSVUploadForm

def validar_csv(request):
    mensaje = None
    errores = []

    if request.method == 'POST':
        form = CSVUploadForm(request.POST, request.FILES)
        if form.is_valid():
            archivo = request.FILES['archivo_csv']
            
            # Verificar el formato del archivo
            if not (archivo.name.endswith('.csv') or archivo.name.endswith('.txt')):
                errores.append("Formato de archivo no aceptado. Por favor, suba un archivo .csv o .txt.")
            else:
                # Leer y validar el contenido del archivo CSV
                reader = csv.reader(archivo.read().decode('utf-8').splitlines())
                for i, fila in enumerate(reader, start=1):
                    # Validar número de columnas
                    if len(fila) != 5:
                        errores.append(f"Fila {i}: Número incorrecto de columnas ({len(fila)}). Debe ser 5.")
                        continue

                    # Validar Columna 1 (número entero de 3 a 10 caracteres)
                    if not (fila[0].isdigit() and 3 <= len(fila[0]) <= 10):
                        errores.append(f"Fila {i}, Columna 1: Debe ser un número entre 3 y 10 caracteres.")

                    # Validar Columna 2 (correo electrónico)
                    if not re.match(r"[^@]+@[^@]+\.[^@]+", fila[1]):
                        errores.append(f"Fila {i}, Columna 2: Formato de correo electrónico inválido.")

                    # Validar Columna 3 (valores “CC” o “TI”)
                    if fila[2] not in ["CC", "TI"]:
                        errores.append(f"Fila {i}, Columna 3: Solo se permite 'CC' o 'TI'.")

                    # Validar Columna 4 (valor entre 500000 y 1500000)
                    try:
                        valor = int(fila[3])
                        if not (500000 <= valor <= 1500000):
                            errores.append(f"Fila {i}, Columna 4: Debe estar entre 500000 y 1500000.")
                    except ValueError:
                        errores.append(f"Fila {i}, Columna 4: Debe ser un número entero.")

                # Si no hay errores, el archivo es válido
                if not errores:
                    mensaje = f"Archivo '{archivo.name}' validado exitosamente."

    else:
        form = CSVUploadForm()

    return render(request, 'up_validate/validar_csv.html', {'form': form, 'mensaje': mensaje, 'errores': errores})
