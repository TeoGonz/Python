import cv2
import easyocr

def process_frame(frame, reader):

    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    

    result = reader.readtext(gray_frame)
    

    for detection in result:
    
        text = detection[1]
        bbox = detection[0]
    
        x_min, y_min = map(int, bbox[0])
        x_max, y_max = map(int, bbox[2])
    
        cv2.rectangle(frame, (x_min, y_min), (x_max, y_max), (0, 255, 0), 2)
    
        cv2.putText(frame, text, (x_min, y_min - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
    
        print("Texto:", text)
        print("Coordenadas del rectángulo:", bbox)

reader = easyocr.Reader(['en'])

cap = cv2.VideoCapture(0) 

while True:

    ret, frame = cap.read()
    

    if not ret:
        print("Error al leer el fotograma de la cámara")
        break
    

    process_frame(frame, reader)
    

    cv2.imshow('Camera Feed', frame)
    

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()