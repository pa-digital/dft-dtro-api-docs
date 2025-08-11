Creating Applications
=====================

Creating a publisher application in integration
***********************************************

.. notification::
    :heading: Note
    
    This functionality is only available for publisher accounts. Consumer accounts are unable to create publisher applications.

When creating a publisher application in integration, the only required information is application name.

.. image:: _static/images/create-publisher-application-integration.png
    :alt: Creating a publisher application in integration
    :width: 60%
    :align: center

If you application name violates the name requirements or constraints, you will receive a validation message communicating this. See the bototm of this page for information on what constitues a valid application name.

Upon successful creation of your application, you will be redirected to the application details screen, which displayes your created application, including:

* Application ID
* TRA code (this is a test code generated for use in the integration environment, and does not correspond to a real Traffic Regulation Authority)
* API key
* API secret

.. image:: _static/images/publisher-integration-app.png
    :alt: Publisher integration app details
    :width: 60%
    :align: center

.. note::
    Once created, publisher applications enter a pending state. Your application will be reviewed by a Central Service Operator, and you will receive an email once approved. You may receive an email requesting more information if required to support the application review process.

Creating a publisher application in production
**********************************************

Production publisher applications require the following information:

* Application name
* The Traffic Regulation Authority the D-TROs will will be submitted on behalf of
* Confirmation of whether you are a Digital Service Provider or self-publishing Traffic Regulation Authority
* Acceptance of the terms and conditions

.. image:: _static/images/create-publisher-application-production.png
    :alt: Creating a publisher application in production
    :width: 60%
    :align: center

Upon successful application creation, you will be atomatically redirected to the application details screen.

.. _creating-consumer-app-in-integration:

Creating consumer applications in integration
*********************************************

.. note::
    Both publisher and consumer accounts can create consumer applications.

When creating a consumer account in the integration environment, an application name is again required.

.. image:: _static/images/create-consumer-app-name.png
    :alt: Creating a consumer application (name) in integration
    :width: 60%
    :align: center

Additionally, Department for Transport also collect information on the proposed usage of consumer applications. This information is not shared, and is used solely for understanding the types of activities consumers are using the data for, and helping to guide future development of the service. These fields include, but are not limited to, the regions of the country and types of data you are interested in.

 .. image:: _static/images/create-consumer-app-details.png
    :alt: Creating a consumer application (application details) in integration
    :width: 60%
    :align: center

Creating consumer applications in production
********************************************

The process for creating a consumner account in production is identical to that of creating a consumer account in integration. Please see section :ref:`creating-consumer-app-in-integration` for more details.

.. note::
    Consumer applications do not require apporoval from a Central Service Operator, and so can be used with the D-TRO service immediately after they are created.

.. notification::
    :heading: Application name requirements

    For an application name to be valid, all of the following must be true:

    * The name must be unique across all applications
    * The name must start with an alphanumeric character
    * The name can contain only alphanumeric characters, the symbols ``_-.#$%``, and spaces

.. button-nav::
    :next-text: Requesting production access
    :next-url: requesting_production_access.html
    :back-url: navigation.html   