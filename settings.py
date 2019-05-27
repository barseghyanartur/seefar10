import os

IMAGE_WIDTH = 96
IMAGE_HEIGHT = 96

BASE_DIR = os.path.dirname(__file__)
SAMPLE_IMAGES_PATH = os.path.join(BASE_DIR, 'examples')

EPOCHS = 200
MODEL_NAME = 'seefar10_200_epochs_96px.model'
LABEL_BIN = 'seefar10_200_epochs_96px.pickle'
DATASET_DIR = 'datasets'

# EPOCHS = 10
# MODEL_NAME = 'seefar10_10_epochs_96px_cleaned.model'
# LABEL_BIN = 'seefar10_10_epochs_96px_cleaned.pickle'
# DATASET_DIR = 'var'
