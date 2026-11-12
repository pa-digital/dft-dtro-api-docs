Annex D - D-TRO Guidance 2026
=============================

Purpose, scope and legal status
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This non-statutory guidance supports implementation of the Traffic Orders and Notices (Provision of Digital Information) (England) Regulations 2026.

In this guidance these Regulations are referred to as the D-TRO Regulations, for brevity.

The guidance explains the statutory requirements under the D-TRO Regulations for providing digital information relating to traffic regulation measures (TRMs) to the central publication platform for the traffic regulation measures digital service, supported by the Department for Transport, also known as the D-TRO service.

TRMs are specific Traffic Regulation Orders (TROs) that are defined in section 93 of the Automated Vehicles Act 2024.  A TRO is the legal order needed to set and enforce rules that prohibits, restricts or regulates use of a road. They are used by traffic authorities (including local authorities, the Secretary of State, and strategic highways companies) to regulate traffic in their areas.

There are different types of TRMs, for instance, they can be permanent, temporary, experimental, or special events. They can be in the form of orders or notices. TRMs are needed to, for example, install a bus lane and set rules about who can use it and at what times, introduce controlled parking zones or pedestrianised areas, close a road, either permanently or temporarily, for road works and to set times and locations for loading and unloading.

Speed limit orders (SLOs) are made using the same procedures as for TRMs, so the D-TRO Regulations would also affect those where relevant. This guidance uses the term 'TRMs' to include all types of relevant orders and notices defined under section 93(3) of the Automated Vehicles Act 2024.

Authorities already follow procedures for making TROs that are set out in three statutory instruments:

* The Secretary of State's Traffic Orders (Procedure) (England and Wales) Regulations 1990 (SI 1990/1656)
* The Road Traffic (Temporary Restrictions) Procedure Regulations 1992 (SI 1992/1215)
* The Local Authorities' Traffic Orders (Procedure) (England and Wales) Regulations 1996 (SI 1996/2489)

The D-TRO Regulations do not change these procedures. 

Section 93 of the Automated Vehicles Act 2024 (the 2024 Act) gives the Secretary of State a power to make regulations requiring a traffic regulation authority to provide:

* prescribed information about a relevant traffic regulation measure
* in a digital format
* to a central publication platform
* in line with a common data model and standards

The D-TRO Regulations, made under section 93 of the 2024 Act, make provision about:

* to whom the information is to be provided
* when it is to be provided, and
* the manner and form in which it is to be provided

Nothing in this guidance replaces the legal requirements contained within the Regulations. Where there is any discrepancy between this guidance and the D-TRO Regulations, the D-TRO Regulations take precedence.

This guidance should be read alongside:

* The D-TRO Regulations themselves, which can be found at https://www.example.com
* The Explanatory Memorandum, which can be found at https://www.example.com
* The D-TRO Data Specification - which are described further below.

The D-TRO Data Specification can be found at the official D-TRO portal, at the following link: https://d-tro.dft.gov.uk. This comprises:

* the D-TRO Data Model,
* the JSON schema, which a document that defines the structure, data types, and validation rules for JSON data; JSON (JavaScript Object Notation) is a simple, text-based format for storing and exchanging data,
* validation rules, and
* technical guidance documentation.

The technical guidance documentation suite includes the Data Model User Guide, API (Application Programming Interface) documentation, and a Quickstart guide designed to facilitate integration. Furthermore, to assist developers and authorities, the D-TRO Data Specification is supported by practical technical artefacts, including example files. Further information can be found at the official D-TRO portal.

The D-TRO data specification may change from time to time.

This guidance will be kept under review to ensure its correctness and completeness.

With the D-TRO Regulations, TRAs must ensure all submissions adhere to the D-TRO Data Specification schema as they exist from time to time, validation rules and any mandatory instructions specified in the technical guidance documentation hosted on the official D-TRO portal.

Who the guidance applies to
^^^^^^^^^^^^^^^^^^^^^^^^^^^

This guidance applies to all Traffic Regulation Authorities in England. A Traffic Regulation Authority (TRA) is a person that has the power to make traffic regulation measures (TRMs). This includes all traffic authorities and any authority to which power to make a TRO has been delegated, such as National Highways and Transport for London.

Which TRMs are covered and commencement dates
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

A specified in the 2024 Act, a Traffic Regulation Measure (TRM) means an order or notice made under any of the following provisions of the Road Traffic Regulation Act 1984. This guidance will refer to TRMs as this is the term used in the 2024 Act and the D-TRO Regulations:
* Section 1 (traffic regulation orders)
* Section 6 (orders regulating traffic in Greater London)
* Section 9 (experimental traffic orders)
* Section 14 (temporary orders and notices)
* Section 16A (special event orders), or
* Section 84 (speed limits)

The requirements apply in relation to:
* new TRM made after commencement;
* circumstances where a post-commencement measure amends a pre-commencement measure. If a post-commencement TRM only revokes a pre-commencement TRM, then the requirements under the D-TRO Regulations do not apply. If a post-commencement TRM changes a pre-commencement TRM, the requirements apply only with respect to the provisions amended.

The D-TRO Regulations do not apply to specified anti-terrorism traffic regulation measures.

The coming into force date for the provisions in the D-TRO Regulations which require the submission of “real time” start and stop information for TRM made for local authorities' own works is 2 October 2028, see regulations 7, 9(4)(b) and (c) and 9(5)(b) and (c), to allow sufficient time for technical and operational compliance.

The coming into force date for the remainder of the D-TRO Regulations is 11 February 2027.

What Information must be supplied
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Under the D-TRO Regulations TRAs shall submit D-TRO information at specified points in the lifecycle of TRM, relating to the Road Traffic Regulation Act 1984.

The Regulations require reporting at three levels:

**Measure-Level Information**

Authorities must provide information as specified in regulation 4(1) relating to:

* title - Full legal title of the Order, Notice or Instrument as made by the TRA.
* date made - Date on which the Order was legally made by the TRA.
* commencement date - Date on which the measure comes into force and acquires legal effect.
* duration - Overall legal duration of the measure including permanent, temporary, experimental or special-event applicability.
* general description - Free text description of the prohibition, restriction, regulation or permission established by the measure.
* operational dates and times - The dates, periods and times when the measure is active or anticipated to be active, including recurring and conditional periods where applicable Anticipated future dates and times provide insight of the timing of the operational effect of the prohibition, restriction, regulation or permission established by the measure. When anticipated dates and times are modified, or become actual operational dates and times, updated D-TRO records should be supplied to the D-TRO service.
* linked DTRO identifiers where relevant - References to related D-TRO records, amended orders, parent orders, replacement orders or linked provisions.

**Provision-Level Information**

Authorities must provide information as specified in regulation 4(2), 4(3),4(4) so far as that information is relevant for the provision is question. For precise description of the information to be supplied refer to the regulations themselves. This information relates to:

* affected roads - Roads, streets, highways or byways to which the provision applies, supported where possible by machine-readable location references and geometry.
* affected locations - The regulated place or places subject to the provision.
* alternative routes - Diversionary routes associated with closures or restrictions, described in sufficient detail for digital navigation and routing services.
* bus services - Identification of whether bus routes, local services or London bus services materially affected by the provision.
* tram services - Identification of whether tramway or trolley vehicle operations affected by the provision.
* speed limits - Relevant speed restriction values, profiles or temporary speed management measures.
* charges - Any charge or monetary obligation arising from the provision. For instance, if relevant to the provision in question, this might include parking charges. conditions and exceptions - All qualifying conditions, exemptions, exclusions and eligibility requirements governing application of the provision.

**Restriction-Level Information**

Authorities must provide information as specified in regulation 5. For a precise description of the information to be supplied refer to the regulation itself. This information relates to:

* vehicle classes - Vehicle categories to which the measure applies, permits or exempts, using standardised vehicle characterisation concepts.
* dimensions - Maximum or minimum vehicle dimensions including height, width, length, axle weight or gross weight where relevant.
* fuel types - Vehicle propulsion or fuel characteristics used within access, environmental or charging-based restrictions.
* emissions criteria - Emission classifications, environmental standards and low-emission conditions applicable to vehicle access.
* specified goods - Particular loads, dangerous goods or cargo-related characteristics relevant to the restriction.
* driver characteristics - Driver eligibility conditions such as resident, permit holder, disabled badge holder or learner status.
* passenger characteristics - Occupancy or passenger-based conditions including accessibility and high-occupancy requirements.

**Experimental Traffic Orders** 

Authorities must provide additional information where an experimental order is modified, suspended or terminated before the anticipated end date. Information should clearly identify the affected provision, the legal effect of the change, revised duration, and actual cessation details to support auditability and lifecycle management.

**Own-Works Reporting for Temporary Traffic Regulation Orders**

From 2 October 2028 applicable own-works restrictions require reporting of actual start and stop times representing operational occupation of the highway rather than planned timings, see regulation 7. This allows digital users to receive near real-time information.

When information must be provided
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Permanent Orders, see regulation 9(2)**

As soon as practicable and within two working days.

**Experimental Orders, see regulation 9(3)**

As soon as practicable and within two working days, including extensions and modifications.

**Temporary Orders and Notices, see regulation 9(4) and 9(5)**

Specific timing requirements apply, including actual start and stop reporting from 2 October 2028. Please refer to the regulation for the specific requirements.

**Special Event Orders, see regulation 9(6)**

On the day the order is made.

How to submit information through the D-TRO Service
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The Department for Transport (DfT) has built a central publication platform for the traffic regulation measures digital service, also known as the D-TRO service. The D-TRO Service is a data centered service, with data being submitted and extracted using Application Programming Interfaces (APIs).

DfT has been developing the D-TRO service and its Data Specification with authorities and software providers.

The objectives of the D-TRO service are to:

* provide a single trusted source of traffic regulation data for England;
* support digital transport services;
* support automated vehicle operation;
* improve data consistency;
* improve accessibility of traffic regulation information; and
* support innovation and reuse.

Access to the D-TRO Service
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Digital TRO data is sent to the D-TRO Service. Access to this data is managed as follows:

* Data Publishers: TRAs and Digital Service Providers must complete a two-step onboarding process, starting with an account in the integration/sandbox environment for testing before gaining production environment access to publish live data.
* Data Consumers: Any individual or organisation may register for a free consumer account to access D-TRO data via the API, subject to verification by the DfT Central Service Operator (CSO).
* To register for the service and access the D-TRO Data Specification and other technical artefacts see the official D-TRO portal.

Duty to Keep Information Accurate 
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

TRAs must in respect of data submitted to the D-TRO service, correct inaccuracies, report newly identified prescribed information, update records following amendment, suspension or revocation, see regulation 10.

**Data Ownership, Responsibilities and Governance**

**Traffic Regulation Authorities**

Traffic Regulation Authorities (TRAs) remain responsible for the legal accuracy, currency and completeness of data supplied in a timely manner to the D-TRO service. TRAs are responsible for maintaining up to date data in the D-TRO service, correcting identified errors and maintaining records throughout their lifecycle (see regulation 10).

Submission to the D-TRO Service does not transfer ownership of the source information. The TRA remains the data owner and authoritative source.

**Digital Solution Providers**

Many TRAs will use software providers to manage D-TRO submissions to the D-TRO Service. These are referred to as Digital Solution Providers (DSPs).

Where a DSP submits information on behalf of a TRA: 

* responsibility for the accuracy and completeness of information submitted to the D-TRO Service remains with the TRA;
* the TRA should maintain quality assurance processes. 

**Department for Transport (DfT)**

The Department for Transport:

* operates the D-TRO Service;
* maintains the D-TRO data specification;
* manages onboarding processes;
* re-publishes D-TRO data; and
* supports reuse of the information.

DfT is the data custodian in the context of the D-TRO service, and is responsible for making data available but not for its accuracy or completeness. 

**Data Consumers**

A data consumer to encouraged to:

* Consume D-TROs in accordance with the service terms and licence. Further information on licensing can be found at the following link: https://d-tro.dft.gov.uk/dtro?id=kb_article_view&sysparm_article=KB0010666
* Note that the authoritative legal instrument remains the underlying TRO.

A data consumer should endeavour to:

* Monitor updates, amendments, revocations and expiry dates.
* Refresh local systems regularly.
* Not misrepresent restrictions.
* Preserve the effect represented by the published D-TRO.

Voluntary Information
^^^^^^^^^^^^^^^^^^^^^

This guidance supports the implementation of the requirements, including voluntary information that, if it is available, authorities can send to D-TRO service.

Traffic regulation authorities may optionally provide additional information to enhance the dataset, including:

* Data regarding proposed TRMs.
* Parking charges orders made under sections 32 or 45 of the Road Traffic Regulation Act 1984, which may not otherwise meet the definition of a TRM under the Automated Vehicles Act 2024.
* Bridge height warning and restriction data.
* Restrictions that do not require a TRO - e.g. restricted roads, box junctions, bus stops, pedestrian crossings, stop lines, keep left, school keep clear.
* Additional voluntary data sets are under consideration.

Spatial Data and Ordnance Survey Coordinate Randomisation
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The publication of data from the D-TRO Service is foreseen as open data. To ensure that the D-TRO service does not infringe copyright of Ordnance Survey's Licenced Data, DfT and Ordnance Survey have reached an agreement to randomly shift some of the spatial data associated with D-TRO records. With the exception of Temporary Traffic Regulation Orders (TTROs) or a D-TRO where the effect of where the regulation is in effect (e.g. regulatedPlace) is represented by a single point, all vertices are randomised. Each vertex is randomised between 0.5 metre and 0.75 metre. The resultant data set is freely available as open data under an Open Government Licence v.3.0 (Open Government Licence). For further information please visit https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/.

The published open dataset therefore differs slightly from the original submitted geometry.

The raw, unrandomised spatial data sent to the D-TRO service will be made available to third parties holding an appropriate Ordnance Survey Licence, including members of OS's Public Sector Geospatial Agreement (PSGA). To access the data licence holders should contact OS Pricing and Licensing Team (pricinglicensing@os.uk).

TRAs should continue to submit accurate source geometry in accordance with the data specification.

Key terms - Provisions, Regulations and Regulated Places
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Provision**

A **Provision** is an individually identifiable component of a Traffic Regulation Measure that applies a specific regulatory effect to a particular location, road, movement, vehicle category, user category or period of operation.

A provision is the practical expression of part of a measure. It defines precisely where, when and to whom a regulatory effect applies. A single Traffic Regulation Measure may contain many provisions.

For example, a town-centre pedestrianisation measure may contain separate provisions governing access by buses, taxis, residents and loading activities.

**Regulation**

Within the D-TRO Data Specification, a **Regulation** is an identifiable, distinct prohibition, restriction, requirement, permission or condition imposed by a provision.

The regulation defines exactly what road users may, must or must not do.

A provision may contain several regulations operating together.

Examples of regulations may include, for example, bus lane restrictions; kerbside waiting and loading restrictions, permit parking restrictions.

**Regulated Place**

A **Regulated Place** is the spatial extent of the highway, road network or transport infrastructure to which a provision or regulation applies.

The regulated place defines the geographic scope of the legal restriction or permission. It represents the real-world location affected by the regulation and may be represented digitally by points, linear features, areas, carriageways, lanes, movements or network elements.

A regulated place is not itself a restriction; it is the location to which a restriction applies.

Submission of historic legacy, in force Traffic Regulation Measures
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The 2024 Act also gives the Secretary of State powers to require information from TRMs made before 2024 (see section 93(9)), that is, the archive of existing TRMs. To note, except where a TRM was made before 11 February 2027 and is being amended after the coming into force of the Regulations, we are not requiring authorities to submit information in earlier TRMs at the current time. However, D-TRO will accept the submission of information from such TRMs if an authority wants to submit that information voluntarily.