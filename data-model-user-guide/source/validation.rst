Validation
==========

Validation approach
*******************
Semantic validation ensures that submitted D-TROs contain quality and representational data beyond alignment with the schema. 
Semantic validation is executed at the time of submission. Semantic validation is defined through two approaches. The first is to use JSON native validation where possible to validate ranges or types, through the use of schema validation (see above section). The second is to define more complex, dependent rules using code-side validation.

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

Code side validation
--------------------
.. csv-table:: Code side Validation
    :file: table_data/code_side_validation.csv
    :header-rows: 1

Validation strategy for supporting multiple versions
----------------------------------------------------
When a D-TRO is submitted the request body must include a version of the data schema that the D-TRO is to be validated against. There is a relationship between the schema version number and a semantic rules version number document. As code-side validation rules are defined in table 8, they are assigned an `introduced in version` number showing which version they are applied to, therefore any D-TRO submitted with the corresponding schema version will be validated against that versions ruleset and any lower versions ruleset. If a D-TRO is submitted against one version of the schema and semantic rules, future updates can be made against the version of the schema it was originally submitted against. Updates can also be submitted against a higher version of the schema and rules and will be accepted against the higher version if validation is successful.

Assumptions, Constraints, Risks and Dependencies
************************************************
.. csv-table:: Assumptions, Constraints, Risks and Dependencies
    :file: table_data/assumptions_constraints_risks_and_dependencies.csv
    :header-rows: 1

