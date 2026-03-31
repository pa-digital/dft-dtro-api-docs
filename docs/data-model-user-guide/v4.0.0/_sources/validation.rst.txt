Validation
==========

Introduction
************
Britain is on the verge of a transport revolution and the Department has recently delivered the Future of Mobility, Urban Strategy as part of the Future of Mobility Grand Challenge. The Strategy priorities providing a regulatory framework that evolves with transport technology and advocates data sharing to improve operation of the transport system.
Traffic Regulation Orders (TROs) are the legal orders made under the Road Traffic Regulation Act 1984 which define the rules of the road network. They currently provide Traffic Regulation Authorities with powers to place permanent, temporary, or experimental restrictions on traffic for the purposes of safety or traffic management. Orders therefore provide a vital mechanism for enforcement on the road network. Digitization of these orders and providing them as standardized data would provide many benefits, including : 
    1. improving existing services (e.g., satNav routing);
    2. providing new services; 
    3. reducing enforcement and processing costs to highway authorities;
    4. reducing congestion;
    5. provision of the digital infrastructure for connected and automated vehicles.

The Automated Vehicles Act 2024 (section 93) provides the capability for the Secretary of State, through regulation, to require Traffic Regulation Authorities (TRAs) to provide information on a defined set of Traffic Regulation Measures, in a specified manner and form, to be provided in accordance with a specified model, standard or set of specifications. These will be the D-TRO Data Specification including the D-TRO Data Model, and are expected to be specified under secondary legislation.
This document specifies the semantic validation rules that submitted D-TRO records will be executed against before acceptance into the central storage system.

Terms and abbreviations
***********************
.. csv-table:: Terms and Abbreviations
    :file: table_data/terms_and_abbreviations.csv
    :header-rows: 1

Target audience
***************
The target audiences of this document include :
    * Traffic Regulation Authorities (TRAs) and any Digital Solution Providers that currently manage IT contracts within the authority.
    * The D-TRO Service Owner who will be responsible for long-term support, maintenance, and continual improvement of the Service.

Validation approach
*******************
Schema validation
-----------------
Schema validation ensures that submitted D-TROs align with the data model. Schema validation is executed at the time of submission. The current version of the schema can be found within the D-TRO Beta GitHub repository: https://github.com/department-for-transport-public/D-TRO.
The purpose of schema validation is to validate that a submitted payload conforms to all the rules outlined within the schema. This includes, but is not limited to, the following:
    * All submitted property names match the naming convention
    * Required properties are present
    * Additional submitted properties not outlined in the schema are forbidden
    * Data types are correct
    * Values are one of a fixed enumeration, where required
    * Numeric values are within a given range
    * Strings are of a minimum/maximum length
    * Arrays have a minimum/maximum number of items
    * Values match expected formats/patterns, e.g. date formats, datetime formats
    * Conditional logic, e.g. when a property has a certain value, this property must/must not exist

Schema validation is implemented with Newtonsoft (https://www.newtonsoft.com/json). Newtonsoft provides a useful online schema validation tool, providing the ability to interactively validate payloads against a schema. This can be found here: https://www.jsonschemavalidator.net/.

.. csv-table:: Schema Validation
    :file: table_data/schema_validation.csv
    :header-rows: 1
    :class: table-sm

Semantic validation
-------------------
Semantic validation ensures that submitted D-TROs contain quality and representational data beyond alignment with the schema. Semantic validation is executed at the time of submission.
Semantic validation is defined through two approaches. The first is to use JSON native validation where possible to validate ranges or types, through the use of schema validation (see above section). The second is to define more complex, dependent rules using code-side validation.

.. csv-table:: Code Side Validation
    :file: table_data/code_side_validation.csv
    :header-rows: 1
    :class: table-sm

Validation strategy for supporting multiple versions
----------------------------------------------------
When a D-TRO is submitted the request body must include a version of the data schema that the D-TRO is to be validated against. There is a relationship between the schema version number and a semantic rules version number document. As semantic validation rules are defined in table 8, they are assigned an `introduced in version` number showing which version they are applied to, therefore any D-TRO submitted with the corresponding schema version will be validated against that versions ruleset and any lower versions ruleset. If a D-TRO is submitted against one version of the schema and semantic rules, future updates can be made against the version of the schema it was originally submitted against. Updates can also be submitted against a higher version of the schema and rules and will be accepted against the higher version if validation is successful.

Assumptions, Constraints, Risks and Dependencies
************************************************
.. csv-table:: Assumptions, Constraints, Risks and Dependencies
    :file: table_data/assumptions_constraints_risks_and_dependencies.csv
    :header-rows: 1

