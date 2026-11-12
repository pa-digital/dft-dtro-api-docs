Digital Traffic Regulation Orders - The Government's response to the consultation
=================================================================================

Introduction
^^^^^^^^^^^^

This report should be read in conjunction with the corresponding consultation Digital Traffic Regulation Orders. It presents the government's response to the proposed amendments to the regulations.

Traffic Regulation Orders (TROs) are legal instruments used by traffic authorities to 
manage the public road network. They enable authorities to introduce and enforce rules 
such as speed limits, parking restrictions, bus lanes, pedestrian zones, and temporary 
road closures. TROs are essential for delivering safe, efficient, and responsive transport systems, and they play a critical role in supporting wider government priorities including economic growth, decarbonisation, and improved public transport.

Despite their importance, the current process for creating and publishing TROs is 
fragmented. Many authorities still rely on paper-based systems or locally stored digital files, which limits the accessibility, consistency, and interoperability of TRO data. This presents challenges for road users, utility companies, transport operators, and emerging technologies such as automated vehicles, which increasingly rely on accurate, real-time traffic regulation data.

To address these challenges, the Department for Transport (DfT) has developed the 
Digital Traffic Regulation Orders (D-TRO) service—a central digital platform designed to receive, store, and publish traffic regulation measures (TRMs) in a standardised, digital format. The D-TRO service is being built in accordance with the Government Digital Service's standards and has been shaped by extensive user research with authorities and digital solution providers.

The D-TRO service is supported by a data specification that defines the structure and 
standards for TRM data. Authorities will submit information via an application programming interface (API), and the data will be published as open data for use by automated vehicles, navigation systems, and other digital services. The service is designed to integrate with existing systems such as Street Manager, and aims to reduce administrative burden, improve data accuracy, and enhance public transparency.

Section 93 of the Automated Vehicles Act 2024 provides the legal basis for requiring traffic regulation authorities (TRAs) to submit prescribed information about TRMs to the D-TRO service. The draft regulations set out the scope, timing, and format of these requirements. They apply to TRMs made under sections 1, 6, 9, 14, 16A, and 84 of the Road Traffic Regulation Act 1984, and cover both new and amended measures from the date the regulations come into force.

This consultation, held between 23 January and 21 March 2025, sought views on the draft 
regulations, including the proposed data fields, reporting timelines, system integration, and implementation challenges. A total of 93 responses were received from a wide range of stakeholders, including local authorities, utility companies, digital solution providers, and representative organisations.

This report summarises the feedback received, outlines the Government's response to 
each issue, and explains how the regulations have been amended to reflect stakeholder 
input. It also sets out the next steps for implementation, including the development of non-statutory guidance and support for authorities transitioning to digital systems.

Summary of the Responses
^^^^^^^^^^^^^^^^^^^^^^^^

A total of 93 responses were received from a wide range of stakeholders. This was a 
targeted stakeholder consultation and was not made available to the general public. The 
breakdown is as follows:

.. list-table::
   :header-rows: 1
   :widths: 70 30

   * - Type of Respondent
     - Number of Responses
   * - Local Authorities
     - 67
   * - Utility Companies
     - 7
   * - Technology company
     - 4
   * - Representative Organisations
     - 3
   * - NGOs / Not-for-profits
     - 2
   * - Individuals
     - 8
   * - Professional body
     - 1
   * - Other
     - 1
   * - **Total**
     - **93**

Response to Consultation Questions, feedback and Government Responses
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Section 1: Implementation Date for D-TRO Requirements
-----------------------------------------------------

Relevant Question(s)
~~~~~~~~~~~~~~~~~~~~

Q6: When would you want the requirement to submit information to D-TRO to come into
force?

Purpose of the Section
~~~~~~~~~~~~~~~~~~~~~~

To determine stakeholders’ preferred timeline for the commencement of mandatory digital
submission of traffic regulation measures (TRMs) to the D-TRO platform, and assess
readiness across authorities.

Summary of Responses
~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: 70 30

   * - Preferred Start Date
     - Number of Respondents
   * - 1 July 2025
     - 4
   * - 1 October 2025
     - 79
   * - Either date
     - 10

Consultation Feedback
~~~~~~~~~~~~~~~~~~~~~

The majority of respondents supported a later implementation date, citing the following
reasons:

* **Procurement and system readiness:** Many authorities are still using paper-based systems or have not yet procured D-TRO-compliant software.

* **Training and staffing:** Respondents highlighted the need for time to train staff and adjust internal processes.

* **Budget alignment:** Several authorities noted that October aligns better with financial planning cycles.

* **Integration with Street Manager:** Authorities expressed concern about the lack of integration between D-TRO and existing systems, particularly for temporary orders.

* **Administrative burden:** A phased or advisory rollout was suggested to reduce pressure and allow for gradual adoption.

Some authorities indicated they were already using digital systems and could comply 
earlier but still supported a later date to ensure sector-wide readiness.

Government Response
~~~~~~~~~~~~~~~~~~~

The Government has decided to delay the commencement date to 11 February 2027. This revised timeline reflects the clear majority preference expressed during engagement 
for a later start, allowing more time for authorities to prepare adequately for 
implementation.

The additional lead-in period is intended to support a smoother and more coordinated 
transition, giving local authorities and stakeholders the opportunity to procure necessary systems, train staff, and establish internal processes to ensure full compliance with the new requirements. By extending the timeline, the Government aims to reduce the risk of non-compliance, data inaccuracies, and operational disruption, particularly for those authorities facing resource constraints or complex integration challenges.

The delay also promotes greater consistency across the sector, helping to ensure that all authorities are working to the same standards and expectations from the outset. To further support implementation, the Government will issue non statutory guidance and provide access to worked examples through GitHub ahead of the commencement date. 

This non-statutory guidance will clarify operational expectations, provide technical support, and outline options for voluntary early submission for those authorities that are ready to begin implementation ahead of the formal start date.

Section 2:  Required Data for Traffic Regulation Measures (TRMs)
----------------------------------------------------------------

Relevant Questions
~~~~~~~~~~~~~~~~~~

Q7: Do you agree or disagree that the list of information required in respect of a traffic regulation measure is the correct data to include?

Q8: Do you think certain information required in respect of a traffic regulation measure should be: Changed in the list; added to the list or removed from the list?
Q9-Q11: What do you think should be changed, added, or removed? Why?

Q12: Why do you agree or disagree?

Purpose of the Section
~~~~~~~~~~~~~~~~~~~~~~

To assess whether the proposed list of data fields for traffic regulation measures (TRMs) is  appropriate, sufficient, and practical for authorities to provide digitally.

Summary of Responses
~~~~~~~~~~~~~~~~~~~~

Q7
~~

.. list-table::
   :header-rows: 1
   :widths: 70 30

   * - Response
     - Number of Respondents
   * - Agree
     - 57
   * - Disagree
     - 26
   * - Don’t know
     - 10

Q8
~~

.. list-table::
   :header-rows: 1
   :widths: 60 20 20

   * - Response
     - Yes
     - No
   * - Changed in the list
     - 12
     - 81
   * - Removed from the list
     - 12
     - 79
   * - Added to the list
     - 12
     - 78

Consultation Feedback
~~~~~~~~~~~~~~~~~~~~~

Most respondents agreed that the proposed list of data fields was broadly appropriate. 
However, several key themes emerged:

* **Clarification of terminology:** Respondents requested clearer definitions for terms such as “made,” “coming into force,” and “activation” dates, noting that these can differ in practice.

* **Expiration dates:** Many authorities felt that expiration dates should be explicitly included, especially for temporary orders.

* **Applicability and relevance:** Concerns were raised about the relevance of certain 
fields for permanent orders, such as diversion routes and traffic management details.

* **Burden of data provision:** Some authorities highlighted the administrative burden of providing detailed data manually, especially where systems are not yet integrated.

* **Digital readiness:** Authorities using paper-based systems expressed concern about 
their ability to comply without significant investment in digital tools.

Government Response
~~~~~~~~~~~~~~~~~~~

The Government has amended Regulation 4(2) to address these concerns:

* **Date fields clarified:** To improve clarity, reduce administrative burden, and support practical implementation. Authorities are now permitted to include key date fields such as “made,” “coming into force,” and “activation” dates, where applicable, ensuring greater transparency and alignment with operational practices

* **Expiration dates included:** These are now explicitly permitted in the regulation.

* **Relevance principle introduced:** To reduce unnecessary data entry, a new relevance principle has been introduced, meaning that fields are only required “so far as relevant,” especially in cases where certain details—such as diversion routes or traffic management plans—may not apply to permanent orders

* **Guidance to support implementation:** Non-statutory guidance will clarify expectations and authorities will be able to view examples on GitHub to help them interpret and apply the data requirements consistently.

These changes aim to balance the need for comprehensive digital records with the 
practical realities faced by traffic regulation authorities.

Section 3: Required Data for Each provision
-------------------------------------------

Relevant Questions
~~~~~~~~~~~~~~~~~~

Q13: Do you agree or disagree that the list of information required in respect of each 
provision of a TRM is the correct data to include?

Q14: Do you think certain information required in respect of each provision of a TRM 
should be: changed in the list; added to the list or removed from the list?

Q15-Q17: What do you think should be changed, added, or removed? Why?

Q18: Why do you agree or disagree?

Purpose of the Section
~~~~~~~~~~~~~~~~~~~~~~

To assess whether the proposed provision-level data fields — such as location, timing, 
and diversion routes — are appropriate and practical for authorities to provide digitally.

Summary of Responses
~~~~~~~~~~~~~~~~~~~~

Q13
~~~

.. list-table::
   :header-rows: 1
   :widths: 70 30

   * - Response
     - Number of Respondents
   * - Agree
     - 57
   * - Disagree
     - 17
   * - Don’t know
     - 19

Q14
~~~

.. list-table::
   :header-rows: 1
   :widths: 60 20 20

   * - Response
     - Yes
     - No
   * - Changed in the list
     - 10
     - 83
   * - Removed from the list
     - 7
     - 83
   * - Added to the list
     - 3
     - 87

Consultation Feedback
~~~~~~~~~~~~~~~~~~~~~

There was strong support for the inclusion of provision-level data, with respondents 
recognising its importance for clarity and enforcement. However, several concerns were 
raised:

* **Relevance for permanent orders:** Some fields, such as diversion routes, were seen 
as unnecessary for permanent TRMs.

* **Complexity of data**: Authorities noted that some provisions (e.g. multiple USRNs or geospatial references) may be difficult to provide, especially for complex or multi-site orders.

* **Digital capability:** Respondents using paper-based systems expressed concern 
about the feasibility of providing detailed provision-level data without significant 
investment.

* **Need for guidance:** Authorities requested examples and clarification on how to 
interpret and apply provision-level requirements, particularly for less common 
scenarios.

Government Response
~~~~~~~~~~~~~~~~~~~

The Government has retained the full list of provision-level data in Regulation 4(3), but introduced the following:

* **“So far as applicable” clause:** This ensures that authorities are required to submit complete and accurate data that is applicable to the specific TRM. This means, for example, that detailed diversion route information would not be expected for permanent orders where such data is not relevant. The clause is designed to reduce unnecessary burden while maintaining the integrity and usefulness of the data submitted.

* **Guidance and worked examples to support interpretation:** To support implementation, the DfT will issue non-statutory guidance that will provide clarification on when fields are "relevant". Authorities will also be able to view examples on GitHub that will help them understand how to apply provision-level requirements, especially for permanent orders.

* **Support for digital transition:** Authorities are encouraged to adopt digital systems if they have not done so already and move away from paper-based systems. The
Government will continue working with digital solution providers to ensure 
compatibility and ease of use, ensuring that provision-level data can be entered and 
updated easily and systems support phased data entry and validation.

These changes aim to ensure that provision-level data enhances transparency and 
usability without imposing undue burden on authorities, ensuring a smooth transition.

Section 4: Conditions and Exceptions
------------------------------------

Relevant Questions
~~~~~~~~~~~~~~~~~~

Q19: Do you agree or disagree that the list of information required in respect of conditions attached to a TRM is the most correct data to include?

Q20-Q23: Should any data be changed, added, or removed? Why?

Q24: Why do you agree or disagree?

Purpose of the Section
~~~~~~~~~~~~~~~~~~~~~~

To evaluate whether the proposed list of conditions and exceptions — such as vehicle 
types, environmental factors, and user characteristics — is appropriate and sufficient for digital submission.

Summary of Responses
~~~~~~~~~~~~~~~~~~~~

Q19
~~~

.. list-table::
   :header-rows: 1
   :widths: 70 30

   * - Response
     - Number of Respondents
   * - Agree
     - 65
   * - Disagree
     - 13
   * - Don't know
     - 15

Q20
~~~

.. list-table::
   :header-rows: 1
   :widths: 60 20 20

   * - Response
     - Yes
     - No
   * - Changed in the list
     - 7
     - 85
   * - Removed from the list
     - 7
     - 84
   * - Added to the list
     - 2
     - 88

Consultation Feedback
~~~~~~~~~~~~~~~~~~~~~

Respondents broadly supported the inclusion of conditions and exceptions, recognising their importance for enforcement and clarity. However, several key points were raised:

* **Additional condition types:** Respondents suggested including restrictions for vulnerable road users and environmental factors (e.g. tidal conditions, weather).

* **Practicality of enforcement:** Some authorities questioned how certain conditions (e.g. fuel type, emissions standards, passenger characteristics) could be monitored or enforced in practice.

* **Clarity and flexibility:** Authorities requested clearer definitions and flexibility to specify local conditions not covered in the standard list.

* **Digital compatibility:** Concerns were raised about whether existing systems could accommodate the full range of condition types.

Government Response
~~~~~~~~~~~~~~~~~~~

The Government has confirmed that Regulation 5 will allow authorities to specify any relevant conditions or exceptions. To support this:

* **Expanded guidance:** Authorities will be able to view examples of common and complex conditions on GitHub, including weather-related restrictions and exclusions for vulnerable users.

* **Flexibility retained:** Authorities may include additional conditions beyond those listed, provided they are relevant and clearly defined. The "so far as relevant" clause ensures that authorities only need to submit data that applies to the specific regulation measure. For example, if an authority does not use emissions-based restrictions, no data entry is required for that field.

* **Digital support:** The D-TRO service has been designed to accommodate a wide range of condition types, including those used by authorities with advanced schemes such as clean air zones or low-emission vehicle restrictions. The service is being built to be system agnostic and the Government will continue working with digital solution providers to ensure compatibility and ease of use.

These measures aim to ensure that TRMs remain adaptable to local needs while 
maintaining consistency and clarity across the national network

Section 5: Missing Information in Draft Regulations
---------------------------------------------------

Relevant Question
~~~~~~~~~~~~~~~~~

Q25: In your view, what, if any, information is missing and should be included in the draft regulations?

Purpose of the Section
~~~~~~~~~~~~~~~~~~~~~~

To identify any gaps in the proposed regulations and assess whether additional provisions or data fields should be included to ensure completeness, clarity, and operational effectiveness.

Summary of Feedback
~~~~~~~~~~~~~~~~~~~

Respondents provided a range of suggestions and concerns regarding missing or unclear elements in the draft regulations:

* **Additional legislative references:** Several authorities suggested including
  provisions under:

  * Section 21 of the Town Police Clauses Act 1847 (used for event-related
    closures)
  * Section 45 of the Road Traffic Regulation Act 1984 (parking places)
  * Sections 32–35 (free and paid parking bays)
  * Section 22 (ATTROs – anti-terrorism traffic regulation orders)

* **Clarification of scope:** Authorities requested clearer guidance on:

  * Whether the regulations apply to public rights of way (PROWs), footpaths,
    and bridleways
  * How to handle orders that span multiple jurisdictions or affect roads
    managed by other authorities

* **Digital identifiers and mapping:**

  * Some respondents questioned the mandatory use of Unique Street Reference
    Numbers (USRNs), especially where they do not exist (e.g. for PROWs or
    alleyways)
  * Others requested clearer definitions for geospatial data, such as grid
    references and coordinate formats

* **Diversion routes and charges:**

  * Concerns were raised about the practicality of listing full diversion
    routes, especially for complex or multi-site closures
  * Some questioned the inclusion of “charges” in the data model, asking
    whether this refers to application fees, tolls, or enforcement penalties

* **Operational clarity:**

  * Respondents asked for clearer definitions of “activation” dates and how
    they differ from “coming into force”
  * Authorities requested guidance on how to handle orders that are amended
    after being made, and whether full re-submission is required
  
Government Response
~~~~~~~~~~~~~~~~~~~

The Government acknowledges the feedback and has taken the following steps:

* **Scope clarification:**

  * The regulations will remain focused on TRMs under the Road Traffic Regulation
    Act 1984.
  * Voluntary submission of other orders (e.g. under Section 21 or Section 45) will
    be encouraged and will be supported in guidance.

* **Mapping and identifiers:**

  * Regulation 4(3)(n) retains the requirement for USRNs but clarifies that they are
    required only “where relevant.”
  * GitHub will provide examples of how to handle cases where USRNs are unavailable,
    and clarify acceptable formats for geospatial data.

* **Diversion routes and charges:**

  * Diversion route data will be required only for temporary orders and “so far as
    relevant.”
  * The term “charges” will be clarified in guidance and does not include
    administrative costs.

* **Handling amendments:**

  * Authorities making minor amendments will be able to re-submit amended orders
    using the same system generated order identifier, replacing the older order
    record, and the original order will be marked as not live.
  * Regulation 10 introduces a duty to maintain accurate data, with corrections
    required within two working days.

These changes aim to ensure the regulations are clear, practical, and adaptable to the diverse operational contexts of traffic regulation authorities.

Section 6: Use of Unique Street Reference Numbers (USRNs)
---------------------------------------------------------

Relevant Question
~~~~~~~~~~~~~~~~~

Q26: Should we be asking for the Unique Street Reference Number (USRN) to be 
supplied where it exists?

Q27: Why?

Purpose of the Section
~~~~~~~~~~~~~~~~~~~~~~

To assess whether the inclusion of USRNs — a nationally standardised identifier for 
streets — should be mandatory in digital traffic regulation submissions, and to understand the implications for authorities and data users.

Summary of Responses
~~~~~~~~~~~~~~~~~~~~

Q26:
~~~~

.. list-table::
   :header-rows: 1
   :widths: 70 30

   * - Response
     - Number of Respondents
   * - Yes
     - 60
   * - No
     - 18
   * - Don’t know
     - 15

Consultation Feedback
~~~~~~~~~~~~~~~~~~~~~

The majority of respondents supported the inclusion of USRNs, citing benefits for 
accuracy, interoperability, and integration with existing systems. Key themes included:

* **Benefits of USRNs:**

  * Widely used in systems such as Street Manager and the National Street
    Gazetteer.
  * Helps avoid ambiguity, especially for roads with similar names.
  * Facilitates integration with mapping tools and digital platforms.

* **Concerns and caveats:**

  * Some authorities noted that USRNs may not exist for certain types of routes,
    such as public rights of way (PROWs), alleyways, or off-street locations.
  * Manual entry of USRNs could be burdensome, especially for complex or
    multi-site orders.
  * A few respondents questioned the public relevance of USRNs, suggesting they
    are more useful for internal systems than for public-facing data.

* **Suggestions:**

  * USRNs should be required only “where they exist.”
  * Systems should automate USRN inclusion to reduce manual workload.
  * Guidance should clarify how to handle cases with multiple USRNs or where
    none are available.

Government Response
~~~~~~~~~~~~~~~~~~~

The Government has confirmed that Regulation 4(3)(n) will retain the requirement for USRNs, with the following clarifications:

* **Conditional requirement:** USRNs will be required only “where relevant” — i.e., where they exist and apply to the road or provision in question.

* **Examples and guidance support:** GitHub will provide examples of how to handle multiple-USRN routes and edge cases, and non statutory guidance will clarify that USRNs are not required for routes without identifiers (e.g. certain Public Rights of Way).

* **Interoperability focus:** The inclusion of USRNs supports the broader goal of creating a consistent, digital dataset for use by automated vehicles, mapping services, and transport digital solution providers.

These measures aim to ensure that USRNs enhance data quality and usability without 
creating unnecessary administrative burden

Section 7: Actual Start and Stop Times
--------------------------------------

Relevant Questions
~~~~~~~~~~~~~~~~~~

Q28: In your view, should we be asking for actual starts and stops to be supplied by
authorities so that road users know when restrictions are in place?

Q29: Why?

Purpose of the Section
~~~~~~~~~~~~~~~~~~~~~~

To assess whether traffic regulation authorities (TRAs) should be required to submit real-time data on when temporary traffic regulation measures (TRMs) begin and end, and to understand the feasibility and implications of this requirement.

Summary of Responses
~~~~~~~~~~~~~~~~~~~~

Q28:
~~~~

.. list-table::
   :header-rows: 1
   :widths: 70 30

   * - Response
     - Number of Respondents
   * - Yes
     - 45
   * - No
     - 38
   * - Don't know
     - 10

Consultation Feedback
~~~~~~~~~~~~~~~~~~~~~

Responses were mixed, with a slight majority opposing the requirement. Key themes 
included:

* **Support for transparency:**

  * Respondents who supported the proposal cited the value of accurate, real-time
    data for road users, automated vehicles, and journey planning tools.
  * Some authorities already link TTROs to permit systems and felt this could be
    extended to D-TRO.

* **Concerns about feasibility:**

  * Many authorities noted that actual start/stop times are often unknown in
    advance and subject to change due to weather, contractor delays, or
    emergency works.
  * Utility companies and event organisers are not currently required to notify
    TRAs of precise timings, making manual tracking difficult.
  * Several respondents suggested that this data should come from Street
    Manager, which already collects permit timing information.

* **Resource implications:**

  * Authorities warned that tracking and updating start/stop times manually would
    require dedicated staff and weekend coverage, which is not currently
    resourced.

Government Response
~~~~~~~~~~~~~~~~~~~

The Government recognises the importance of accurate timing data but acknowledges the concerns raised. As a result:

* Regulation 7 introduces the requirement for actual start/stop times but delays
  its commencement until 1 October 2028.

* This delay allows time for:

  * Integration with Street Manager and other systems.
  * Development of automated data-sharing processes.
  * Authorities to prepare operationally and financially.

* Guidance will clarify:

  * That the requirement applies only to TRAs (not contractors or utility
    companies).
  * How to handle phased or multi-stage works.
  * Acceptable formats and update procedures.

Section 8: Timing of Submissions to D-TRO
-----------------------------------------

Relevant Questions
~~~~~~~~~~~~~~~~~~

Q30: Do you agree or disagree that the proposed timings for sending the
information to D-TRO are clear and appropriate?

Q31: Why?

Purpose of the Section
~~~~~~~~~~~~~~~~~~~~~~

To evaluate whether the proposed submission deadlines — including for proposed and 
made orders, and real-time updates — are realistic and achievable for authorities.

Summary of Responses
~~~~~~~~~~~~~~~~~~~~

Q30:
~~~~

.. list-table::
   :header-rows: 1
   :widths: 70 30

   * - Response
     - Number of Respondents
   * - Agree
     - 26
   * - Disagree
     - 49
   * - Don't know
     - 17

Consultation Feedback
~~~~~~~~~~~~~~~~~~~~~

While most respondents found the timings clear, many raised concerns about feasibility:

* **Emergency and weekend operations:**

  * Authorities noted that emergency works often occur outside office hours,
    making it difficult to meet submission deadlines (e.g. within two hours or
    by 10am the next day).
  * Weekend coverage is not standard in most authorities.

* **Administrative burden:**

  * Respondents warned that the proposed timings would require significant
    staffing and system changes.
  * Some suggested aligning D-TRO timings with permit system workflows to
    reduce duplication.

* **Need for flexibility:**

  * Authorities requested the ability to update data retrospectively or in
    batches, especially for complex or multi-phase works.

Government Response
~~~~~~~~~~~~~~~~~~~

The Government has retained the proposed timings in Regulation 9, but introduced the following mitigations:

* **Flexibility for updates:** Authorities may update activation dates and other fields after initial submission.

* **Delayed commencement for real-time requirements:** As noted in Section 7, real-time start/stop reporting will not be mandatory until October 2028.

* **Guidance will clarify:** The guidance references out to detailed technical guidance, which may be altered from time to time, to the D-TRO web portal and the documentation and artifacts it contains.

These changes aim to ensure timely data submission while recognising operational 
constraints.

Section 9: Submission at Proposed vs. Made Stage
------------------------------------------------

Relevant Questions
~~~~~~~~~~~~~~~~~~

Q32: Your view is that the required information should be sent when TRMs undersection 1 of the 1984 Act are: proposed, made or proposed and made. Why?

Q33: Your view is that the required information should be sent when TRMs undersection 6 of the 1984 Act are: proposed, made or proposed and made. Why?

Q34: Your view is that the required information should be sent when TRMs under
section 84 of the 1984 Act are proposed, made or proposed and made. Why?

Purpose of the Section
~~~~~~~~~~~~~~~~~~~~~~

To determine whether authorities should submit data to D-TRO at the proposal stage, the made stage, or both — and to understand the implications for transparency,  workload, and data accuracy.

Summary of Responses
~~~~~~~~~~~~~~~~~~~~

Q32:
~~~~

.. list-table::
   :header-rows: 1
   :widths: 70 30

   * - Stage Preference
     - Number of Respondents
   * - Proposed only
     - 3
   * - Made only
     - 56
   * - Proposed and made
     - 28

Q33:
~~~~

.. list-table::
   :header-rows: 1
   :widths: 70 30

   * - Stage Preference
     - Number of Respondents
   * - Proposed only
     - 4
   * - Made only
     - 46
   * - Proposed and made
     - 30

Q34:
~~~~

.. list-table::
   :header-rows: 1
   :widths: 70 30

   * - Stage Preference
     - Number of Respondents
   * - Proposed only
     - 4
   * - Made only
     - 52
   * - Proposed and made
     - 34

Consultation Feedback
~~~~~~~~~~~~~~~~~~~~~

Opinions were divided, with a majority preferring submission only at the “made” stage. Key points included:

* **Support for “made only”:**

  * Authorities argued that proposed orders may change or be withdrawn, leading
    to confusion or duplication.
  * Submitting at the made stage ensures accuracy and reflects legal status.

* **Support for “proposed and made”:**

  * Some respondents felt that early visibility supports transparency and public
    engagement.
  * Useful for automated vehicles and mapping services to anticipate upcoming
    changes.

* **Concerns about duplication:**

  * Submitting at both stages could increase workload, especially if proposals
    are amended or abandoned.

Government Response
~~~~~~~~~~~~~~~~~~~

The Government has decided that while the submission of measures at the made stage 
will be mandatory, the submission of measures at the proposed stage will be on a 
voluntary basis only. **Voluntary submission of proposed measures will still be 
supported.**

* Authorities may still submit proposed TRMs to the D-TRO platform voluntarily and this will be clarified in the accompanying guidance.

This approach ensures legal compliance while still enabling authorities to benefit from early data sharing where feasible.

Section 10: Other Comments
--------------------------

Relevant Question
~~~~~~~~~~~~~~~~~

Q35: Any other comments?

Purpose of the Section
~~~~~~~~~~~~~~~~~~~~~~

To capture additional feedback, concerns, and suggestions not covered by specific 
questions.

Summary of Feedback
~~~~~~~~~~~~~~~~~~~

Respondents raised a wide range of issues, including:

* **Guidance:**

  * Strong support for detailed guidance to support implementation, clarify
    responsibilities, and ensure consistency.

* **Funding and resources:**

  * A minority of authorities requested financial support for software
    procurement, staffing, and training.
  * Concerns about affordability and sustainability, especially for smaller or
    rural authorities.

* **System integration:**

  * Calls for integration with Street Manager and other platforms to reduce
    duplication and improve accuracy.

* **Enforcement and responsibilities:**

  * Requests for clarity on who is responsible for data accuracy, especially
    for temporary orders.
  * Suggestions to shift some responsibilities to works promoters.

* **Digital format and accessibility:**

  * Mixed views on the JSON schema; some preferred tabular or GIS formats.
  * Requests for open-source tools and standardised templates.

Government Response
~~~~~~~~~~~~~~~~~~~

The Government has committed to the following actions:

* **Non Statutory Guidance:** Will be issued alongside the regulations to support implementation and clarify expectations. This will also include Cabinet Office guidelines regarding best practice for managing geospatial data.

* **System development:** Continued work with digital solution providers to ensure compatibility and ease of use and development of a service that is system agnostic.

* **Clarification of duties:** Regulation 10 establishes a duty to maintain accurate data, with corrections required within two working days.

* **Open data principles:** D-TRO will remain free to use and accessible, supporting innovation and public benefit.

These measures aim to ensure successful implementation and long-term sustainability of the D-TRO system.

Summary of Next Steps
---------------------

The Government is grateful to all stakeholders who responded to the consultation and engaged with the development of the Digital Traffic Regulation Orders (D-TRO) service. The feedback received has been key in shaping the final regulations and ensuring they are practical, proportionate, and aligned with the needs of traffic regulation authorities and road users.

Based on the consultation responses, the Government intends to proceed with the 
following:

* **Next Steps / Commencement Date**

  The regulations will come into force on 11 February 2027, allowing sufficient time for authorities to prepare and align systems. We encourage authorities to begin submitting orders voluntarily during Public Beta, ahead of the mandatory requirement, to support testing and ensure readiness.

* **Phased Implementation of Start/Stop Times**
  
  The requirement to report actual start and stop times for section 14 orders will be delayed until October 2028, enabling integration with Street Manager and reducing administrative burden.

* **Expanded Date Reporting**
  
  Authorities will be required to submit the made date, coming into force date, activation date (if different), and expiration date where relevant, to improve clarity and support real-time data use.

* **Scope and Flexibility of Data Fields**
  
  The regulations clarify that data fields are required only where relevant, and non-statutory guidance will support interpretation for different types of TRMs.

* **Retention of USRN Requirements**
  
  Unique Street Reference Numbers (USRNs) will be retained in the regulations, with flexibility for cases where they are not available.

* **Conditions and Exceptions**
  Authorities will be able to specify conditions and exceptions, including those related to vulnerable road users and environmental factors. The D-TRO Guidance references out to detailed technical guidance, which may be altered from time to time, to the D-TRO web portal and the documentation, artifacts and examples it contains.

* **Accuracy and Updates**

  Authorities must correct inaccurate data within two working days of becoming aware of the issue, ensuring the reliability of published information.

* **Guidance and examples**
  The DfT will issue non-statutory guidance to support implementation, including examples that will be available through GitHub. Advice on voluntary data submissio will also be provided.

* **Voluntary Submission of Historical Data**
  Authorities may submit data from older TRMs voluntarily, provided it complies with the D-TRO data specification.

* **Support for Authorities**
  The Government will continue to engage with authorities and digital solution providers to support system integration and ensure readiness ahead of the commencement date.

The Government looks forward to working with traffic regulation authorities, digital solution providers, and stakeholders to ensure successful implementation of the regulations and to realise the full benefits of a modern, digital approach to traffic regulation across England.