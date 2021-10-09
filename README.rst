Settle-Up-Adapter
=================

The aim of this project is to provide a rest-adapter for the firebase database used in the `Settle-Up-Application <https://settleup.io/>`_.

The main purpose is to evenly distribute a recurring payment across a specific group.

Getting started
---------------
The application is configured to run in a docker container. For example you can start the application by creating a .env file with the following entries (here the `sandbox <https://settle-up-sandbox-app.web.app/>`_ ist used):

.. code-block:: properties

    SETTLE_UP_FIREBASE_API_KEY=AIzaSyCfMEZut1bOgu9d1NHrJiZ7ruRdzfKEHbk
    SETTLE_UP_FIREBASE_PROJECT_NAME=settle-up-sandbox
    SETTLE_UP_USER={email-address of your settle-up-user}
    SETTLE_UP_PASSWORD={password for your settle-up-user}

Afterwards you can start the docker container by typing:

.. code-block:: console

  $ docker build -t=settle-up-sandbox-adapter .
  $ docker run -p 8080:80 --env-file=.env -d settle-up-sandbox-adapter

Now you can visit the swagger-ui on http://localhost:8080/docs or http://localhost:8080/redoc and add transactions.

For further requirements to use the prod environment see https://docs.google.com/document/d/18mxnyYSm39cbceA2FxFLiOfyyanaBY6ogG7oscgghxU/edit

