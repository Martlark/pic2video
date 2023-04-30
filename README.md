# Pic2Video

A simple Python program using cv2 to convert still images files of a single format
into a video file

All files in any child folder will be selected, then they will be sorted into time order
and converted to a movie.

NOTE: Images should be the same size and format.

## installation

### Make venv

    $ python -m venv venv

    $ pip -r requirements.txt

## Usage

    python main.py "folder" [options...]

Use --help for options

## Options

* --file_name : output video file, default='video.avi'
* --image_type : optional image type, default='jpg'

