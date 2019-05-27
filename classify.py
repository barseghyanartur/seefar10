# import the necessary packages
from keras.preprocessing.image import img_to_array
from keras.models import load_model
import numpy as np
import argparse
import imutils
import pickle
import pprint
import cv2
import os
import time

from settings import IMAGE_WIDTH, IMAGE_HEIGHT, MODEL_NAME, LABEL_BIN
from data_structures import Label


def load_labels(labelbin):
    # load the trained convolutional neural network and the label
    # binarizer
    return pickle.loads(open(labelbin, "rb").read())


def classify_image(model, lb, image_path, use_opencv=False):
    # if use_opencv:
    # load the image
    image = cv2.imread(image_path)
    output = image.copy()

    # pre-process the image for classification
    # image = cv2.resize(image, (96, 96))
    image = cv2.resize(image, (IMAGE_WIDTH, IMAGE_HEIGHT))
    image = image.astype("float") / 255.0
    # else:
    #     from helpers import resize_image
    #     sized_image = resize_image(image_path, IMAGE_WIDTH)
    #     image = sized_image['sized']
    #     output = sized_image['original']

    image = img_to_array(image)
    image = np.expand_dims(image, axis=0)

    # classify the input image
    print("[INFO] classifying image...")

    start = time.time()  # Measuring

    proba = model.predict(image)[0]
    idx = np.argmax(proba)
    label = lb.classes_[idx]

    end = time.time()  # End timer
    print("[INFO] classifying image took {}".format(end - start))  # Measuring

    # we'll mark our prediction as "correct" of the input image filename
    # contains the predicted label text (obviously this makes the
    # assumption that you have named your testing image files this way)
    filename = image_path[image_path.rfind(os.path.sep) + 1:]
    correct = filename.rfind(label) != -1

    # build the label and draw the label on the image
    label = Label(label, proba[idx], correct)

    if use_opencv:
        output = imutils.resize(output, width=400)
        cv2.putText(
            output,
            label.as_text,
            (10, 25),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.7,
            (0, 255, 0),
            2
        )

        # show the output image
        print("[INFO] {}".format(label))
        cv2.imshow("Output", output)
        cv2.waitKey(0)

    # print additional preds
    preds = [__p for __p in reversed(np.argsort(proba))]
    labels = []

    for idx_ in preds:
        label_ = lb.classes_[idx_]
        correct_ = filename.rfind(label_) != -1
        labels.append(
            Label(
                label=label_,
                probability=proba[idx_],
                correct=correct_
            )
        )

    return {
        'preds': preds,
        'labels': labels,
        'proba': proba,
        'label': label,
        'filename': filename,
        'output': output,
    }


if __name__ == "__main__":
    # construct the argument parse and parse the arguments
    ap = argparse.ArgumentParser()
    ap.add_argument(
        "-m",
        "--model",
        required=False,
        default=MODEL_NAME,
        dest='model',
        help="path to trained model model"
    )
    ap.add_argument(
        "-l",
        "--labelbin",
        default=LABEL_BIN,
        dest='labelbin',
        required=False,
        help="path to label binarizer"
    )
    ap.add_argument(
        "-i",
        "--image",
        required=True,
        dest='image',
        help="path to input image"
    )
    ap.add_argument(
        "-u",
        "--use-opencv",
        required=False,
        dest='use_opencv',
        action='store_true',
        help="Use OpenCV?"
    )
    args = vars(ap.parse_args())

    use_opencv = args["use_opencv"]
    image_path = args['image']

    print("[INFO] loading network...")
    start = time.time()  # Measuring

    model = load_model(args['model'])
    lb = load_labels(args['labelbin'])

    end = time.time()  # End timer

    print("[INFO] loading model took {}".format(end - start))  # Measuring

    res = classify_image(model, lb, image_path, use_opencv)
    preds = res['preds']
    proba = res['proba']
    filename = res['filename']
    labels = res['labels']

    pprint.pprint(labels)
