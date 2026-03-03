Large D-TRO Guidance
====================

This section provides advice on the submission of large payloads to the D-TRO service.

Background
^^^^^^^^^^

As the D-TRO service matures, it is seeing larger and larger payloads being submitted. The vast majority of submitted orders are very small, and pose no problems during submission. However, payload size is skewed by the large number of submitted temporary orders; permanent and consultation orders are comparatively rare, and tend to be much, much larger in size.

The service itself has a fixed, maximum body/file size of 10MB. Payloads that exceed this limit cannot be submitted to the service, and must be compressed to below this limit in order to be submitted. The service provides a mechanism for submitting gzip-compressed files (see section :ref:`gzip-upload` for details).

However, although gzip compression may allow a file exceeding 10MB to be compressed to something smaller and sent to the server, the server must still decompress this on the other end, before performing schema validation, code-side validation, metadata parsing and saving to the database. For large payload sizes, this can consume large amounts of memory and resources, and lead to container exhaustion and ultimately failures in submissions.

Solutions
^^^^^^^^^

Often, retrying the submission is the easiest first step in successfully submitting large payloads. The success of submission is dependant on what else is happening in the service; at periods of low usage, more resources can be dedicated to the processing of large D-TROs, while at periods of high usage there is less resource available. Therefore, careful consideration of when to submit large D-TROs can help yield more successful submissions (e.g. during the early hours of the morning, when traffic is low).

Future-proofing
^^^^^^^^^^^^^^^

Retrying failed submissions is not a long-term solution to this problem, and the DfT are actively investigating a robust and scalable solution. This may include core architecture changes to the service around how D-TROs are stored, and how clients publish to/consume from the service. The DfT has established the Large D-TRO Working Group to assist in this process, and will provide timely updates as necessary to support clients with the changes required once the solution is defined and developed.