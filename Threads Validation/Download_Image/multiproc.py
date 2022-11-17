import time
import multiprocessing
import requests

img_url = ['https://pixabay.com/get/g769338751d860ac2b46f2da9bf4234fe27145434082d3e91bdb1449966f692afff338fbc5dac82888270e22a2d66fcaf0562fc8456935859c9d89c7b7301fb43dffb5f437ef474d79b23727f90a54b31_1920.jpg','https://pixabay.com/get/gf521ee6aca3d814275281aedbc43a7f3f6df9a623431d42378cdf158ce73818eca65b6e7e9089c8e653e1b069c75e805ea4caefe013b3c9ed910ed6b84a68d233e241cabc16702c358386532f261c2d9_1920.jpg','https://pixabay.com/get/ge16f448ec62196d13b250fb503bde6391d8c449720231dc70bf3ad7de58c7948e525d7fcc3ca4c705d38bd37889648c714416d281520f40cd15e97765d272b645cc8e47516b7c7398cb12412e57ebac5_1920.jpg']

def download_image(img_url):
    img_bytes = requests.get(img_url).content
    img_name = img_url.split('/') [4]
    with open(img_name, 'wb') as img_file:
        img_file.write(img_bytes)
        print(f"{img_name} was downloaded")

if __name__ == '__main__':
    start = time.perf_counter()
    p1 = multiprocessing.Process(target=download_image, args = [img_url[0]])
    p2 = multiprocessing.Process(target=download_image, args = [img_url[1]])
    p3 = multiprocessing.Process(target=download_image, args = [img_url[2]])
    
    p1.start()
    p2.start()
    p3.start()

    p1.join()
    p2.join()
    p3.join()

    end = time.perf_counter()
    print(f"Tasks ended in {round(end - start, 2)} second(s)")