# Video-quality-analyser

## Requirements

The following requirements need to be satisfied in order to run the scripts.

### Directory structure

The folders shown below need to be created and the relevant data needs to be stored there.

- #### Raw data  
    The SD and HD data need to be stored in the following folders :-
    > raw_data/SD/  
    raw_data/HD/

- #### Processed data
    The processed data will be stored here and the following folders need to be created :-
    > processed_data/SD/  
    processed_data/HD/

- #### Models
    The models created while training will be stored in the folder below :-
    > models/

- #### Testing data
    Any video to test the model should be stored in the folder below :-
    > test_data/

###  Packages
The following packages need to be installed in the environment where this project is being done(Anaconda).

- #### OpenCV
        conda install -c conda-forge opencv (recommended)  
    or  
        
        pip install opencv-python

- #### Numpy
        pip install numpy

- #### Matplotlib
        pip install matplotlib
- #### Tensorflow
    
        conda install -c anaconda tensorflow (recommended with CPU)  
        conda install -c anaconda tensorflow-gpu (recommended with GPU)   
    or  
        
        pip install tensorflow

## Getting the data ready  

Place the video files in *raw_data/SD/* and *raw_data/HD/* and run the following script :-  

    python video_to_pictures.py  

The extracted pictures will be saved in *processed_data/SD/* and *processed_data/HD/* .  

Shape and dump the training data as a pickle file by running the following notebook :-  

    data_pre_process.ipynb

The picked files will be dumped in *processed_data/*.

## Training the model

The model can be trained by running the following notebook :-  

    train_analyser.ipynb

The model will be saved in *models/* .

## Testing the model

Place the video files to be tested in *test_data/* and then run 

    python test_video.py

Enter the name of the video file and the model will predict the perceived quality for the video file as it plays. 


