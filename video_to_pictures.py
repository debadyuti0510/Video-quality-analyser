import numpy as np
import cv2
import os

if __name__ == "__main__":
    path = input("Enter the path to the video: ")
    target_folder = input("Enter the name of the new folder: ")
    cap = cv2.VideoCapture(path)

    try:
        if not os.path.exists(target_folder):
            os.makedirs(target_folder)
    except OSError:
        print("Error creating the target folder.")

    frame_no = 0
    i = int(input("Enter the starting index: "))
    while(cap.isOpened()):
        ret, frame = cap.read()
        
        if ret:
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            if frame_no % 10 == 0:
                name = target_folder + '/img' + str(i) + '.jpg'
                print('Extracting ' + name)
                cv2.imwrite(name, gray)
                i += 1 
            frame_no += 1
            
        else:
            break

    cap.release()
    cv2.destroyAllWindows()