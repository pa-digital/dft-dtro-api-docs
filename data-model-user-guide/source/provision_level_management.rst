Provision level managment
^^^^^^^^^^^^

This section sets out the approach the Department for Transport is taking to support the creation, update and deletion of provisions.

Rationale
*********

The D-TRO service is an evolving service. Over time, changes are made to the data specification to support new TRO representations. This includes the addition of new fields and properties, restructuring of existing properties and concepts, and deprecation of outdated or obsolete properties.

The service manages this through the release of new data specification versions. Data specification releases adopts a semantic versioning approach, with major, minor and bugfix releases. A major version is released when the data specification includes breaking changes to the publishing or submission of D-TROs. Minor versions include additive, non-breaking changes to the data specification. Bugfix versions are released to address bugs in the data specification.

The D-TRO service endeavours to support the latest three versions of the data specification for submissions. As new versions are released, and older versions deprecated, the service is left with records that are submitted against legacy, unsupported data specification versions. For this reason, the service will implement an upversioning strategy, whereby records submitted against earlier unsupported schema versions complying to earlier data specification versions will be upversioned to validate against supported schemas.

High-level Approach
*******************

Provision-level management is required to support the way D-TRO records are structured and maintained, particularly where a single Traffic Regulation Order contains multiple distinct regulatory provisions. The official D-TRO data model describes each D-TRO record as containing the information for one D-TRO record, while each provision represents one specific type of regulation, subject to a homogeneous set of conditions, exemptions, times of applicability and, where relevant, tariff rates, and related to one or more regulated places. This means that a single order may legitimately contain multiple provisions — for example, separate parking, loading and speed-limit restrictions — each of which may need to be managed independently within the same overall D-TRO record.

Adding provision-level management also provides a clearer mechanism for handling large or complex D-TROs. Support for provision-level management of D-TROs feeds into the large D-TRO work, explicitly linked provision-level management with the need to split or manage large D-TROs by provision. This approach reduces the need to treat the D-TRO as a single monolithic object when only part of the order is changing, and instead allows the system to track, process and reason about the individual regulatory components that make up the order.

Provision-level management is also aligned with the lifecycle semantics already present in the D-TRO model. The public schema and user guide include provision-level action types which indicate how a specific provision relates to an earlier version of that provision. Managing provisions explicitly therefore supports more accurate versioning, amendment, revocation, auditability and downstream consumption, while remaining consistent with the Department for Transport’s published model and GitHub artefacts for D-TRO. The D-TRO Data Model User Guide also states that users and stakeholders are encouraged to review and provide feedback through the public GitHub repository, reinforcing the importance of keeping this implementation aligned with the published specification.
