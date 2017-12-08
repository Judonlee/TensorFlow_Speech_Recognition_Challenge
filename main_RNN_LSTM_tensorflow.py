import tensorflow as tf
import numpy as np

from tensorflow.python.ops import rnn, rnn_cell
from data_preprocessing import get_audio_dataset_features_labels

DATASET_PATH = 'G:/DL/tf_speech_recognition'


dataset_train_features, dataset_train_labels = get_audio_dataset_features_labels(DATASET_PATH, type='train')
# dataset_test_features, dataset_test_labels = get_audio_dataset_features_labels(DATASET_PATH, type='test')

print('dataset_train_features.shape:', dataset_train_features.shape, 'dataset_train_labels.shape:', dataset_train_labels.shape)


CLASSES = ['yes', 'no', 'up', 'down', 'left', 'right', 'on', 'off', 'stop', 'go', 'silence', 'unknown']
NUM_CLASSES = len(CLASSES)
CHUNK_SIZE = dataset_train_features.shape[2]	# 99 
NUM_CHUNKS = dataset_train_features.shape[1]	# 161
NUM_EPOCHS = 100
BATCH_SIZE = 128
RNN_SIZE = 128

# x = tf.placeholder(tf.float32)
# y = tf.placeholder(tf.float32)

# def recurrent_neural_network(x):
