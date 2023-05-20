import cv2
import numpy as np

def _laplacian(img):
    return cv2.Laplacian(img, cv2.CV_64F)

def contrast_score(img):
    if len(img.shape) == 3:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    std_dev = np.std(img)
    return std_dev/100

def blur_score(img, lap = None):
    if lap is None:
        lap = _laplacian(img)
    laplacian_var = cv2.Laplacian(img, cv2.CV_64F).var()
    return laplacian_var/1000

def detect_white_noise(image, threshold=10, lap = None):
    if lap is None:
        laplacian = _laplacian(image)
    else:
        laplacian = lap
    abs_laplacian = np.abs(laplacian)
    
    noisy_pixels = np.sum(abs_laplacian < threshold)
    total_pixels = image.size
    noise_percentage = (noisy_pixels / total_pixels)
    return noise_percentage

def run(img):
    if isinstance(img, str):
        img = cv2.imread(img)
    if img is None:
        return 0,0,0
    lap = _laplacian(img)
    return contrast_score(img), blur_score(img, lap), detect_white_noise(img, lap = lap)