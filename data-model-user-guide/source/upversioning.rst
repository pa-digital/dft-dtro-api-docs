Upversioning
^^^^^^^^^^^^

This section details the approach Department for Transport are taking for upversioning legacy D-TRO data.

Rationale
*********

The D-TRO service is an evolving service. Over time, changes are made to the data model to support new TRO representations. This includes the addition of new fields and properties, restructuring of existing properties and concepts, and deprecation of outdated or obsolete properties.

The service manages this through the release of new schema versions. Schema releases adopts a semantic versioning approach, with major, minor and bugfix releases. A major version is released when the data model includes breaking changes to the publishing or submission of D-TROs. Minor versions include additive, non-breaking changes to the data model. Bugfix versions are released to address bugs in the model.

The D-TRO service endeavours to support the latest three versions of the data model for submissions. As new versions are released, and older versions deprecated, the service is left with records that are submitted against legacy, unsupported data model versions. For this reason, the service will implement an upversioning strategy, whereby records submitted against unsupported schema versions will be upversioned to validate against supported schemas.

High-level Approach
*******************

The first upversioning exercise is scheduled to be released with the ``v4.0.0`` production release. At this time, all **active** records in the service submitted against schemas pre-``v3.5.1`` will be upversioned to ``v3.5.1`` records. Going forwards, upversioning will occur in combination with each new schema release, and will upversion records to the latest-but-one schema version. This is a deliberate design decision that prevents the need for users to have bleeding-edge consumer applications.

.. notification::
    :heading: A note on pre-v3.4.0 D-TROs

    Prior to the introduction of schema ``v3.4.0``, the D-TRO service did not implement the full suite of schema validation that exists today. Therefore, D-TROs submitted in earlier schema versions exhibit large amounts of variation, and a stepwise upversioning approach is difficult to develop. Therefore, pre-``v3.4.0`` D-TROs will be upversioned directly to ``v3.4.0``, and then stepwise from this point forward.

v3.2.3 Strategy
***************

The following transformations have been applied to upversion D-TROs from ``v3.2.3`` to ``v3.4.0``.

* non-conforming datetimes for values of ``lastUpdateDate``, ``endOfPeriod``, ``startOfPeriod``, ``end`` and ``start`` were normalized to the schema-enforced ``dd:mm:YYYYTHH:MM:SS`` format
* ``geometry.externalReference`` and ``geometry.version`` properties were nested under their specific geometry type
* for records containing the deprecated ``geometry`` object, the children of this object were unnested into the parent object, and the ``geometry`` object deleted
* for records that represent ``externalReference`` as an object, this was wrapped in an array
* for records missing the mandatory ``linearGeometry.representation`` field, this field was added with a default value of ``linear`` *
* records missing the mandatory ``regulatedPlace.type`` field, this field added with a default value of ``regulationLocation`` *
* for orders with an ``orderReportingPoint`` that is **not** ``troOnRoadActiveStatus`` or ``permanentNoticeOfProposal`` and were missing the mandatory ``source.madeDate`` property, this property was added with a default value of ``2025-01-01`` *
* for orders with an ``orderReportingPoint`` that is **not** ``troOnRoadActiveStatus`` or ``permanentNoticeOfProposal`` and were missing the mandatory ``source.comingIntoForceDate`` property, this property was added with a default value of ``2025-01-01`` *
* for orders missing the mandatory ``source.statementDescription`` property, this was added with the default value ``**NOT PROVIDED**``
* for records with a value of ``miscTemporarySpeedLimit`` for ``regulationType``, this value was amended to ``**DEPRECATED**``
* for records not containing a ``uniqueStreetReferenceNumber`` array, this was added with a single default object of ``{"usrn": 0}``
* for records missing a ``regulatedPlace.description`` property, this property was added with a default value of ``**NOT PROVIDED**``

v3.2.4 Strategy
***************

The following transformations have been applied to upversion D-TROs from ``v3.2.4`` to ``v3.4.0``.

* the deprecated ``regulationStatus`` property was deleted from records containing this
* records with a missing or empty mandatory ``source.troName`` had the property added with a default value of ``**NOT PROVIDED**``
* records missing the mandatory ``regulation.isDynamic`` property had the property added with a defualt value of ``false``
* records missing the mandatory ``regulation.timeZone`` property had the property added with a default value of ``Europe/London``
* for records representing ``polygon`` geometry types as arrays, these were validated to ensure they contained only single objects as children, and then the object unnested from the array
* records missing the mandatory ``polygon.version`` property had the property added with a default value of ``1``
* for records whose provisions contain specific order reporting points but not the required manadatory properties, these properties and default values were added as follows: ``concession: false``, ``assignment: false``, ``tramcar: false``, ``busRoute: false`` and ``bywayType: **NOT PROVIDED**``
* for records containing empty ``consultation`` arrays, these arrays were deleted
* for records containing the unrecognized ``validityCondition`` property, child ``condition`` properties were unnested, and ``validityCondition`` was deleted
* for records with a ``regulationType`` using the deprecated ``speedLimitValueType``, this value was updated to ``**DEPRECATED**``
* for records with null ``usrn`` properties, a default value of ``0`` was applied
* misspelled ``kerbsidePemitParkingPlace`` values of the ``regulationType`` enum were corrected to ``kerbsidePermitParkingPlace``
* deprecated property ``regulationFullText`` was deleted
* deprecated property ``regulationShortName`` was deleted
* unnested ``timeValidity`` objects that are children of a ``validityCondition`` condition, representing them as their own ``condition``
* ``vehicleType`` values represented as an array were unnested to single values
* misspelled field ``permitIdentifer`` was renamed to ``permitIdentifier``, and values represented as an array were unwrapped to single values
* ``permitCondition`` children not nested under a ``permitCondition`` parent were wrapped in this parent object
* for records containing none of the mandatory ``regulation`` children, the default child object ``{"offListRegulation": {"regulationShortName": "**NOT PROVIDED**", "regulationFullName": "**NOT PROVIDED**"}}``
* records containing a ``driverCharacteristicsType`` child not inside a ``driverCondition`` parent were wrapped in this parent object. ``driverCharacteristicsType`` was renamed to ``driverCharacterstics``
*  records containing a ``vehicleUsageType`` child not inside a ``vehicleCondition`` parent were wrapped in this parent object. ``vehicleUsageType`` was renamed to ``vehicleUsage``
*  records missing the madatory ``regulatedPlace.description`` field has this added with a default value of "**NOT PROVIDED**"
*  records with a ``permitCondition`` object where ``permitCondition.type`` was set to ``other`` but missing the ``permitType.permitTypeExtension`` object had this object added with the following default values: ``{"permitTypeExtension": {"definition": "**NOT PROVIDED**", "value": "**NOT PROVIDED**", "enumeratedList": "permitType"}}``
*  the deprecated ``regulationType`` enum value ``otherBusLaneWithTrafficFlow`` was replaced with ``**DEPRECATED**``  

v3.3.0 Strategy
***************

The following transformations have been applied to upversion D-TROs from ``v3.3.0`` to ``v3.4.0``.

* ensure every ``externalReference`` entry has a valid ``uniqueStreetReferenceNumber`` array, creating one if needed, and normalising any existing ones to a consistent format. For missing or empty ``uniqueStreetReferenceNumber`` arrays, a single default object of ``{"usrn": 0}`` was added
* records missing the mandatory ``source.statementDescription`` field had the field added with a default value of ``**NOT PROVIDED**``
* for orders with an ``orderReportingPoint`` that is not ``troOnRoadActiveStatus`` or ``permanentNoticeOfProposal`` that are missing the mandatory ``madeDate`` property, this was added with a default value of ``2025-01-01`` *
* for records containing the ``temporaryRegulation`` property, this property was deleted
* for records containing a ``linearGeometry`` property but missing the mandatory ``representation`` child, this was added with a default value of ``**NOT PROVIDED**``
* for records containing a ``regulationType`` with an enum value of ``miscTemporarySpeedLimit``, this value was updated to ``**DEPRECATED**``
* for records missing the mandatory ``regulatedPlace[*].description`` field, a default ``description`` with value ``**NOT PROVIDED**`` was added
* for records missing the ``generalRegulation.regulationType`` property, a default value of ``**NOT PROVIDED**`` was added
* for records where ``externalReference`` is represented as an object, this was wrapped in an array
* for records containing empty ``consultation`` arrays, these arrays were deleted
* for records whose provisions contain specific order reporting points but not the required manadatory properties, these properties and default values were added as follows: ``concession: false``, ``assignment: false``, ``tramcar: false``, ``busRoute: false`` and ``bywayType: **NOT PROVIDED**``
* for records where ``timeValidity`` is represented as an array with a single object, this object was unnested from the array
* for records with invalid datetime formats for values of keys ``startTimeOfPeriod`` and ``endTimeOfPeriod``, these were normalized to ``dd:mm:YYYYTHH:MM:SS`` format

v3.3.1 Strategy
***************

To upversion from ``v3.3.1`` to ``v3.4.0``, the above transformations for upversioning ``v3.3.0`` records were applied, in addition to the following.

* ``directedLinear.externalReference`` was renamed to ``directedLinear.origin``

v3.4.0 Strategy
***************

All published ``v3.4.0`` D-TROs were compliant with ``v3.4.1`` of the schema, and so no transformations were applied.

v3.4.1 Strategy
***************

The following transformations have been applied to upversion from ``v3.4.1`` to ``v3.5.0``.

* the mandaotry ``timeValidity.isPlaceholderTro`` property was added with a default value of ``false``

v3.5.0 Strategy
***************

All published ``v3.5.0`` D-TROs were compliant with ``v3.5.1`` of the schema, and so no transformations were applied.






