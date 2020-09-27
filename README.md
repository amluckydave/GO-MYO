# <p align="center">GO MYO</p>

<p align="center">
      <a href="https://github.com/Holaplace/GO-MYO"><img src="https://img.shields.io/badge/status-updating-brightgreen.svg"></a>
      <a href="https://github.com/python/cpython"><img src="https://img.shields.io/badge/Python-3.6-FF1493.svg"></a>
      <a href="https://github.com/Holaplace/GO-MYO"><img src="https://img.shields.io/github/repo-size/Holaplace/GO-MYO"></a>
      <a href="https://github.com/Holaplace/GO-MYO/stargazers"><img src="https://img.shields.io/github/stars/Holaplace/GO-MYO.svg?logo=github"></a>
      <a href="https://github.com/Holaplace/GO-MYO/blob/master/LICENSE/"><img src="https://img.shields.io/badge/license-MIT-blue"></a>
      <a href="https://www.python.org/"><img src="https://upload.wikimedia.org/wikipedia/commons/c/c3/Python-logo-notext.svg" align="right" height="48" width="48" ></a>
      
</p>
<br />

## :building_construction: Introduction

GO MYO: Online Training & Predicting Hand Gestures.

Designed By @[Holaplace](https://github.com/Holaplace)
<br />

## :rocket: Progressing
This project aims to realize real-time hand gestures prediction, which means the GO MYO-embeded model can output target gestures before the completion of signal collection.

**DO NOT provide vital classification algorithm coding.** (- at present)


## :pushpin: Training
The first step for predicting is to train the individual classifier, you can follow the GUI notes to save your gesture raw EMG data in the default folder. 

Once all the preset 12 gestures are recorded and saved properly, you can press "Train" button to train the recognition model. And the trained classifier will be saved in the same folders.

Then, you can move to Prediction period. If you had trained your classifier, you can just skip training and initialize the prediction.

<img src="https://github.com/Holaplace/GO-MYO/blob/master/training_png.png" height="320">

## :pencil: Predicting
You should initialize the prediction model with the trained data (weights, default options etc.) titled with "CL.h5". Then, just connect the MYO armband, and do the predicting. To evaluate the real-time performance, you can check the LCD module (milli seconds) which stands for the duration between gesture begining and result generating.

<img src="https://github.com/Holaplace/GO-MYO/blob/master/wearing%20style.png" height="300"><img src="https://github.com/Holaplace/GO-MYO/blob/master/testing_png.png" height="300">


### Reference

% Python bindings for the Myo SDK: @NiklasRosenstein | myo-python

% You can check the media files about the real-time experiment (rawVideo.mp4, ba0.gif, etc). 

<img src="https://github.com/Holaplace/GO-MYO/blob/master/ba0.gif" height="320">
