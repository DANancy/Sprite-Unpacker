#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# import libs
import click
import sys
from PIL import Image
import os


@click.command()
@click.option("--in", "-i", "input_file", required=True, help="Path to image to be processed.",
              type=click.Path(exists=True, dir_okay=False, readable=True), )
@click.option("--out", "-o", "output_dir", required=True, help="Folder to images to export.",
              type=click.Path(dir_okay=True))
@click.option("--height", "-h", "height", type=click.INT,required=True, help="Output image height.", )
@click.option("--width", "-w", "width", type=click.INT, required=True, help="Output image width.", )
@click.option("--padding", '-p', "padding", type=click.INT, default=0, help="Input image padding (space between output images), default is 0.", )
@click.option("--margin", "-m", "margin", type=click.INT, default=0, help="Input image outer margin, default is 0.", )
@click.option("--name", '-n', "file_name_pattern", default="IMG(#).png", help="Output image file name pattern to be saved, default=IMG(#).png, # will be replaced by image index.")
def sprite_unpacker(input_file, output_dir, height, width, padding, margin, file_name_pattern):
    try:
        # Open image
        im = Image.open(input_file)
    except IOError:
        sys.exit("Unable to load image")

    try:
        # Create target Directory
        os.mkdir(output_dir)
        print("Directory ", output_dir, " Created ")
    except FileExistsError:
        print("Directory ", output_dir, " already exists")

    imgwidth, imgheight = im.size
    k = 1
    if '#' in file_name_pattern:
        file_name = file_name_pattern.replace('#', '{}')
    else:
        file_name = file_name_pattern + '-{}'
    for h in range(margin, imgheight - margin, height + padding):
        for w in range(margin, imgwidth - margin, width + padding):
            box = (w, h, w + width, h + height)
            a = im.crop(box)
            a.save(os.path.join(output_dir, file_name.format(k)))
            k += 1
    print("%s images have been created." % k)


if __name__ == "__main__":
    sprite_unpacker()
