Change Log
==========

.. note::
    The following critical changes have been made between release ``v3.1.1`` and ``v3.2.0``:

1.	Inclusion of a Records Management provision
2.	Ability to provide Reporting of the real-world status of on road occupancy of TROs (specifically included for TTROs/TTMOs)
3.	Development of Location Referencing
4.	Proposed approach for Standardised Terms and Definitions

.. note::
    The following critical changes have been made between release ``v3.2.0`` and ``v3.2.2``:

1.	``Source.traAffected`` attribute data type changed to an array of int (integers)
2.	``ExternalReference`` class made optional. Relationship from ``PointGeometry`` [0..1] to ``ExternalReference`` [0..1]; Relationship from ``LinearGeometry`` [0..1] to ``ExternalReference`` [0..*]; Relationship from ``Polygon`` [0..1] to ``ExternalReference`` [0..*]; Three relationships from ``DirectedLinear`` [all 0..1] to ``ExternalReference`` all have lower bound multiplicity 0
3.	Classes ``LicenseCharacteristics`` and ``AgeOfDriver`` removed from ``Conditions`` package. Enum list ``licenseCharacteristicsType`` removed
4.	Two missing association added - association - ``ChangeableTimePeriodEnd`` [1] and ``ChangeableTimePeriodSource`` [0..1]; association - ``ChangeableTimePeriodEnd`` [1] and ``ChangeableTimePeriodEntry`` [0..*]
5.	Typo correction attribute name - ``legislationCrossReference``
6.	``RegulationType`` enumeration entries with prefixed 'other' have been replaced by 'misc'. Enumeration entries to support TTRO regulations added ``miscRoadClosure``, ``miscLaneClosure``, ``miscContraflow``, ``miscFootwayClosure``, ``miscCycleLaneClosure``, ``miscTemporaryParkingRestriction``, ``miscSuspensionOfOneWay``, ``miscSuspensionOfParkingRestriction``, ``miscSuspensionOfWeightRestriction``, ``miscTemporarySpeedLimit``, ``miscRoadClosureCrossingPoint``, ``miscBaySuspension``, ``miscTemporaryParkingBay``, ``miscPROWClosure``
7.	Adjust association to - Provision [1] to Regulation [1]
8.	``Provision.provisionIndex`` attribute has been removed
9.	``regulationType`` attribute only retained for ``GeneralRegulation`` class; removed from ``Regulation`` class
10.	``schemeIdentifier`` and ``permitIdentifier`` typos corrected in ``PermitCondition`` class
11.	``Authority.name`` attribute ``ID`` property removed and typed as a string
12.	``Consultation.pointOfContactEmail`` attribute renamed
13.	Add ``other`` enumeration entries to ``PayloadType``, ``VehicleEquipmentType`` and ``VehicleUsageType`` and ``VehicleType``, to support extension mechanism. ``VehicleType`` has been added to the ``TargetEnumeratedList`` Enum
14.	Add additional permissable Enum for ``nationalSpeedLimitMotorway`` in ``SpeedLimitProfileType``
15.	The Package name ``Validity`` and class name ``OverallPeriod`` have both been changed to ``TimeValidity``. The package ``ValidityEnumerations`` has been renamed ``TimeValidityEnumerations``
16.	Class name for all ENUM classes written in UpperCamelCase
17.	``RateLine.description`` attribute data type changed to string

.. note::
    The following critical changes have been made between release ``v3.2.2`` and ``v3.2.3``:

1.	Clarification of various data types (see 3.9. Removal of ``duration`` data type, replaced by integer minutes)
2.	Clarification of the use of WKT formatting for the specification of geometric spatial coordinates

.. note::
    The following changes have been made between release ``v3.2.3`` and ``v3.2.4``:

1.	Addition of ``miscSuspensionOfBusway`` to ``RegulationType``
2.	Notes to address future updates planned around ``TimeValidity`` and ``ChangeableTimePeriod``

.. note::
    The following changes have been made between release ``v3.2.4`` and ``v3.3.0``:

1.	Clarify circular referencing between ``TimeValidity`` and ``Validity`` Condition - the association between ``Regulation`` and ``TimeValidity`` has been removed. ``TimeValidity`` is a child of ``Condition``
2.	Adding two more regulation types (``kerbsideSingleRedLines`` and ``kerbsideDoubleRedLines``)
3.	Allowing multiple geometries
4.	``TemporaryRegulation`` providing a reference to the previous ``Provision`` which it overrides (partially or fully)
5.	Adding the capability to model diversion routes

.. note::
    A summary of the changes have been made between release ``v3.3.0`` and ``v3.4.0``:

1.	In response to stakeholder comments, we have adopted a more widely adopted approach - the data model, data schema and service have been adapted to use camelCase for all object names and attribute names. Previously, object names were in PascalCase
2.	All ``/rules`` endpoints and the ``/schemas/{id}`` endpoint have been retired due to redundancy
3.	Additional objects and attributes added in response to expected functional needs resulting from the Secondary Legislation - see below for details
4.	In response to stakeholder comments, we have moved ``maximumAccessDuration`` and ``minimumTimetoNextEntry`` from ``permitSubjectToFee`` object to ``permitCondition`` object
5.	Use of the extension enumerations has been clarified
6.	The ability to submit a consultation D-TRO record is now correctly supported
7.	In response to stakeholder comments, additional enumeration values to ``regulationType``, ``vehicleType`` and ``permitType``
8.	A few attribute datatypes have been changed
9.	Use of headers ``X-App-Id``, ``X-App-Id-Override`` and ``X-Correlation-Id`` has been clarified

.. note::
    A summary of the changes have been made between release ``3.4.0`` and ``3.4.1``:

1.  Addition of a ``maxStayNoReturn`` attribute for all regulations (previously limited to Permits only)
2.  Extending the “Extension Enumeration” works across all of the following enumerated list:
  * ``permitType``
  * ``paylodType``
  * ``vehicleUsageType``
  * ``emissionsClassificationEuroType``
  * ``fuelType``
  * ``vehicleEquipmentType``
  * ``vehicleType``
3.  Bug fixes to the processing of Consultation records
4.  Additional enumerations. In response to stakeholder comments we continue to adjust various enumerated lists in the data specification:
  *  Additional vehicle types:
    *  ``poweredVehicleUsedByDisabledPeople``
    *  ``emergencyAndIncidentSupportVehicle``
    *  ``diplomaticVehicle``
  *  Additional fuel types:
    *  ``electric``
  *  Additional regulation types:
    *  ``kerbsideRedRouteBusStopClearway``
    *  ``miscCycleHireParking``
    *  ``miscCycleParking``

.. note::
    A summary of the changes have been made between release ``3.4.1`` and ``3.5.0``:

1.  Support to provide an information update to enable the submission of planned activation start and stop dates and times, after the submission of a Made Order D-TRO. For periodic maintenance style TROs (which create windows of opportunity to activate the TRO on sections of the network within a defined overall period, without specifying specific activation times at the time of being Made), the “information update” D-TRO submission enables records to be updated and give times and dates in the timeValidity sub-model represent when the TRO and its provisions are foreseen to be activated.
2.	Modelling to support Emissions-related regulations (ability to define CO2 limits, engine capacity, battery capacity, etc).
3.	Modelling to support Electric Charging Conditions (e.g. when vehicle is connected to a charger; when charging).
4.	Addition of an “Other Condition” option with in Condition Sub-model to support definition of conditions and exemptions that are not covered by the range of conditions in the existing Data Specification.
5.	Extensions of supported WKT coding of spatial coordinates beyond Point, LineString and Polygon to also support MultiPoint, MultiLineString, MultiPolygon.
6.	Add ``dialARide`` to the vehicle usage type list.
7.	Change of the datatype of ``expectedDuration`` from ``integer`` to ``duration``.
8.	Removal of support for the provision of Elementary Street Units (ESUs) from Data Specification.
9.	Addition of a National Speed Limit profile for speed limit regulations – that applies to all road types.

 
A full list of changes is published on the D-TRO GitHub repository at https://github.com/department-for-transport-public/D-TRO.
