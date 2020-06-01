.. _install:

==============================
Project install & setup
==============================

.. toctree::
   :maxdepth: 5

About
+++++++++++++++++++++++++++
Summary for setup & installs necessary for this project.

Part 1 - Flask, Sphinx, virtual env & Docker
+++++++++++++++++++++++++++++++++++++++++++++++

Sphinx
---------------------------------------

* Not strictly speaking necessary. Lots of docs in my Encyclopedia already. Used for project doc.

Flask
----------------

The webserver framework. Instally by creating a pycharm project. Pretty much automatic.

Docker
------------------

Followed `these instructions <https://docs.docker.com/engine/install/ubuntu/>`_ for Ubuntu install. Nothing special to report.

Generally speaking, to verify that the docker engine is installed, you can run:
`sudo docker run hello-world`, which will download a test image from docker & print stuff (including hello world) on the console.

Docker-compose
-----------------------

Installed on top of docker. See `this <https://docs.docker.com/compose/install/>`_ for details.

To check: `>> docker-compose --version` should return the version number

Build with docker-compose
-------------------------------------------

I had an issue running the command in the otherwise on the  `ball tutorial <https://medium.com/@riken.mehta/full-stack-tutorial-flask-react-docker-420da3543c91>`_. The command `docker-compose up --build` as proposed returned `Couldn't connect to Docker daemon at http+unix://var/run/docker.sock - is it running?`

So instead I followed the suggestion `from SO <https://stackoverflow.com/questions/29101043/cant-connect-to-docker-from-docker-compose>`_ and ran `sudo docker-compose up`.

The complete answer suggests adding docker to sudoer (more or less) since apparently the inability of the initial command to connect with the docker engine was a rights issue.

Then I ran it and it was fine! Perfect setup.


Part 2 - MongoDB & link with Flask
+++++++++++++++++++++++++++++++++++++++++++++++

MongoDB in a docker container
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This is not explained in the main tutorial, so I'm winging it here. I'm going to base it on `docker mongo image <https://hub.docker.com/_/mongo/>`_. So I'll need to adapt whatever reference (names, version, etc.) that may not be up to date in the tuto. The main lines are:

#. create a container for mongodb
    #. `sudo docker run --name climbticks-mongodb -d mongo:bionic` (with "bionic" being a tag that specify what image version we want

#. Connect to it from my project's (climbticks) container using docker-compose
    #. That didn't work. See `my SO question <https://stackoverflow.com/questions/62110783/connecting-to-docker-mongo-db-image>`_
    #. However, if I instead follow `these instructions<https://www.thepolyglotdeveloper.com/2019/01/getting-started-mongodb-docker-container-deployment/>`_ to setup the mongdodb image....

Seems like everything docker is a container.


Useful shorcuts
-------------------------------------
* :ref:`Homepage <index>`
* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

Auto-documentating some module
-------------------------------------

.. automodule:: main
   :members:
   :undoc-members:

