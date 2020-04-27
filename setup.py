from setuptools import setup

setup(name='sprite-unpacker',
      version='0.0.1',
      description='Sprite Unpacker for Animal Crossing',
      keywords = ['Images', 'Animal Crossing', 'Sprites'],
      url='https://github.com/DANancy/sprite-unpacker',
      download_url = 'https://github.com/DANancy/sprite-unpacker',
      author='DA Nancy',
      author_email='gnancy417@gmail.com',
      license='MIT',
      install_requires=[
          'Click',
          'Pillow',
      ],
      packages=['sprite_unpacker'],
      entry_points={
          'console_scripts': [
              'sprite-unpacker = sprite_unpacker.__main__:sprite_unpacker'
          ]},
      classifiers=[
          'Development Status :: 3 - Alpha',
          'Intended Audience :: Developers',
          'Topic :: Software Development :: Build Tools',
          'License :: OSI Approved :: MIT License',
          'Programming Language :: Python :: 3.7',
      ],
      )