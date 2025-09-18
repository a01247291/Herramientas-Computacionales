import cv2

cam_port = 0
cam = cv2.VideoCapture(cam_port)

while True:

    result, frame = cam.read()

    if result: 

        # Convertimos cada cuadro a escala de grises
        gris = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Deteccion de bordes Canny en cada cuadro 
        edges = cv2.Canny(gris, 100, 200)

        cv2.imshow("Presiona 'q' para salir", edges)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    else:
        print("No image detected")
        break

cam.release()
cv2.destroyAllWindows()