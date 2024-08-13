import cv2
import time
import os

# Crear el directorio 'capturas' si no existe
if not os.path.exists('capturas'):
    os.makedirs('capturas')

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: No se puede abrir la cámara")
    exit()

# Configurar la resolución deseada (por ejemplo, 1920x1080)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 8000)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 6000)

# Capturar una imagen
ret, frame = cap.read()
if not ret:
    print("Error: No se puede recibir la imagen (finalizando el flujo...)")
else:
    timestamp = int(time.time())
    img_name = f"capturas/captura_{timestamp}.jpg"
    cv2.imwrite(img_name, frame)
    print(f"{img_name} guardada!")

cap.release()
cv2.destroyAllWindows()

