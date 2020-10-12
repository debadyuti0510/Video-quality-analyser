import numpy as np
import cv2
import os

'''
Iterates and reads all videos placed in source folder and extracts 
every 10th frame as an image to the target folder. Takes source 
folder and target folder paths as arguments.

'''
def vid_to_pic(source_folder, target_folder):
    i = 0
    for video in os.listdir(source_folder):
        cap = cv2.VideoCapture(os.path.join(source_folder, video))
        frame_no = 0
        
        while(cap.isOpened()):
            ret, frame = cap.read()
            
            if ret:
                gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                if frame_no % 10 == 0:
                    name = os.path.join(target_folder, "img" + str(i) + ".jpg")  #Incrementally generates names for extracted images
                    print('Extracting ' + name)
                    cv2.imwrite(name, gray)
                    i += 1 
                frame_no += 1
                
            else:
                break       #Breaks out if no more frames exist in the video

        cap.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    CATEGORIES = ["SD", "HD"]
    current_path = os.getcwd()
    hd_video_path = os.path.join(current_path, "raw_data", "HD")
    sd_video_path = os.path.join(current_path, "raw_data", "SD")
    hd_target_path = os.path.join(current_path, "processed_data", "HD")
    sd_target_path = os.path.join(current_path, "processed_data", "SD")
    vid_to_pic(sd_video_path, sd_target_path)
    vid_to_pic(hd_video_path, hd_target_path)

