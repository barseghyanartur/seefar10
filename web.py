import os
import responder
from keras.models import load_model

from classify import classify_image, load_labels
from helpers import get_sample_images
from settings import LABEL_BIN, MODEL_NAME

api = responder.API(
    static_dir='examples'
)

LB = load_labels(LABEL_BIN)
MODEL = load_model(MODEL_NAME)


@api.route("/")
def index(req, resp):
    """Index view.

    :param req:
    :param resp:
    :return:
    """
    resp.content = api.template(
        'index.html'
    )


@api.route("/api/predict-sample-image/")
def predict_sample_image(req, resp):
    """REST view.

    :param req:
    :param resp:
    :return:
    """
    image_path = req.params.get('image', None)
    if image_path:
        res = classify_image(MODEL, LB, image_path)
        media = {
            'preds': [float(f) for f in res['preds']],
            'labels': [__l.as_text_with_percentage_only
                       for __l
                       in res['labels']],
        }
        resp.media = media


@api.route("/list-predict-sample-images/")
def list_predict_sample_images(req, resp):
    """Listing view of all sample images.

    :param req:
    :param resp:
    :return:
    """
    category = req.params.get('category', None)
    images = get_sample_images(category)
    predictions = []
    correct_predictions = 0
    total_predictions = len(images)
    for image_path in images:
        res = classify_image(MODEL, LB, image_path)
        if res['labels'][0].correct:
            correct_predictions += 1
        prediction = {
            'image_path': os.path.basename(image_path),
            'preds': [float(f) for f in res['preds']],
            'labels': res['labels'],
        }
        predictions.append(prediction)

    resp.content = api.template(
        'list_predict_sample_images.html',
        predictions=predictions,
        correct_predictions=correct_predictions,
        total_predictions=total_predictions,
        correct_percentage=(correct_predictions * 100.0 / total_predictions)
    )


if __name__ == '__main__':
    api.run()
