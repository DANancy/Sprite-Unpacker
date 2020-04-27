## Sprite-Unpacker
Sprite-Unpacker is a sample CLI tool for processing a big sprites image to be multiple small pieces. 

### Install Package
```
$ pip install sprite-unpacker
```
### Command Options
```
Options:
  -i, --in FILE          Path to image to be processed.  [required]
  -o, --out PATH         Folder to images to export.  [required]
  -h, --height INTEGER   Image height to be processed.  [required]
  -w, --weight INTEGER   Image width to be processed.  [required]
  -p, --padding INTEGER  Image padding to be processed.  [required]
  -m, --margin INTEGER   Image margin to be processed.  [required]
  -n, --name TEXT        Image file name pattern to be saved,
                         default=IMG(#).png, # will be replaced by image
                         index.

  --help                 Show this message and exit.
```
### Usage
#### Using it
```
sprite-unpacker -i example/images/128280.png -o example/processed_images/ -h 255 -w 255 -p 5 -m 5 
```
#### Input Image
![Image of Input Image](example/images/128280.png)

#### Output Image
<img src="example/processed_images/IMG(1).png" width="128" height="128">
<img src="example/processed_images/IMG(2).png" width="128" height="128">
<img src="example/processed_images/IMG(3).png" width="128" height="128">

### References
* [Create PyPi Package](https://medium.com/@joel.barmettler/how-to-upload-your-python-package-to-pypi-65edc5fe9c56)
* [Create Python CLT Tool](https://towardsdatascience.com/how-to-write-python-command-line-interfaces-like-a-pro-f782450caf0d)
