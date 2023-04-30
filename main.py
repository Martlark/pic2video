import cv2
import os
import click
import logging
from pathlib import Path

logging.basicConfig()


@click.command("turn images into movie")
@click.argument("image_folder")
@click.option("--file_name", default='video.avi', help="optional filename")
@click.option("--image_type", default='jpg', help="type of image, use extension. Default (jpg)" )
def main(image_folder, file_name=None, image_type='jpg'):
    font = cv2.FONT_HERSHEY_SIMPLEX
    video_name = file_name

    images = [i for i in Path(image_folder).rglob(f"*.{image_type}")]
    images = sorted(images, key=lambda i: os.path.getctime(i), reverse=True)

    if not images:
        logging.warning(f'no images in {image_folder}')
        return

    frame = cv2.imread(os.path.join(image_folder, images[0]))
    height, width, layers = frame.shape

    video = cv2.VideoWriter(video_name, 0, 1, (width,height))

    for image_path in images:
        img = cv2.imread(os.path.join(image_path))
        base_path = os.path.splitext(os.path.basename(image_path))[0]
        cv2.putText(img, str(base_path), (50, 100), font, 1, (255,255,255), 3)
        video.write(img)

    cv2.destroyAllWindows()
    video.release()

if __name__ == '__main__':
    main()