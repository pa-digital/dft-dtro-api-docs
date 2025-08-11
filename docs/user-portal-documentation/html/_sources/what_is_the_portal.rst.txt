What is the D-TRO User Portal?
==============================

.. notification::
    :heading: Disclaimer
    
    This service is still in development, and is subject to change.

Introduction
************

The D-TRO Portal is a newly-developed web portal that allows users of the D-TRO service to create and manage their publisher and consumer applications that interface with the D-TRO service. The portal currently allows users to:

* Register for an account
* Create publisher and/or consumer applications
* Browse applications and credentials
* Submit data errors with published D-TROs

Accessing the portal
********************

The D-TRO service is split into two environments: the **integration** environment for testing your software's integration with the service, without impacting production data, and the **production** environment containing live D-TRO data. As a result, there are separate portals for the two environments.

* The integration environment portal is hosted at https://dtro-ui-integration.dft.gov.uk
* The production environment portal is hosted at https://dtro-ui.dft.gov.uk

.. note::
    Users wishing to publish to the D-TRO production service are required to first create a publisher application in the integration environment, and demonstrate they can successfully publish to the environment. After this, users can request access to the production environment; applications will be reviewed by a D-TRO Central Service Operator (CSO), and production access will be granted once successful publishing to the integration environment is evidenced.

.. button-nav::
    :next-text: Creating an account
    :next-url: creating_an_account.html
    :back-url: index.html