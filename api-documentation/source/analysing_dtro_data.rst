Preparing D-TRO data for analysis
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Because of the nature of D-TROs, the current amount of data available in the D-TRO service is large. Moreover, the hierarchical structure of D-TRO data and the API-first nature of the service means that JSON is the sensible data format to use to represent D-TRO data. Because of this, common software tools that are designed for analysis of flat file data, like Microsoft Excel, are not particularly suited for anaylsis of these data formats, and tend to be too memory-intensive to load the complete set of data into memory at once. This section of the documentation will suggest some alternative methods for loading and analysing the data.

Structure of D-TRO data
=======================

The D-TRO service is an API-first service, and as such data published to and consumed from the service is in JSON format. Because of this, when working with D-TRO data, you will need to use an application that can parse and manipulate JSON data. Common examples are programming languages and databases with JSON format support.

The D-TRO service provides an endpoint for retrieving all live orders in the service. Data retrieved from this endpoint is in CSV format. Although the data is provided as a CSV file, it is important to note that this export is **not** a normalised, flat view of D-TRO data; it still contains nested JSON which will need to be appropriately parsed, but alongside metadata like ID, schema version and created and last updated dates. The full structure of the file is as follows:

* ``Id`` - unique identifier of the D-TRO
* ``SchemaVersion`` - version of the data model the D-TRO was submitted for
* ``Created`` - date and time the D-TRO was submitted to the service
* ``LastUpdated`` - date and time the D-TRO was last submitted to the service. If the D-TRO has not been updated after submission, ``Created`` and ``LastUpdated`` values will be equal
* ``Data`` - string representation of the JSON payload

This endpoint is designed as a quick way for users new to the service to download an initial export of all the data. Going forwards, you may prefer to use the API search functionality to retrieve new, updated or deleted D-TROs, rather than re-processing the whole file.

Once you have the data downloaded, you are free to use any software or application to analyse the data to your needs. We suggest a couple of suitable approaches here, but there are many others you may prefer. The DfT are deliberatley not prescriptive when recommended tools and workflows, as you are free to build your own integrations and processing with whatever tools you like.

Analysing D-TRO data with Python
================================

Python contains many mature, well-supported libraries for data analysis. Here we provide an example using the ``pandas`` library to read the D-TRO data export and parse the data payloads to JSON for downstream analysis:

.. code-block:: python

    import json
    import pandas as pd

    # Read export into a DataFrame
    df = pd.read_csv("dtros.csv")

    # Data column is read into pandas as a string, so convert to JSON (Python dictionary)
    df["Data"] = df["Data"].apply(json.loads)

    # Now the data can be operated on like any JSON document

    # To extract TRO names from the payload:
    def extract_tro_title(data: dict) -> str:
        return data["source"]["troName"]

    df["TroTitle"] = df["Data"].apply(extract_tro_name)

    # To extract creator of the TRO
    def extract_tro_creator(data: dict) -> int
        return int(data["source"]["traCreator"])

    df["TroCreator"] = df["Data"].apply(extract_tro_creator)


Analysing D-TRO data with a relational database
===============================================

Many databases support JSON natively as a data type, such as PostgreSQL. The instructions below illustrate how you can create a table to store the data, load the export in, and query the data. These instructions are given for PostgreSQL - other database engines may differ in syntax and functionality.

1. Create the table
*******************

.. code-block:: sql

    CREATE TABLE dtros (
        id UUID PRIMARY KEY,
        schema_version TEXT,
        created TIMESTAMPTZ NOT NULL,
        last_updated TIMESTAMPTZ NOT NULL,
        data JSONB NOT NULL
    );

2. Import data export into table
********************************

.. code-block:: sql

    \copy dtros (id, schema_version, created, last_updated, data)
    FROM '/tmp/dtros.csv'
    WITH (
        FORMAT csv,
        HEADER true,
        DELIMITER ',',
        QUOTE '"'
    );

3. Query data
*************

.. code-block:: sql

    SELECT data->'source'->>'troName' AS tro_name
    FROM dtros;

 
.. raw:: html

   <br><br>


Note: you may want to consider adding indexes to columns in your tables for performance purposes.

Analysis beyond search capabilities of the API
==============================================

The D-TRO service aims to provide common functionality for the search and retrieval of D-TROs relevant to user needs. However, all user needs are different, and it is likely that you may come across limitations in getting what you need through the search capabilities of the API. As a result the D-TRO API provides raw D-TRO data, allowing users to build their own analytical tools and pipelines. While we endeavour to provide useful search and retrieval functionality, D-TRO is a transactional service and not an analytical one, and so there is an expectation on users to perform their own downstream processing of data if required.

As an example, a common question that is asked is how to use the API to return D-TROs relating to speed limits. In its current form, speed limits are not exposed as a regulation type, and as such using the ``/search`` endpoint to filter D-TROs will not yield any results. Instead, speed limit D-TROs can be recognized by the presence of two objects linked to the D-TRO regulation object: ``speedLimitProfileBased`` and ``speedLimitValueBased``.

The folliowing examples show how downstream processing of D-TRO data can be used to retrieve D-TROs relating to speed limits.

Python
******

Here we use ``pandas`` to read the full D-TRO export, transform the data to JSON, and recursively search the payloads to match records that contain these speed limit objects.

.. code-block:: python

    import json
    import pandas as pd

    # Load data extract
    df = pd.read_csv("dtros.csv")

    # Convert data column to Python dictionary
    df["Data"] = df["Data"].apply(json.loads)

    # Function to return a boolean indicating the presence of the speed limit object(s)
    def contains_speed_limit(data):    
        if isinstance(obj, dict):
            # Check current level
            if "speedLimitProfileBased" in obj or "speedLimitValueBased" in obj:
                return True

            # Recurse into values
            return any(contains_speed_limit(v) for v in obj.values())

        elif isinstance(obj, list):
            return any(contains_speed_limit(item) for item in obj)

        return False

    # Apply function and set result to new column
    df["IsSpeedLimitDtro"] = df["Data"]/apply(is_speed_limit_dtro)

Note that in this example we have written the code ourselves to recurse through the JSON and find the objects. There are many JSON-parsing libraries available in the Python ecosystem for doing operations like this, including - but not limited to - ``jsonpath-ng``, ``jmespath`` and ``glom``. 

SQL
***

The following is the equivalent in SQL (PostgreSQL), using PostgreSQL's JSON parsing capabilities.

.. code-block:: sql

    SELECT *
    FROM dtros
    WHERE 
        data @? '$.source.provision[*].regulation.speedLimitValueBased'
        OR data @? '$.source.provision[*].regulation.speedLimitProfileBased';

In conclusion, there are many different tools and software packages you can use for analysing D-TRO data, and DfT are deliberately not presciptive about tools to use. The most appropriate tools are specific to individuals, workflows and use cases.