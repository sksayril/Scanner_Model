import cv2
from pyzbar import pyzbar


def decode_qr_code():
    # Open the webcam
    cap = cv2.VideoCapture(0)

    while True:
        # Read a frame from the webcam
        ret, frame = cap.read()

        # Convert the frame to grayscale
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Apply a blur filter to the frame
        blurred = cv2.GaussianBlur(gray, (5, 5), 0)

        # Perform QR code detection on multiple resized versions of the frame
        for scale in [1.0, 0.8, 0.6]:
            resized = cv2.resize(blurred, None, fx=scale, fy=scale)

            # Use pyzbar to detect and decode QR codes
            qr_codes = pyzbar.decode(resized)

            # Loop over the detected QR codes
            for qr_code in qr_codes:
                # Scale the bounding box coordinates back to the original frame size
                (x, y, w, h) = qr_code.rect
                x = int(x / scale)
                y = int(y / scale)
                w = int(w / scale)
                h = int(h / scale)

                # Draw a rectangle around the QR code
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

                # Decode the QR code
                data = qr_code.data.decode("utf-8")

                # Print the decoded data
                print("Decoded Data:", data)

        # Show the frame with detected QR codes
        cv2.imshow("QR Code Detection", frame)

        # Wait for the 'q' key to exit
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the webcam and close any open windows
    cap.release()
    cv2.destroyAllWindows()


# Call the function to decode QR codes from the webcam
decode_qr_code()
