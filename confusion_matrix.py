import numpy as np 
import itertools

import matplotlib.pyplot as plt

from sklearn import svm, datasets
from sklearn.metrics import confusion_matrix

#f = open('test-data-new.txt','rb')
f = open('labels-new.txt','rb')
lines = f.readlines()
f.close()

y_original = []
for line in lines:
	label = int(line.split(' ')[1].replace('\n',''))
	y_original.append(label)
print len(y_original)
y_original = np.array(y_original)

#f = open('classified_test_new.txt','rb')
f = open('tracklet_wise_prediction_new.txt','rb')
lines = f.readlines()
f.close()

y_pred = []
for line in lines:
	label = int(line.split(' ')[1].replace('\n',''))
	y_pred.append(label)
print len(y_pred)
y_pred = np.array(y_pred)

def plot_confusion_matrix(cm, classes,normalize=False,title='Confusion matrix',cmap=plt.cm.Blues):
    """
    This function prints and plots the confusion matrix.
    Normalization can be applied by setting `normalize=True`.
    """
    plt.imshow(cm, interpolation='nearest', cmap=cmap)
    plt.title(title)
    plt.colorbar()
    tick_marks = np.arange(len(classes))
    plt.xticks(tick_marks, classes, rotation=45)
    plt.yticks(tick_marks, classes)

    if normalize:
        cm = cm.astype('float') / cm.sum(axis=1)[:, np.newaxis]

        print("Normalized confusion matrix")
    else:
        print('Confusion matrix, without normalization')

    print(cm)

    thresh = cm.max() / 2.
    for i, j in itertools.product(range(cm.shape[0]), range(cm.shape[1])):
        plt.text(j, i, cm[i, j],
                 horizontalalignment="center",
                 color="white" if cm[i, j] > thresh else "black")

    plt.tight_layout()
    plt.ylabel('True label')
    plt.xlabel('Predicted label')

class_names = ['Stand','Service','Reception','Setting','Attack','Block','Defence-Move']
# Compute confusion matrix
cnf_matrix = confusion_matrix(y_original, y_pred)

sum = 0
for i in range(7):
	sum+=cnf_matrix[i][i]
print sum

np.set_printoptions(precision=2)

# Plot non-normalized confusion matrix
plt.figure()
plot_confusion_matrix(cnf_matrix, classes=class_names,
                      title='Confusion matrix, without normalization')

# Plot normalized confusion matrix
plt.figure()
plot_confusion_matrix(cnf_matrix, classes=class_names, normalize=True,
                      title='Normalized confusion matrix')

plt.show()