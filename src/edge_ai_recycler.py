import cv2
import numpy as np
import tensorflow.lite as tflite

interpreter = tflite.Interpreter(model_path="recycle_model.tflite")
interpreter.allocate_tensors()

input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()

labels = ["plastic", "paper", "metal", "glass"]

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    img = cv2.resize(frame, (150, 150))
    img = np.expand_dims(img / 255.0, axis=0).astype(np.float32)

    interpreter.set_tensor(input_details[0]['index'], img)
    interpreter.invoke()

    preds = interpreter.get_tensor(output_details[0]['index'])
    item = labels[np.argmax(preds)]
    confidence = np.max(preds) * 100

    cv2.putText(frame, f"{item} ({confidence:.1f}%)", (10, 30),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    cv2.imshow("Edge AI Recyclable Classifier", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
