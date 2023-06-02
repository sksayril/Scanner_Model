import cv2
from pyzbar import pyzbar


def decode_qr_code():
    cap = cv2.VideoCapture(0)

    while True:

        ret, frame = cap.read()

        # Resize the frame to increase the smallest QR code size
        resized_frame = cv2.resize(frame, None, fx=2, fy=2)

        gray = cv2.cvtColor(resized_frame, cv2.COLOR_BGR2GRAY)
        qr_codes = pyzbar.decode(gray)

        for qr_code in qr_codes:
            (x, y, w, h) = qr_code.rect
            # Scale the coordinates back to the original frame size
            x, y, w, h = x // 2, y // 2, w // 2, h // 2
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

            data = qr_code.data.decode("utf-8")
            print("Decoded Data:", data)

        cv2.imshow("QR Code Detection", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()


decode_qr_code()
