Quickstart
==========

This quickstart guide is designed to illustrate how to begin using the D-TRO API. It covers:

* Authenticating your application to receive an access token
* Making requests to publish D-TROs to the service
* Making requests to retrieve published D-TROs

.. note::
    This guide assumes you have already created a publisher/consumer application, and know your API key and secret. You can create applications and retrieve application credentials in the D-TRO User Portal.

A Note on Environments
**********************

The D-TRO service exposes two environments; **integration** and **production**.

* The integration environment is designed to allow users of the service to test their application's ability to publish to/consume from the service, without live data
* Once happy with the process for publishing/consuming with their application, live data can be published/consumed from the production environment
  
.. note::

    The integration environment includes upcoming features for testing and adapting applications to future API or data model changes. It may differ from the production environment. DfT is considering adding a pre-production environment that mirrors production, allowing users to test with confidence. In this setup, integration becomes a sandbox for new features. DfT will provide updates if this new environment is introduced.

The integration and production environments are two isolated services, and as such have different URLs.

* Integration: https://dtro-integration.dft.gov.uk/v1
* Production: https://dtro.dft.gov.uk/v1

Because of this, separate applications are required for communicating with each environment.

Authenticating Your Application
*******************************

The D-TRO service makes use of the **OAuth 2.0 client credentials flow** for authentication. In this flow, a **client ID** and **client secret** are exchanged with the service for an **access token**. This access token permits a user to interact with the service for a fixed period of time, until the token expires. Token expiry is configured to **30 minutes**. After this time a new token will need to be issued through the same flow.

Exchanging credentials for an access token is achieved by making a ``POST`` request to the OAuth 2.0 token generation endpoint, providing the client ID and secret as HTTP basic authentication credentials, and the client credentials grant type in the request body.

.. tabs::
    .. tab:: curl
        .. code-block:: bash
            
            curl -X POST https://dtro-integration.dft.gov.uk/v1/oauth-generator
                -u <client_id>:<client_secret>
                -d "grant_type=client_credentials"
    .. tab:: Python 
        .. code-block:: python
            
            response = requests.post(
                https://dtro-integration.dft.gov.uk/v1/oauth-generator,
                auth=HTTPBasicAuth(<client_id>, <client_secret>),
                data={"grant_type": "client_credentials"}
            )

    .. tab:: Response
        .. code-block:: json

            {
                "refresh_token_expires_in": "0",
                "api_product_list": "[int-publisher]",
                "api_product_list_json": [
                    "int-publisher"
                ],
                "organization_name": "dft-dtro-test",
                "developer.email": "dtro@dft.gov.uk",
                "token_type": "BearerToken",
                "issued_at": "1749815435563",
                "client_id": "<client_id>",
                "access_token": "<access_token>",
                "application_name": "00000000-0000-0000-0000-000000000000",
                "scope": "dsp",
                "expires_in": "1799",
                "refresh_count": "0",
                "status": "approved"
            }

The response payload contains ``access_token``, which is the token you will use when making requests to the API to authenticate.

.. danger::
   Do not share your access token with anybody. A valid access token allows your application to interface with the service. If somebody knows your access token they can use the D-TRO service on your behalf.

Publishing to the D-TRO Service
*******************************

There are three main ways to publish a D-TRO to the service. These are:

* Sending a JSON payload in the body of a ``POST`` request
* Sending a JSON file in a ``POST`` request
* Sending a gzip-compressed JSON file in a ``POST`` request
  
.. note::
    Only applications with the publisher scope can publish D-TROs to the service. If you try to publish a D-TRO using a consumer account, you will receive the following response:

    .. code-block:: json

        {
            "fault": {
                "faultstring": "Required scope(s): [cso, dsp]",
                "detail": {
                    "errorcode": "steps.oauth.v2.InsufficientScope"
                }
            }
        }

Submitting JSON in the body
***************************

A D-TRO can be published to the service by making a ``POST`` request to the ``/dtros/createFromBody`` endpoint, passing the access token as a header and the payload in the body.

.. tabs::
    .. tab:: curl
        .. code-block:: bash
            
            JSON=$(<file.json)

            curl -X POST https://dtro-integration.dft.gov.uk/v1/dtros/createFromBody
                -H "Authorization: Bearer <access_token>"
                -H "Content-Type: application/json"
                -d "$JSON"

    .. tab:: Python
        .. code-block:: python

            
            response = requests.post(
                'https://dtro-integration.dft.gov.uk/v1/dtros/createFromBody',
                headers={
                    'Authorization': 'Bearer <access_token>',
                    'Content-Type': 'application/json'
                },
                json=json.load(open('file.json'))
            )

    .. tab:: Response
        .. code-block:: json

            {
                "id": "00000000-0000-0000-0000-000000000000"
            }

The response payload contains a single field, ``id``, which is the ID of the created D-TRO record.

.. note::
    There is a 10MB request payload limit imposed by the API proxy. If the request body exceeds this limit, the submission will be rejected. Consider minifying your JSON payload, or uploading as a gzip-compressed file (see :ref:`gzip-upload`).

Submitting a JSON file
**********************

This endpoint is similar to the endpoint that handles publishing D-TROs using a JSON body, but instead allows a file to be uploaded. This is achieved by making a ``POST`` request to the ``/dtros/createFromFile`` endpoint, passing the access token as a header and attaching a JSON file.

.. tabs::
    .. tab:: curl
        .. code-block:: bash
            
            curl -X POST https://dtro-integration.dft.gov.uk/v1/dtros/createFromFile
                -H "Authorization: Bearer <access_token>"
                -F "file=@file.json"


    .. tab:: Python
        .. code-block:: python
            
            response = requests.post(
                'https://dtro-integration.dft.gov.uk/v1/dtros/createFromFile',
                headers={'Authorization': 'Bearer <access_token>'},
                files={'file': open('file.json', 'rb')}
            )

    .. tab:: Response
        .. code-block:: json

            {
                "id": "00000000-0000-0000-0000-000000000000"
            }

The response payload again contains a single field, ``id``, which is the ID of the created D-TRO record. The same file size limits are imposed here as when submitting JSON in the request body.

.. _gzip-upload:

Submitting a gzip-compressed file
*********************************

gzip is an excellent compression algorithm for JSON data, as it excels at compressing large, text-based, repetitive data, exactly like JSON. There are various tools available for compressing JSON with gzip. The following command uses the gzip CLI utility, installed on many Unix-like systems, to compress ``file.json`` and output it to a file named ``file.json.gz``.

.. code-block:: bash

    gzip -c file.json file.json.gz

The process for submitting a gzip-compressed JSON file is identical to that of submitting a JSON file.

.. tabs::
    .. tab:: curl
        .. code-block:: bash
            
            curl -X POST https://dtro-integration.dft.gov.uk/v1/dtros/createFromFile
                -H "Authorization: Bearer <access_token>"
                -F "file=@file.json.gz"

    .. tab:: Python
        .. code-block:: python
            
            response = requests.post(
                'https://dtro-integration.dft.gov.uk/v1/dtros/createFromFile',
                headers={'Authorization': 'Bearer <access_token>'},
                files={'file': open('file.json.gz', 'rb')}
            )

    .. tab:: Response
        .. code-block:: json

            {
                "id": "00000000-0000-0000-0000-000000000000"
            }

.. note::
    As gzip can compress very large raw files into very small gzip-compressed files, there is a hard limit on the server when decompressing gzip files. To prevent zip bomb attacks gzip files are processed in 8-byte chunks up to a maximum of 25MB. If the uncompressed file exceeds this 25MB limit, the API will return an error.

Consuming Data Within the D-TRO Service
***************************************

Both publisher and consumer applications have the necessary scopes to consume data from the D-TRO service. The API allows retrieval of individual D-TROs by their ID, searching for D-TROs that match some filter criteria, and retrieveing all D-TROS published to the service.

Retrieving a D-TRO by ID
************************

A single D-TRO can be retrieved by making a ``GET`` request to the ``/dtros/<id>`` endpoint, passing the D-TRO ID as a path parameter, and a valid access token as a header.

.. tabs::
    .. tab:: curl
        .. code-block:: bash

            curl https://dtro-integration.dft.gov.uk/v1/dtros/146375a5-7cc6-4092-b515-0c5c105820ff
                -H "Authorization: Bearer <access_token>"

    .. tab:: Python
        .. code-block:: python
            
            response = requests.get(
                'https://dtro-integration.dft.gov.uk/v1/dtros/146375a5-7cc6-4092-b515-0c5c105820ff',
                headers={'Authorization': 'Bearer <access_token>'}
            )

    .. tab:: Response
        .. code-block:: json

            {
                "id": "146375a5-7cc6-4092-b515-0c5c105820ff",
                "schemaVersion": "3.3.0",
                "data": {
                    "source": {
                    "section": "Schedule 1",
                    "troName": "DfT Example - Oct. 2024 - partial extract of THE DERBYSHIRE COUNTY COUNCIL (MARKET STREET AND TOWN END ROAD, DRAYCOTT) (RESTRICTION AND LIMITED WAITING) TRAFFIC REGULATION ORDER 2024 (DfT mockup, v2) API_TEST_RUN_2025-05-12T09:57:09.1817531+00:00",
                    "provision": [
                        {
                        "reference": "A3448229-1DFA-48CD-A785-376ACB9F7C56",
                        "regulation": [
                            {
                            "timeZone": "Europe/London",
                            "condition": [
                                {
                                "timeValidity": {
                                    "start": "2024-08-01T08:00:00",
                                    "validPeriod": [
                                    {
                                        "recurringTimePeriodOfDay": [
                                        {
                                            "endTimeOfPeriod": "18:00:00T00:00:00",
                                            "startTimeOfPeriod": "08:00:00T00:00:00"
                                        }
                                        ],
                                        "recurringDayWeekMonthPeriod": [
                                        {
                                            "applicableDay": [
                                            "friday",
                                            "monday",
                                            "saturday",
                                            "thursday",
                                            "tuesday",
                                            "wednesday"
                                            ]
                                        }
                                        ]
                                    }
                                    ]
                                }
                                }
                            ],
                            "isDynamic": false,
                            "generalRegulation": {
                                "regulationType": "kerbsideLimitedWaiting"
                            }
                            }
                        ],
                        "actionType": "new",
                        "regulatedPlace": [
                            {
                            "type": "regulationLocation",
                            "description": "West side, Market Street, Draycott",
                            "linearGeometry": {
                                "version": 1,
                                "direction": "bidirectional",
                                "linestring": "SRID=27700;LINESTRING(444284 333253, 444284 333253)",
                                "representation": "linear",
                                "lateralPosition": "onKerb",
                                "externalReference": [
                                {
                                    "lastUpdateDate": "2024-10-01T08:00:00",
                                    "uniqueStreetReferenceNumber": [
                                    {
                                        "usrn": 14000759
                                    }
                                    ]
                                }
                                ]
                            }
                            }
                        ],
                        "orderReportingPoint": "permanentNoticeOfMaking",
                        "provisionDescription": "Schedule 1: No Waiting Monday to Saturday, 8am to 6pm"
                        }
                    ],
                    "reference": "B2787FE2-AD74-432A-BB32-76FDB065F3E8",
                    "actionType": "new",
                    "traCreator": 99999,
                    "traAffected": [99999],
                    "currentTraOwner": 99999
                    }
                }
            }

.. note::
    Retrieving a D-TRO by ID relies on knowing the ID of the D-TRO.

Retrieving all D-TROs
*********************

The D-TRO service provides the capability to retrieve all published D-TROs. Due to the large volumes of data contained within D-TROs, retriveing all D-TRO records is not achieved via the API. Instead, the API is used to request a signed URL, which enables users to download a ``.csv`` file containing all D-TRO data.

This URL can be requested by making a ``GET`` request to the ``/dtros/all`` endpoint, passing a valid access token as a header.

.. tabs::
    .. tab:: curl
        .. code-block:: bash

            curl https://dtro-integration.dft.gov.uk/v1/dtros/all
                -H "Authorization: Bearer <access_token>"

    .. tab:: Python
        .. code-block:: python
            
            response = requests.get(
                'https://dtro-integration.dft.gov.uk/v1/dtros/all',
                headers={'Authorization': 'Bearer <access_token>'}
            )

    .. tab:: Response
        .. code-block:: json

            "https://storage.googleapis.com/dtro-records/dtros_20250805_104621.csv?X-Goog-Algorithm=GOOG4-RSA-SHA256&X-Goog-Credential=sa-execution%40dft-dtro-dev-01.iam.gserviceaccount.com%2F20250805%2Fauto%2Fstorage%2Fgoog4_request&X-Goog-Date=20250805T104710Z&X-Goog-Expires=3600&X-Goog-SignedHeaders=host&X-Goog-Signature=ac6f85fe1df2f36ffdc969e96147e0bd2c542c4088fe3c5f228d233986d536286afdd0e6983950cade741eae12eaabb85cb362cd813059fa1d5be84c236576db9fe1b01acdb2810774374e379113ad9e47be200de89c9ec3df79e6283f1ecd029fd48fe8e18cf785aa6ad84dd88e299563207547efe49b820a701d0eec3bfc4d5b5726c68393dae7acb122eefee928b8bdf6caebd3c94c39db8c597a29474c5be81f04ea4b9a4a6eb901be5043772fa3cd29992c9759755faeb375d0034605f6b5a38bd88e103c8b19b8911f28d68c225f4b9d3e5f2369c7d226d7ed59d44576ca8777bdcaf181d5390b8e70d8b343535fbb1a955ddc1e167f6680676a088075"

.. note::
    The signed URL is valid for 60 minutes only, and once expired can no longer be used to retrieve the dataset.

.. button-nav::
   :next-text: API documentation
   :next-url: api_documentation.html
   :back-url: index.html