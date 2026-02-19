Releases
========

This section provides details of releases that include changes to the data model.

31st March 2026
^^^^^^^^^^^^^^^

Release ``x``

On 31st March 2026 we released ``v4.0.0`` of the Data Model. This major release includes the following changes.

* restructured how ``condition``, ``conditions`` and ``conditionSet`` objects are represented in the Data Model. This is a breaking change and payloads will need to be updated to reflect these changes. For more information please see :ref:`condition-information`.
* added validation logic to ``externalReference.lastUpdateDate`` to ensure date is not in the future
* added validation logic to ``rateLine.durationStart`` and ``rateLine.durationEnd`` to ensure start date is before end date
* added ``minimum``, ``maximum`` and ``multipleOf`` constraints to ``heaviestAxleWeight``, ``grossVehicleWeight``, ``vehicleHeight``, ``vehicleLength`` and ``vehicleWidth`` vehicle characteristics
* enforced value of ``Europe/London`` for ``regulation.timeZone``

9th January 2026
^^^^^^^^^^^^^^^^

Release ``35d03c05aeeb43d38d3fa0285af6c14c``

On 9th January 2026 we released ``v3.5.1`` of the Data Model. This minor release includes the following changes.

* added the following four ``vehicleType`` enumerations: ``heavyGoodsVehicle``, ``motorVehicle``, ``publicServiceVehicle`` and ``schoolBus``
* added ``miscFootpathClosure`` as a new ``regulationType``
* removed ``publicRightOfWayClosure`` from ``regulationType``, as it is considered a duplicate of ``miscPROWClosure``
* corrected inconsistency between naming of ``coastGuardVehicle`` in the Data Model and ``coastguardVehicle`` in the schema. ``coastGuardVehicle`` in the Data Model has been updated to ``coastguardVehicle`` to match the schema
* removed duplicate ``electric`` entry from ``fuelType`` enumeration
* added tighter validation for datetime formats, where hours, minutes and seconds are all mandatory
* added the following four ``vehicleCharacteristics`` extension mechanisms: ``payloadType``, ``fuelType``, ``vehicleEquipment`` and ``vehicleType``
* corrected inconsistency between the multiplicity of ``vehicleType`` in the Data Model (zero-to-many) and the schema (zero-to-one). Multiplicity of the Data Model has been updated to zero-to-many to match the schema

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

27th October 2025
^^^^^^^^^^^^^^^^^

On 27th October we released ``v3.5.0`` of the Data Model. This minor release includes the following changes:

* Support to provide an information update to enable the submission of planned activation start and stop dates and times, after the submission of a Made Order D-TRO. For periodic maintenance style TROs (which create windows of opportunity to activate the TRO on sections of the network within a defined overall period, without specifying specific activation times at the time of being Made), the “information update” D-TRO submission enables records to be updated and give times and dates in the timeValidity sub-model represent when the TRO and its provisions are foreseen to be activated.
* Modelling to support Emissions-related regulations (ability to define CO:sub:`2` limits, engine capacity, battery capacity, etc).
* Modelling to support Electric Charging Conditions (e.g. when vehicle is connected to a charger; when charging).
* Addition of an “Other Condition” option with in Condition Sub-model to support definition of conditions and exemptions that are not covered by the range of conditions in the existing Data Specification.
* Extensions of supported WKT coding of spatial coordinates beyond Point, LineString and Polygon to also support MultiPoint, MultiLineString, MultiPolygon.
* Add ``dialARide`` to the vehicle usage type list.
* Change of the datatype of ``expectedDuration`` from integer to duration.
* Removal of support for the provision of Elementary Street Units (ESUs) from Data Specification.
* Addition of a National Speed Limit profile for speed limit regulations - that applies to all road types.

12th August 2025
^^^^^^^^^^^^^^^^

On 12th August 2025 we released ``v3.4.1`` of the Data Model. This minor release includes the following changes:

* Addition of a ``maxStayNoReturn`` attribute for all regulations (previously limited to Permits only)
* Extending the “Extension Enumeration” works across all of the following enumerated list:
  * ``permitType``
  * ``paylodType``
  * ``vehicleUsageType``
  * ``emissionsClassificationEuroType``
  * ``fuelType``
  * ``vehicleEquipmentType``
  * ``vehicleType``
* Bug fixes to the processing of Consultation records
* Additional enumerations. In response to stakeholder comments we continue to adjust various enumerated lists in the data specification:
  * Additional vehicle types:
    * ``poweredVehicleUsedByDisabledPeople``
    * ``emergencyAndIncidentSupportVehicle``
    * ``diplomaticVehicle``
  * Additional fuel types:
    * ``electric``
  * Additional regulation types:
    * ``kerbsideRedRouteBusStopClearway``
    * ``miscCycleHireParking``
    * ``miscCycleParking``

10th June 2025
^^^^^^^^^^^^^^

On 10th June 2025 we released ``v3.4.0`` of the Data Model. This minor release includes the following changes:

* In response to stakeholder comments, we have adopted a more widely adopted approach - the data model, data schema and service have been adapted to use camelCase for all object names and attribute names. Previously, object names were in PascalCase
* All /rules endpoints and the /schemas/{id} endpoint have been retired due to redundancy
* Additional objects and attributes added in response to expected functional needs resulting from the Secondary Legislation - see below for details
* In response to stakeholder comments, we have moved ``maximumAccessDuration`` and ``minimumTimetoNextEntry`` from ``permitSubjectToFee`` object to ``permitCondition`` object
* Use of the extension enumerations has been clarified/
* The ability to submit a consultation D-TRO record is now correctly supported
* In response to stakeholder comments, additional enumeration values to ``regulationType``, ``vehicleType`` and ``permitType``
* A few attribute datatypes have been changed
* Use of headers ``X-App-Id``, ``X-App-Id-Override`` and ``X-Correlation-Id`` has been clarified

29th November 2024
^^^^^^^^^^^^^^^^^^

On 29th November 2024 we released ``v3.3.0`` of the Data Model. This minor release includes the following changes:

* Clarify circular referencing between ``TimeValidity`` and ``Validity`` condition - the association between ``Regulation`` and ``TimeValidity`` has been removed. ``TimeValidity`` is a child of ``Condition``
* Adding two more regulation types (``kerbsideSingleRedLines`` and ``kerbsideDoubleRedLines``)
* Allowing multiple geometries
* TemporaryR``egulation providing a reference to the previous ``Provision`` which it overrides (partially or fully)
* Adding the capability to model diversion routes

17th October 2024
^^^^^^^^^^^^^^^^^

On 17th October 2024 we released ``v3.2.4`` of the Data Model. This bugfix release includes the following changes:

* Addition of ``miscSuspensionOfBusway`` to ``RegulationType``
* Notes to address future updates planned around ``TimeValidity`` and ``ChangeableTimePeriod``

10th September 2025
^^^^^^^^^^^^^^^^^^^

On 10th September 2025 we released ``v3.2.3`` of the Data Model. This bugfix release includes the following changes:

* Clarification of various data types (removal of ``duration`` data type, replaced by integer minutes)
* Clarification of the use of WKT formatting for the specification of geometric spatial coordinates

Earlier Releases
^^^^^^^^^^^^^^^^

``v3.2.2`` Data Model bugfix release includes the following changes:

* ``Source.traAffected`` attribute data type changed to an array of int (integers)
* ``ExternalReference`` class made optional. Relationship from ``PointGeometry`` [0..1] to ``ExternalReference`` [0..1]; Relationship from ``LinearGeometry`` [0..1] to ``ExternalReference`` [0..*]; Relationship from ``Polygon`` [0..1] to ``ExternalReference`` [0..*]; Three relationships from ``DirectedLinear`` [all 0..1] to ``ExternalReference`` all have lower bound multiplicity 0
* Classes ``LicenseCharacteristics`` and ``AgeOfDriver`` removed from ``Conditions`` package. Enum list ``licenseCharacteristicsType`` removed
* Two missing association added - association - ``ChangeableTimePeriodEnd`` [1] and ``ChangeableTimePeriodSource`` [0..1]; association - ``ChangeableTimePeriodEnd`` [1] and ``ChangeableTimePeriodEntry`` [0..*]
* Typo correction attribute name - ``legislationCrossReference``
* ``RegulationType`` enumeration entries with prefixed 'other' have been replaced by 'misc'. Enumeration entries to support TTRO regulations added ``miscRoadClosure``, ``miscLaneClosure``, ``miscContraflow``, ``miscFootwayClosure``, ``miscCycleLaneClosure``, ``miscTemporaryParkingRestriction``, ``miscSuspensionOfOneWay``, ``miscSuspensionOfParkingRestriction``, ``miscSuspensionOfWeightRestriction``, ``miscTemporarySpeedLimit``, ``miscRoadClosureCrossingPoint``, ``miscBaySuspension``, ``miscTemporaryParkingBay``, ``miscPROWClosure``
* Adjust association to - ``Provision`` [1] to ``Regulation`` [1]
* ``Provision.provisionIndex`` attribute has been removed
* ``regulationType`` attribute only retained for ``GeneralRegulation`` class; removed from ``Regulation`` class
* ``schemeIdentifier`` and ``permitIdentifier`` typos corrected in ``PermitCondition`` class
* ``Authority.name`` attribute ``ID`` property removed and typed as a string
* ``Consultation.pointOfContactEmail`` attribute renamed
* Add other enumeration entries to ``PayloadType``, ``VehicleEquipmentType`` and ``VehicleUsageType`` and ``VehicleType``, to support extension mechanism. ``VehicleType`` has been added to the ``TargetEnumeratedList`` Enum
* Add additional permissable Enum for ``nationalSpeedLimitMotorway`` in ``SpeedLimitProfileType``
* The Package name ``Validity`` and class name ``OverallPeriod`` have both been changed to ``TimeValidity``. The package ``ValidityEnumerations`` has been renamed ``TimeValidityEnumerations``
* Class name for all Enum classes written in UpperCamelCase
* ``RateLine.description`` attribute data type changed to string

``v3.2.0`` Data Model minor release includes the following changes:

* Inclusion of a Records Management provision
* Ability to provide Reporting of the real-world status of on road occupancy of TROs (specifically included for TTROs/TTMOs)
* Development of Location Referencing
* Proposed approach for Standardised Terms and Definitions
