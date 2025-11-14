Releases
========

This section provides details of releases that include changes to the data model.

10th November 2025
^^^^^^^^^^^^^^^^^^

Release ``cb5ec0412d2a2b535469b0862a057712``

On 10th November 2025, we released a minor bugfix to address the following issues with the v3.5.0 data model and schema.

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
