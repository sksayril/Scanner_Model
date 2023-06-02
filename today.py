import cv2
import numpy as np

# Create a VideoCapture object
cap = cv2.VideoCapture(0)

# Define the minimum and maximum size of a QR code
min_size = (100, 100)
max_size = (600, 600)

# Create a QRCode object
qrcode = cv2.QRCodeDetector()

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Convert the frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Find all the QR codes in the frame
    detections = qrcode.detectMultiScale(gray, min_size, max_size)

    # Loop over the detections
    for detection in detections:
        # Draw a rectangle around the QR code
        cv2.rectangle(frame, detection[0], detection[2], (0, 255, 0), 2)

        # Get the text from the QR code
        text, _, _ = qrcode.detectAndDecodeMulti(gray, detection)

        # If the text is not empty, display and print it
        if text:
            cv2.putText(frame, text, (detection[0][0], detection[0]
                        [1] + 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255))
            print("QR Code data:", text)

    # Display the frame
    cv2.imshow('QR Code Detection', frame)

    # Press `q` to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the capture object
cap.release()

# Close all windows
cv2.destroyAllWindows()
