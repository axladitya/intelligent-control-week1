import cv2
import numpy as np

# Inisialisasi kamera
cap = cv2.VideoCapture(0)

while True:
    _, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Rentang warna hijau dalam HSV
    lower_green = np.array([35, 100, 100])
    upper_green = np.array([85, 255, 255])

    # Masking untuk mendeteksi warna hijau
    mask = cv2.inRange(hsv, lower_green, upper_green)
    result = cv2.bitwise_and(frame, frame, mask=mask)

    # Deteksi kontur dari objek hijau
    contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    for contour in contours:
        if cv2.contourArea(contour) > 500:  # Filter ukuran minimum kontur
            x, y, w, h = cv2.boundingRect(contour)
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 3)  # Gambar bounding box
            cv2.putText(frame, "ijo", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)
    # Menampilkan hasil
    cv2.imshow("Frame", frame)
    cv2.imshow("Mask", mask)
    cv2.imshow("Result", result)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()