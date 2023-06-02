import cv2
import pyqrcode


def decode_qr_code(frame):
    decoded_data = None
    detector = cv2.QRCodeDetector()
    data, bbox, _ = detector.detectAndDecodeMulti(frame)
    if bbox is not None and data is not None:
        for i in range(len(bbox)):
            x, y, w, h = bbox[i]
            cv2.rectangle(frame, (int(x), int(y)), (int(x + w),
                          int(y + h)), color=(255, 0, 0), thickness=2)
        decoded_data = data
    return frame, decoded_data


def main():
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Could not open webcam.")
        return

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Error reading frame from webcam.")
            break

        frame, decoded_data = decode_qr_code(frame)

        if decoded_data is not None:
            print("Decoded QR code:", decoded_data)

        cv2.imshow("Webcam", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
