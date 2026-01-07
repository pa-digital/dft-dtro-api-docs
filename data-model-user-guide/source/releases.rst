Releases
========

This section provides details of releases that include changes to the data model.

7th January 2025
^^^^^^^^^^^^^^^^

Release ``b0d3378476931d6c9aeb360e93415a0f``

On 7th January 2026 we released ``v3.5.1`` of the Data Model. This minor release includes the following changes.

* added the following four ``vehicleType`` enumerations: ``heavyGoodsVehicle``, ``motorVehicle``, ``publicServiceVehicle`` and ``schoolBus``
* added ``miscFootpathClosure`` as a new ``regulationType``
* removed ``publicRightOfWayClosure`` from ``regulationType``, as it is considered a duplicate of ``miscPROWClosure``
* corrected inconsistency between naming of ``coastGuardVehicle`` in the Data Model and ``coastguardVehicle`` in the schema. ``coastGuardVehicle`` in the Data Model has been updated to ``coastguardVehicle`` to match the schema
* removed duplicate ``electric`` entry from ``fuelType`` enumeration
* added tighter validation for datetime formats. Optional seconds may be omitted, fractional seconds are no longer permitted
* added the following four ``vehicleCharacteristics`` extension mechanisms: ``payloadType``, ``fuelType``, ``vehicleEquipment`` and ``vehicleType``
* corrected inconsistency between the multiplicity of ``vehicleType`` in the Data Model (zero-to-many) and the schema (zero-to-one). Multiplcity of the Data Model has been updated to zero-to-many to match the schema

27th November 2025
^^^^^^^^^^^^^^^^^^

Release ``e22c38c8dcc0df8458dd5f0acb293a6e``

On 27th November 2025, we released a hotfix to address the following issues with the v3.5.0 schema.

* updated ``conditions.minItems`` from 2 to 1

.. code-block:: diff
  --- a/examples/Schemas/schemas-3.5.0.json
  +++ b/examples/Schemas/schemas-3.5.0.json
  @@ -427,7 +427,7 @@
          },
          "conditions": {
              "type": "array",
  -            "minItems": 2,
  +            "minItems": 1,
              "items": {
                  "type": "object",
                  "oneOf": [

18th November 2025
^^^^^^^^^^^^^^^^^^

Release ``cb5ec0412d2a2b535469b0862a057712``

On 18th November 2025, we released a minor bugfix to address the following issues with the v3.5.0 data model and schema.

* removed ``conditions`` as a property of ``regulation``, and from the ``regulation.oneOf`` constraint

.. code-block:: diff

    --- a/schemas-3.5.0.json
    +++ b/schemas-3.5.0.json
    @@ -2121,13 +2121,6 @@
         "$ref": "#/$defs/condition"
       }
     },
    -    "conditions": {
    -        "type": "array",
    -        "minItems": 1,
    -        "items": {
    -            "$ref": "#/$defs/condition"
    -        }
    -    },
       "generalRegulation": {
         "$ref": "#/$defs/generalRegulation"
       },

    @@ -2184,11 +2177,6 @@
       "condition"
       ]
    },
    -    {
    -        "required": [
    -            "conditions"
    -        ]
    -    },
    {
       "required": [
             "conditionSet"

* updated ``conditions.minItems`` from 1 to 2

.. code-block:: diff

    --- a/examples/Schemas/schemas-3.5.0.json
    +++ b/examples/Schemas/schemas-3.5.0.json
    @@ -427,7 +427,7 @@
       },
       "conditions": {
           "type": "array",
    -      "minItems": 1,
    +      "minItems": 2,
           "items": {
               "type": "object",
               "oneOf": [

* added ``publicRightOfWayClosure`` to ``regulationType`` enum

.. code-block:: diff

    --- a/schemas-3.5.0.json
    +++ b/schemas-3.5.0.json
    @@ -2274,7 +2262,8 @@
         "movementOrderProhibitedAccess",
         "nonOrderKerbsideBusStop",
         "nonOrderKerbsidePedestrianCrossing",
    -    "nonOrderMovementBoxJunction"
    +    "nonOrderMovementBoxJunction",
    +    "publicRightOfWayClosure"
       ],
       "type": "string"
     },

* changed spelling of  ``cubicCentimeters`` to ``cubicCentimetres`` in ``unitOfMeasureEnum``

.. code-block:: diff

    --- a/schemas-3.5.0.json
    +++ b/schemas-3.5.0.json
    @@ -2593,7 +2582,7 @@
     "unitOfMeasureEnum": {
         "description": "Defines the unit used for the measure.",
         "enum": [
    -        "cubicCentimeters",
    +        "cubicCentimetres",
             "year",
             "gkm",
             "kWh",

* added ``publicHolidayName`` object to ``specialDayType`` object

.. code-block:: diff

    --- a/schemas-3.5.0.json
    +++ b/schemas-3.5.0.json
    @@ -2948,6 +2937,10 @@
         },
         "specialDayType": {
             "$ref": "#/$defs/specialDayType"
    +    },
    +    "publicHolidayName": {
    +        "type": "string",
    +        "minLength": 1
         }
       }
     },
