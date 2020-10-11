import numpy as np
import cv2
import tensorflow.compat.v1 as tf
import os

tf.disable_v2_behavior()

CATEGORIES = ["SD", "HD"]
IMG_SIZE_R = 512
IMG_SIZE_C = 512
MODEL_NAME = "video-quality-cnn-final-1.model"
MODEL_PATH = os.path.join(os.getcwd(), "models", MODEL_NAME)

def play_and_test():
    video_name = input("Enter the name of the video to be tested: ")
    cap = cv2.VideoCapture(os.path.join(os.getcwd(), "test_data", video_name))

    tf.keras.backend.clear_session()
    model = tf.keras.models.load_model(MODEL_PATH)
    sd_count = 0.0
    hd_count = 0.0
    frame_count = 0.0
    while(cap.isOpened()):

        ret, frame = cap.read()

        if ret:
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            new_array = cv2.resize(gray, (IMG_SIZE_R, IMG_SIZE_C))
            new_array = new_array.reshape(-1, IMG_SIZE_R, IMG_SIZE_C, 1)

            prediction = model.predict([new_array])

            if CATEGORIES[int(prediction[0][0])]=='SD':
                sd_count += 1
            else:
                hd_count += 1
            frame_count += 1

            print(int(prediction))
            cv2.imshow('frame',gray)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                print("SD: {}%  HD: {}%".format(sd_count*100/frame_count, hd_count*100/frame_count))
                break

        else:
            print("SD: {}%  HD: {}%".format(sd_count*100/frame_count, hd_count*100/frame_count))
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    play_and_test()

