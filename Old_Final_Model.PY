import cv2
from pyzbar import pyzbar


def decode_qr_code():
    cap = cv2.VideoCapture(0)

    while True:

        ret, frame = cap.read()

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        qr_codes = pyzbar.decode(gray)

        for qr_code in qr_codes:

            (x, y, w, h) = qr_code.rect
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

            data = qr_code.data.decode("utf-8")

            print("Decoded Data:", data)

        cv2.imshow("QR Code Detection", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()


decode_qr_code()
