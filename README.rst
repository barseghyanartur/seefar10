========
SeeFar10
========
No, this is not a mistype.

Original CIFAR 10 categories have been retained:

- 0: airplane
- 1: automobile
- 2: bird
- 3: cat
- 4: deer
- 5: dog
- 6: frog
- 7: horse
- 8: ship
- 9: truck

Usage
=====
Train
-----

.. code-block:: sh

    python ./train.py --dataset datasets --model seefar10.model --labelbin seefar10.pickle

Classify
--------
Command line
~~~~~~~~~~~~
**Plain**

.. code-block:: sh

    python classify.py --model seefar10.model --labelbin seefar10.pickle --image examples/airplane01.jpg
    python classify.py --model seefar10.model --labelbin seefar10.pickle --image examples/automobile01.jpg
    python classify.py --model seefar10.model --labelbin seefar10.pickle --image examples/bird01.jpg
    python classify.py --model seefar10.model --labelbin seefar10.pickle --image examples/cat01.jpg
    python classify.py --model seefar10.model --labelbin seefar10.pickle --image examples/deer01.jpg
    python classify.py --model seefar10.model --labelbin seefar10.pickle --image examples/dog01.jpg
    python classify.py --model seefar10.model --labelbin seefar10.pickle --image examples/frog01.jpg
    python classify.py --model seefar10.model --labelbin seefar10.pickle --image examples/horse01.jpg

**Use OpenCV for image output**

.. code-block:: sh

    python classify.py --model seefar10.model --labelbin seefar10.pickle --use-opencv --image examples/airplane01.jpg
    python classify.py --model seefar10.model --labelbin seefar10.pickle --use-opencv --image examples/automobile01.jpg
    python classify.py --model seefar10.model --labelbin seefar10.pickle --use-opencv --image examples/bird01.jpg
    python classify.py --model seefar10.model --labelbin seefar10.pickle --use-opencv --image examples/cat01.jpg
    python classify.py --model seefar10.model --labelbin seefar10.pickle --use-opencv --image examples/deer01.jpg
    python classify.py --model seefar10.model --labelbin seefar10.pickle --use-opencv --image examples/dog01.jpg
    python classify.py --model seefar10.model --labelbin seefar10.pickle --use-opencv --image examples/frog01.jpg
    python classify.py --model seefar10.model --labelbin seefar10.pickle --use-opencv --image examples/horse01.jpg

Web
~~~
**Run the web server first**

.. code-block:: sh

    python web.py

**For all categories**

.. code-block:: text

    http://127.0.0.1:5042/list-predict-sample-images/

**For a single category**

.. code-block:: text

    http://127.0.0.1:5042/list-predict-sample-images/?category=airplane
    http://127.0.0.1:5042/list-predict-sample-images/?category=automobile
    http://127.0.0.1:5042/list-predict-sample-images/?category=bird
    http://127.0.0.1:5042/list-predict-sample-images/?category=cat
    http://127.0.0.1:5042/list-predict-sample-images/?category=deer
    http://127.0.0.1:5042/list-predict-sample-images/?category=dog
    http://127.0.0.1:5042/list-predict-sample-images/?category=frog
    http://127.0.0.1:5042/list-predict-sample-images/?category=horse
    http://127.0.0.1:5042/list-predict-sample-images/?category=ship
    http://127.0.0.1:5042/list-predict-sample-images/?category=truck

**For a single image**

.. code-block:: text

    http://127.0.0.1:5042/api/predict-sample-image/?image=examples/airplane01.jpg

Useful
======
**See GPU usage**

.. code-block:: sh

    nvidia-smi
