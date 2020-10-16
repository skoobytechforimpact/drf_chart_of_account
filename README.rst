Django Rest Framework Chart of Account
======================================

Description
-----------

DRF Chart of Account holds the layer models and it's operations for a greater
Accounting Software. Layers are usually used in an accounting software to make
resources under a relationship. Generally 7 layers are used in a typical accounting
software but in drf_chart_of_account there are 5 layers. As for example an organization
has transport business. So we can say all the vehicles are in Vehicle Layer. Under that
water vehicles may be under Vehicle -> Water Vehicle Layer. A speedboat can be under
Vehicle -> Water Vehicle -> Speedboat layer. That's how all the layer's has relationship.

Requirements
------------

This package needs Django, Django Rest Framework and Requests to run.

Version
-------

Current stable version is 1.0

Compatibility
-------------

This package is Tox tested with Python version 3.6, 3.7 and 3.8 with Django
version 2.0, 2.1, 2.2, 3.0, 3.1 with Django Rest Framework version 3.12.1.
However, this package is compatible with
Python version > 3.0 and Django version > 2.0 but not compatible with
Python 2.7 and Django version < 2.0

Installation
------------

This package can be installed in two ways. One is via the pypi package manager
and other is directly from the Github.

For pypi installation please use the following command

.. code:: python

    pip install drf_chart_of_account

And for directly downloading from the Github repository use the following
commands

.. code:: python

    git clone https://github.com/skoobytechforimpact/drf_chart_of_account

After successful installation open Django's settings.py file and add
'drf_chart_of_account' and 'rest_framework', on your INSTALLED_APPS list.

.. code:: python

   INSTALLED_APPS = [
       ...
       'rest_framework',
       'django_user_interaction_log',
   ]

Include the event loggers URLconf in your project urls.py like this

.. code:: python

   path('accounts/', include('drf_chart_of_account.urls')),

Here you can put whatever you like on the path. Now run the app migration for
creating the database migrations

.. code:: python

   python manage.py makemigrations
   python manage.py migrate

Usage
-----------

This package is shipped with 5 Layer Models. LayerOneModel is the top parent
model of all and LayerTwoModel is the immediate child of LayerOneModel and
LayerThreeModel is the immediate child of LayerTwoModel and so on is
LayerFourModel to LayerThreeModel and LayerFiveModel to LayerFourModel.

Each model needs a name, parent_layer (for child models) and created_by data
to create an instance.

If any of the model instance has child data or has transaction (Transaction is
a feature of Journal application) then the instance can't be updated or
deleted.
However, this update validity check only happens if the update operation is
called from the appropriate Update API. Updating model instance directly without
the usage of the serializer class will not check the validity.
The deletion operation always check the validity. It doesn't depend on the
invoking method.

API Details:
''''''''''''

This package only accept json data as request and returns json in response.
Below are the list of api endpoints for this package.

Here **<layer_no>** belongs to the layer model no. So for different layers the
numbers are here:

+------------+------------+
| Layer Model | URL Text  |
+============+============+
| LayerOneModel | one     |
+------------+------------+
| LayerTwoModel | two     |
+------------+------------+
| LayerThreeModel | three |
+------------+------------+
| LayerFourModel | four   |
+------------+------------+
| LayerFiveModel | five   |
+------------+------------+

The model primary key is an integer value.

**Create API View**

.. code:: python

   endpoint: https://your-domain-name/accounts/charts/layer/<layer_number>/
   method: POST
   payload:
   {
      "name": "Dummy Layer One Data Postman",
      "is_active": true,
      "created_by": 1
   }

**List API View**

.. code:: python

   endpoint: https://your-domain-name/accounts/charts/layer/<layer_number>/
   method: GET

**Detail API View**

.. code:: python

   endpoint: https://your-domain-name/accounts/charts/layer/<pk>/
   method: GET

**Update API View**

.. code:: python

   endpoint: https://your-domain-name/accounts/charts/layer/<pk>/
   method: PUT

**Delete API View**

.. code:: python

   endpoint: https://your-domain-name/accounts/charts/layer/<pk>/
   method: DELETE

Package Creator
---------------

This package is created by Skooby Technology for Impact. The package is a
sub module of a larger Accounting Module
