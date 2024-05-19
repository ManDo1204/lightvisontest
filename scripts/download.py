import matplotlib.pyplot as plt
import numpy as np
import os
import PIL
import tensorflow as tf

from tensorflow import keras
from tensorflow.keras import layers
from tensorflow.keras.models import Sequential
import pathlib

def download_image_from_tensorflow():
    print('\n** Example of the link: https://storage.googleapis.com/download.tensorflow.org/example_images/flower_photos.tgz\n')

    dataset_url = input('\nEnter the link to download image dataset: ')

    cur_dir = os.getcwd()
    save_path = cur_dir+'/downloads/'
    try:
        data_dir = tf.keras.utils.get_file(origin=dataset_url, 
                                        untar=True,
                                        cache_dir=save_path)

        data_dir = pathlib.Path(data_dir)
        print('\nDownload image dataset successfully!')
        print(f'-> Find the image dataset at {data_dir}')
    except Exception as e:
        print("\n<!> HTTP Error") 
        print(e)

    