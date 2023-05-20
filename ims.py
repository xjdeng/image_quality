from Easy_Image import imagesearch
try:
    from . import main
except ImportError:
    import main
default_columns = ['file','mtime','timestamp','contrast', 'blur', 'white noise']
import time

    
def calc_quality(f, fpath, mtime):
    try:
        quality = main.run(fpath)
    except IOError:
        quality = 0, 0, 0
    return [[fpath, mtime, time.time(), quality[0], quality[1], quality[2]]]

def run(start = "./", outfile = "image_quality.csv", batch = 10000):
    imagesearch.run_meta(calc_quality, default_columns, outfile, start, batch)