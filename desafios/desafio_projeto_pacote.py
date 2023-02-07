import numpy as np
import matplotlib.pyplot as plt
from skimage.transform import resize
from skimage.io import imread, imsave
from skimage.color import rgb2gray
from skimage.exposure import match_histograms
from skimage.metrics import structural_similarity
from teste1_image_processing.util import io, plot
from teste1_image_processing.processing import combination, transformation

imagem_1 = io.read_image("C:/temp/imagens/natureza.jpg")
imagem_2 = io.read_image("C:/temp/imagens/textura.jpg")

imagem_resultado = combination.transfer_histogram(imagem_1, imagem_2)
plot.plot_result(imagem_1, imagem_2, imagem_resultado)