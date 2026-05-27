Provision-Level Management
^^^^^^^^^^^^^^^^^^^^^^^^^^

This section sets out the approach the Department for Transport is taking to support the creation, update and deletion of provisions.

Rationale
*********

D-TROs often contain multiple provisions, each representing discrete regulatory elements that may evolve independently over time. In the current model, any change to a provision - whether creating a new one, modifying an existing one, or removing an obsolete one - requires resubmission of the entire D-TRO.

This approach introduces several challenges:

* **Unnecessary overhead**: Re-submitting a complete D-TRO for small, localised changes is inefficient for users and systems, particularly where only a single provision is affected
* **Increased risk of error**: Full resubmission increases the likelihood of unintentionally altering unrelated provisions or metadata, reducing data quality and consistency
* **Limited flexibility**: Users are unable to manage provisions in a granular way that reflects how Traffic Regulation Orders are maintained in practice, where individual provisions are frequently updated independently
* **Processing inefficiency**: Handling full D-TRO payloads for minor changes places unnecessary load on validation and ingestion processes
  
To address these limitations, the service introduces provision-level management, allowing users to create, update, and delete individual provisions within an existing D-TRO without needing to resubmit the entire object.

This approach:

* Aligns the service more closely with real-world operational workflows
* Reduces the burden on users when making incremental changes
* Minimises the risk of unintended modifications to unrelated data
* Improves system efficiency by limiting the scope of changes being processed
* Enables more responsive and maintainable management of evolving D-TRO records

Provision-level management therefore provides a more scalable, precise, and user-centred approach to maintaining D-TRO data over time.

High-level Approach
*******************

Provision-level management enables the service to operate on the individual regulatory components that make up a D-TRO, rather than treating the D-TRO as a single monolithic object. This reflects how Traffic Regulation Orders are structured and maintained in practice, where a single order may contain multiple distinct provisions that evolve independently over time.

Within the D-TRO data model, each record represents a single order, while each provision captures a specific regulatory rule, defined by a consistent set of conditions, exemptions, times of applicability, and, where relevant, tariff rates, and associated with one or more regulated places. A single D-TRO may therefore include multiple provisions - for example, separate parking, loading, and speed limit restrictions - each of which may require independent management.

Provision-level management allows changes to be applied directly to these individual components, avoiding the need to resubmit the entire D-TRO when only a small part of the record is changing. This enables more precise updates, reduces unnecessary processing, and limits the risk of unintended changes to unrelated parts of the order.

This approach also supports the handling of large or complex D-TROs by enabling incremental updates at the provision level. Rather than processing large payloads representing entire orders, the service can manage changes in a more targeted and scalable way.

Provision-level management is implemented through the operational capabilities described below.

Operational Approach
********************

Provision-level management is delivered through a set of dedicated endpoints that allow users to create, update, and delete individual provisions associated with an existing D-TRO record. These operations enable targeted modifications without requiring resubmission of the full D-TRO.
The service supports the following operations:

* **Create provisions**: One or more provisions can be added to an existing D-TRO by submitting a request to a provisions endpoint. The request includes the D-TRO identifier and a payload containing the provision data to be created
* **Update provisions**: An existing provision can be modified by submitting an updated provision payload to a provision-specific endpoint. The provision to be updated is identified by its provision ID
* **Delete provisions**: An existing provision can be removed by issuing a request against the provision ID. This deletes only the specified provision and does not affect other provisions within the same D-TRO

Each operation is scoped to the relevant provision or set of provisions, ensuring that changes are applied only to the intended parts of the D-TRO. The service validates provision payloads in line with the D-TRO data specification and maintains consistency between provisions and their parent D-TRO.

Detailed endpoint usage can be found in the D-TRO API documentation.
