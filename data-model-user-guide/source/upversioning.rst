Upversioning
^^^^^^^^^^^^

This section details the approach Department for Transport are taking for upversioning legacy D-TRO data.

Rationale
*********

The D-TRO service is an evolving service. Over time, changes are made to the data specification to support new TRO representations. This includes the addition of new fields and properties, restructuring of existing properties and concepts, and deprecation of outdated or obsolete properties.

The service manages this through the release of new data specification versions. Data specification releases adopts a semantic versioning approach, with major, minor and bugfix releases. A major version is released when the data specification includes breaking changes to the publishing or submission of D-TROs. Minor versions include additive, non-breaking changes to the data specification. Bugfix versions are released to address bugs in the data specification.

The D-TRO service endeavours to support the latest three versions of the data specification for submissions. As new versions are released, and older versions deprecated, the service is left with records that are submitted against legacy, unsupported data specification versions. For this reason, the service will implement an upversioning strategy, whereby records submitted against earlier unsupported schema versions complying to earlier data specification versions will be upversioned to validate against supported schemas.

High-level Approach
*******************

The first upversioning exercise is scheduled to be implemented with the data specification ``v4.0.0`` production release. At this time, all **active** records in the service submitted against schemas pre-``v3.5.1`` will be upversioned to ``v3.5.1`` records. Going forwards, upversioning will occur in combination with each new data specification release, and will upversion records to the latest-but-one schema version. This is a deliberate design decision that prevents the need for users to be forced to quickly adopt the latest data specification version for consumer applications.

.. notification::
    :heading: A note on pre-v3.4.0 D-TROs

    Prior to the introduction of schema ``v3.4.0``, the D-TRO service did not implement the full suite of schema validation that exists today. Therefore, D-TROs submitted in earlier schema versions exhibit large amounts of variation, and a stepwise upversioning approach is difficult to develop. Therefore, pre-``v3.4.0`` D-TROs will be upversioned directly to ``v3.4.0``, and then stepwise from this point forward.

v3.2.3 Strategy
***************

The following transformations have been applied to upversion D-TROs from ``v3.2.3`` to ``v3.4.0``.

* non-conforming datetimes for values of ``lastUpdateDate``, ``endOfPeriod``, ``startOfPeriod``, ``end`` and ``start`` were normalized to the schema-enforced ``YYYY-mm-ddTHH:MM:SS`` format
* ``geometry.externalReference`` and ``geometry.version`` properties were nested under their specific geometry type
* for records containing the deprecated ``geometry`` object, the children of this object were unnested into the parent object, and the ``geometry`` object deleted
* for records that represent ``externalReference`` as an object, this was wrapped in an array
* for records missing the mandatory ``linearGeometry.representation`` field, this field was added with a default value of ``linear`` *
* records missing the mandatory ``regulatedPlace.type`` field, this field added with a default value of ``regulationLocation`` *
* for orders with an ``orderReportingPoint`` that is **not** ``troOnRoadActiveStatus`` or ``permanentNoticeOfProposal`` and were missing the mandatory ``source.madeDate`` property, this property was added with a default value of ``2025-01-01`` *
* for orders with an ``orderReportingPoint`` that is **not** ``troOnRoadActiveStatus`` or ``permanentNoticeOfProposal`` and were missing the mandatory ``source.comingIntoForceDate`` property, this property was added with a default value of ``2025-01-01`` *
* for orders missing the mandatory ``source.statementDescription`` property, this was added with the default value ``**NOT PROVIDED**``
* for records with a value of ``miscTemporarySpeedLimit`` for ``regulationType``, this value was amended to ``**DEPRECATED**``
* for records not containing an ``externalReference.uniqueStreetReferenceNumber`` array, this was added with a single default object of ``{"usrn": 0}``
* for records missing a ``regulatedPlace.description`` property, this property was added with a default value of ``**NOT PROVIDED**``

v3.2.4 Strategy
***************

The following transformations have been applied to upversion D-TROs from ``v3.2.4`` to ``v3.4.0``.

* for records containing the deprecated ``geometry`` object, the children of this object were unnested into the parent object, and the ``geometry`` object deleted
* for records that represent ``externalReference`` as an object, this was wrapped in an array
* for records representing ``polygon`` as an arwray with a single object, the object was unnested from the array
* records missing the mandatory ``polygon.version`` property had the property added with a default value of ``1``
* for records whose provisions contain specific order reporting points but not the required mandatory properties, these properties and default values were added as follows: ``concession: false``, ``assignment: false``, ``tramcar: false``, ``busRoute: false`` and ``bywayType: **NOT PROVIDED**``
* records missing the ``regulatedPlace.type`` property had this added with a default value of ``regulationLocation``
* for orders with an ``orderReportingPoint`` that is **not** ``troOnRoadActiveStatus`` or ``permanentNoticeOfProposal`` and were missing the mandatory ``source.madeDate`` property, this property was added with a default value of ``2025-01-01`` *
* for orders with an ``orderReportingPoint`` that is **not** ``troOnRoadActiveStatus`` or ``permanentNoticeOfProposal`` and were missing the mandatory ``source.comingIntoForceDate`` property, this property was added with a default value of ``2025-01-01``
* records missing the mandatory ``source.statementDescription`` field had the field added with a default value of ``**NOT PROVIDED**``
* the unrecognized ``consultations`` property and its children were deleted from records containing this
* ``condition`` arrays containing no items had a default child of ``{"driverCondition": {"driverCharacteristics": "localResident"}}`` property had this added *

v3.3.0 Strategy
***************

The following transformations have been applied to upversion D-TROs from ``v3.3.0`` to ``v3.4.0``.

* ensure every ``externalReference`` entry has a valid ``uniqueStreetReferenceNumber`` array, creating one if needed, and normalising any existing ones to a consistent format. For missing or empty ``externalReference.uniqueStreetReferenceNumber`` arrays, a single default object of ``{"usrn": 0}`` was added
* records missing the mandatory ``source.statementDescription`` field had the field added with a default value of ``**NOT PROVIDED**``
* for orders with an ``orderReportingPoint`` that is not ``troOnRoadActiveStatus`` or ``permanentNoticeOfProposal`` that are missing the mandatory ``madeDate`` property, this was added with a default value of ``2025-01-01`` *
* for records containing the ``temporaryRegulation`` property, this property was deleted
* for records containing a ``linearGeometry`` property but missing the mandatory ``representation`` child, this was added with a default value of ``**NOT PROVIDED**``
* for records containing a ``regulationType`` with an enum value of ``miscTemporarySpeedLimit``, this value was updated to ``**DEPRECATED**``
* for records missing the mandatory ``regulatedPlace[*].description`` field, a default ``description`` with value ``**NOT PROVIDED**`` was added
* for records missing the ``generalRegulation.regulationType`` property, a default value of ``**NOT PROVIDED**`` was added
* for records where ``externalReference`` is represented as an object, this was wrapped in an array
* for records containing empty ``consultation`` arrays, these arrays were deleted
* for records whose provisions contain specific order reporting points but not the required mandatory properties, these properties and default values were added as follows: ``concession: false``, ``assignment: false``, ``tramcar: false``, ``busRoute: false`` and ``bywayType: **NOT PROVIDED**``
* for records where ``timeValidity`` is represented as an array with a single object, this object was unnested from the array
* for records with invalid datetime formats for values of keys ``startTimeOfPeriod`` and ``endTimeOfPeriod``, these were normalized to ``YYYY:mm:ddddTHH:MM:SS`` format

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

* the mandatory ``timeValidity.isPlaceholderTro`` property was added with a default value of ``false``

v3.5.0 Strategy
***************

All published ``v3.5.0`` D-TROs were compliant with ``v3.5.1`` of the schema, and so no transformations were applied.






