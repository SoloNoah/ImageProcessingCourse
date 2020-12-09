#Authors
Emilia Zorin
Noah Solomon 

## Project title
KNN built to classify letters in Hebrew.

## Installation
Please check and install these libraries on your IDE if needed:
argparse, datetime, cv2, os, sklearn, skimage, numpy and pandas.


## How to use?
There are two files reported for this assignment.
preprocess.py - deals with preprocessing for the data.
knn_classifier.py - creates 2 models based on euclid and chi distances. Runs from k = 1 to 15 and finds the best for 
both methods. After that does predicition with both models and saves to 2 csv files the report and confusion matrix for both models.
As per demanded, the value of K for each model is written in the csv file under the report (line 33).


To run preprocess.py: 1) open terminal
		     2) python preprocess.py <PATH> 
			path = [TRAIN or TEST]
		     3) run one time each to finish both preprocessing for training and testing data.

To run  knn_classifier.py :  1) open terminal
		           2) python knn_classifier.py	
