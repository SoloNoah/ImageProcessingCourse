from datetime import datetime
import cv2
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier, DistanceMetric
import os.path
from skimage import feature
import numpy as np
import pandas as pd


'''Authors: Emilia Zorin, Noah Solomon'''
def extract_hog(filename):
    print(f"[Extracting Hogs] start time: {datetime.now()}")
    hog_list, hog_label = [], []
    for digit in range(0, 27):
        label = digit
        dir = filename + '/' + str(label) + '/'
        for file in os.listdir(dir):
            img = cv2.imread(dir + file, 0)
            ch_hog = feature.hog(img, orientations=9, pixels_per_cell=(8, 8),
                                 cells_per_block=(2, 2), transform_sqrt=False, block_norm="L2")
            hog_list.append(ch_hog)
            hog_label.append(label)
    print(f"[Extracting Hogs] end time: {datetime.now()}")

    return hog_list, hog_label


def chi_square(h1, h2):
    return 0.5 * np.sum((h1 - h2) ** 2 / (h1 + h2 + 1e-6))


def create_best_model(type, pow=None):
    max_score = 0
    k_max = -1
    best_model = 0
    for i in range(1, 16):
        knn = KNeighborsClassifier(n_neighbors=i, metric=type, p=pow)
        knn.fit(X_train, y_train)
        model_score = knn.score(X_test, y_test)
        if (max_score < model_score):
            max_score = model_score
            k_max = i
            best_model = knn
    return best_model, k_max, max_score


def create_report(tags, preds):
    report = classification_report(tags, preds, output_dict=True)
    cf = confusion_matrix(tags, preds)
    cr = pd.DataFrame(report).transpose()
    return cf, cr


def write2csv(cmat, cr, type, k_max):
    file_name = type + "_" + "results.csv"
    cr.to_csv(file_name)
    with open(file_name, "a") as csvfile:
        csvfile.write(f"\n *** K {k_max} NEIGHBORS WITH EUCLIDEAN DISTANCE *** \n")
        csvfile.write(np.array2string(cmat, separator=', '))


print("--------TRAIN--------")
start = datetime.now()
train_filename = "Preprocessed_Train"
test_filename = "Preprocessed_Test"

hog_list, hog_label = extract_hog(train_filename)

print(f"[Splitting data for training] start time: {datetime.now()}")
train_val_ratio = .1
X_train, X_test, y_train, y_test = train_test_split(hog_list, hog_label, shuffle=True, test_size=train_val_ratio)
print(f"[Splitting data for training] end time: {datetime.now()}")

model_score_euclid, model_score_chi = [], []
'''euclid params'''
euclid_dist = DistanceMetric.get_metric('euclidean')
chi = chi_square
print(f"[Finding Euclid model] start time: {datetime.now()}")
best_model_euclid, k_max_euclid, max_euclid = create_best_model('euclidean')
print(f"[Found best euclidean model] end time: {datetime.now()}")

print(f"[Finding Chi model] start time: {datetime.now()}")

best_model_chi, k_max_chi, max_chi = create_best_model(chi)
print(f"[Found best Chi model] end time: {datetime.now()}")

print("-------------Prediction---------")
print(f"[Prediction] start time: {datetime.now()}")

pred_imgs, pred_tags = extract_hog(test_filename)

print(f"[Calculating predictions for models] start time: {datetime.now()}")

euclid_pred = best_model_euclid.predict(pred_imgs)
chi_pred = best_model_chi.predict(pred_imgs)
print(f"[Calculating predictions for models] end time: {datetime.now()}")

print(f"[Creating report] start time: {datetime.now()}")

euclid_cmat, euclidean_cr = create_report(pred_tags, euclid_pred)
chi_cmat, chi_cr = create_report(pred_tags, chi_pred)

write2csv(euclid_cmat, euclidean_cr, 'euclidean', k_max_euclid)
write2csv(chi_cmat, chi_cr, 'chi', k_max_chi)

print(f"[Creating report] end time: {datetime.now()}")
print(f"[Prediction] end time: {datetime.now()}")

print("The knn_classifier.py script ran {}".format(datetime.now() - start))