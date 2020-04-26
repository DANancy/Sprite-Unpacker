from setuptools import setup

setup(name='sprite_unpacker',
      version='0.0.1',
      description='Sprite Unpacker for Animal Crossing',
      url='https://github.com/DANancy/Automate_Funny_Stuff/sprite_unpacker',
      author='DA Nancy',
      author_email='gnancy417@gmail.com',
      license='MIT',
      install_requires=["Click","Pillow"],
      packages=['sprite_unpacker'],
      entry_points={
          'console_scripts': [
              'sprite_unpacker = sprite_unpacker.__main__:sprite_unpacker'
          ]},
      zip_safe=False)