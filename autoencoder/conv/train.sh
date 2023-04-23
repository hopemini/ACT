## Traing AutoEncoder

# Image path
IMAGE_PATH='../../data_processing/'

echo 'conv autoencoder training..'
python train.py -d ${IMAGE_PATH} -t real -i 10

echo 'vector save..'
python vector_save.py -d ${IMAGE_PATH} -t real -i 10
