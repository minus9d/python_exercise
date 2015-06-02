#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# コピー元：http://scikit-learn.org/stable/auto_examples/classification/plot_digits_classification.html#example-classification-plot-digits-classification-py

print(__doc__)

# Author: Gael Varoquaux <gael dot varoquaux at normalesup dot org>
# License: BSD 3 clause

# Standard scientific Python imports
import matplotlib.pyplot as plt

# Import datasets, classifiers and performance metrics
from sklearn import datasets, svm, metrics

# The digits dataset
digits = datasets.load_digits()

# The data that we are interested in is made of 8x8 images of digits, let's
# have a look at the first 3 images, stored in the `images` attribute of the
# dataset.  If we were working from image files, we could load them using
# pylab.imread.  Note that each image must have the same size. For these
# images, we know which digit they represent: it is given in the 'target' of
# the dataset.
# 手書き数字データセットの学習サンプルを4個描画
images_and_labels = list(zip(digits.images, digits.target))
print("dataset size = ", len(images_and_labels))
for index, (image, label) in enumerate(images_and_labels[:4]):
    plt.subplot(2, 4, index + 1) # 2x4マスの上半分に描画
    plt.axis('off')
    plt.imshow(image,
               cmap=plt.cm.gray_r,     # cmap = color map
               interpolation='nearest' 
    )
    plt.title('Training: %i' % label)
    
# To apply a classifier on this data, we need to flatten the image, to
# turn the data in a (samples, feature) matrix:
n_samples = len(digits.images)                # サンプル数

# もともとのサイズは 1794 x 8 x 8
print("digits.images shape = ", digits.images.shape)

data = digits.images.reshape((n_samples, -1)) # 8x8の部分を64次元の1次元ベクトルに変形

# 変換後のサイズは1794 x 64
# つまり、画像を64次元の1次元ベクトルとした
print("digits.images shape = ", data.shape)

# Create a classifier: a support vector classifier
# SVMを用いて多クラス分類(one-vs-one戦略を使用)
# RBFカーネル(Gaussianカーネル)のハイパーパラメータであるガンマの値を設定
# この値が大きいほど複雑な決定境界となる
classifier = svm.SVC(gamma=0.001)

# We learn the digits on the first half of the digits
# データの半分を学習に使う
classifier.fit(data[:n_samples / 2], digits.target[:n_samples / 2])

# 学習データの一つを見てみる
print("training data example: ")
print(data[0])

# Now predict the value of the digit on the second half:
# 残りの半分に対して、GTと、SVMの予測結果を比較する
expected = digits.target[n_samples / 2:]
predicted = classifier.predict(data[n_samples / 2:])


print("Classification report for classifier %s:\n%s\n"
      % (classifier,   # 分類に用いたSVNの詳細情報
         metrics.classification_report(expected, predicted)  # 各ラベルごとの分類結果
     )
)
print("Confusion matrix:\n%s" % metrics.confusion_matrix(expected, predicted))


# SVMによる分類例を4個描画
images_and_predictions = list(zip(digits.images[n_samples / 2:], predicted))
for index, (image, prediction) in enumerate(images_and_predictions[:4]):
    plt.subplot(2, 4, index + 5)
    plt.axis('off')
    plt.imshow(image, cmap=plt.cm.gray_r, interpolation='nearest')
    plt.title('Prediction: %i' % prediction)

plt.show()

