=====================================
Create a data-set using Google images
=====================================
Create a data-set using Google images. For the moment, this guide is for Ubuntu
16.04 only, although it might inspire for extending it to other
systems/versions.

Pre-requisites
==============
Find out which version of ``ChromeDriver`` is the latest. Go to
`official ChromeDriver <http://chromedriver.chromium.org/downloads>`_ page
to find out. Let's assume, the latest version is 2.42 (which is true on the
moment of writing, as of 2018-09-29).

**Install `unzip` if you don't have it yet**

.. code-block:: sh

    sudo apt-get install unzip

**Install `xvfb` for running `Chrome` in a headless mode**

.. code-block:: sh

    sudo apt-get install xvfb

**Download and install latest `ChromeDriver`**

.. code-block:: sh

    wget -N http://chromedriver.storage.googleapis.com/2.42/chromedriver_linux64.zip
    unzip chromedriver_linux64.zip
    chmod +x chromedriver
    sudo mv -f chromedriver /usr/local/share/chromedriver
    sudo ln -s /usr/local/share/chromedriver /usr/local/bin/chromedriver
    sudo ln -s /usr/local/share/chromedriver /usr/bin/chromedriver

**Install `selenium` and `pyvirtualdisplay` libraries**

.. code-block:: sh

    pip install pyvirtualdisplay selenium

**Install `google-images-download`**

.. code-block:: sh

    pip install google-images-download

Download images
===============
Usage examples.

.. note::

    Note, that path to the ``ChromeDriver`` is given using `--chromedriver`
    directive.

Let's download 500 images for keyword ``pikachu`` and another 500 images for
keyword ``charmander``:

.. code-block:: sh

    googleimagesdownload -k airplane -l 500 -o datasets2/ -e --chromedriver /usr/bin/chromedriver
    googleimagesdownload -k bird -l 500 -o datasets/ -e --chromedriver /usr/bin/chromedriver

Produced directory structure:

.. code-block:: text

    ├── datasets/airplane/1. windowseat.jpg
    ├── datasets/airplane/2. 3l-image-747-400.jpg
    ├── datasets/airplane/3. img_4388-800x600.jpg

.. note::

    Note, that along with the image files saved locally, an image metadata in
    JSON format would be saved in the ``logs`` directory (relative to the
    current path).

Example metadata:

.. code-block:: javascript

    [
        {
            "image_description": "Which airplane seat you choose says a lot about you",
            "image_filename": "1. windowseat.jpg",
            "image_format": "jpg",
            "image_height": 1334,
            "image_host": "nypost.com",
            "image_link": "https://thenypost.files.wordpress.com/2014/12/windowseat.jpg?quality=90&strip=all",
            "image_source": "https://nypost.com/2014/12/10/which-airplane-seat-you-choose-says-a-lot-about-you/",
            "image_thumbnail_url": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS2d4IvhytFDxNvFU3T0_9kpAW8eYlgcY-OgjZVlhsG-xEfe14hnQ",
            "image_width": 2000
        },
        {
            "image_description": "The biggest passenger airplanes in the world",
            "image_filename": "2. 3l-image-747-400.jpg",
            "image_format": "jpg",
            "image_height": 400,
            "image_host": "aerospace-technology.com",
            "image_link": "https://www.aerospace-technology.com/wp-content/uploads/sites/15/2017/10/3l-Image-747-400.jpg",
            "image_source": "https://www.aerospace-technology.com/features/feature-biggest-passenger-airplanes-in-the-world/",
            "image_thumbnail_url": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS7lwTJ-Rf0cehKGfeUlW3FX2zpPuHM2i5DYtKINM1KZhfKWo8E",
            "image_width": 600
        },
        {
        "image_description": "Airplanes for rent in Florida - SkyEagle Aviation Academy",
        "image_filename": "3. img_4388-800x600.jpg",
        "image_format": "jpg",
        "image_height": 600,
        "image_host": "skyeagle.aero",
        "image_link": "http://skyeagle.aero/wp-content/uploads/2015/08/IMG_4388-800x600.jpg",
        "image_source": "http://skyeagle.aero/add_services/rent-a-plane/",
        "image_thumbnail_url": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRoIeOpWoBzD4X7cTXa7wM2i38KPzZMfE2zR8pt7au86gnjuUhlSw",
        "image_width": 800
        }
    ]

Resize images/normalise filenames
=================================
#TODO
