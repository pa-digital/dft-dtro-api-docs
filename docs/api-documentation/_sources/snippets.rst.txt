Snippets
========

This section contains various JSON data snippets which illustrate typical ways in which we would expect different forms of TRO provisions to be coded. In each case, we also provide a full D-TRO example file which mirrors the contwent of the related snippet.

For brevity, the symbol ``...`` is used to indicate several lines in the JSON snippets.

We also include some explanatory notes, which are not replicated in the example files.

Generally, the patterns found in the JSON content of these snippets and examples varies by the form of location referencing mechanism that has been used (``pointLocation``, ``linearLocation``, ``polygon``, ``directedLinear``) and also with the forms of conditions that may be applicable.

These snippets and examples are, by their nature, illustrative.

The circumstances of specific D-TRO provisions may require adjustments to the approach used.

The snippets and examples have been organised into the following groups:

* Group 1 - Specific movement with condition
* Group 2 - Restriction with measurement condition 
* Group 3 - Kerbside regulations represented using a linear location (no specific direction influence)
* Group 4 - Regulations representing roads or parts of roads with some directional influence - modelled as a linear location
* Group 5 - Regulations representing roads or parts of roads or zones - modelled as a polygon
* Group 6 - Regulations representing roads or parts of roads or zones - modelled as a point

Group 1 - Specific movement with condition
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

regulationTypes:

* `bannedMovementNoEntry`
* `bannedMovementNoLeftTurn`
* `bannedMovementNoRightTurn``
* `bannedMovementNoUTurn`
* `mandatoryDirectionAheadOnly`
* `mandatoryDirectionLeftTurnOnly`
* `mandatoryDirectionOneWay`
* `mandatoryDirectionRightTurnOnly`

Example snippet 1: `bannedMovementNoUTurn`

`Full snippet <#>`_

.. code-block:: json

   {
     "actionType": "new",
     "orderReportingPoint": "permanentNoticeOfMaking",
     "provisionDescription": "Banned U turn - made up - Holland Park Avenue (W) to Holland Park Avenue (E)",
     "reference": "b1618e6f-f65c-48c7-9cc7-45da9f45fbdc",
     "comingIntoForceDate": "2025-01-01",
     "regulatedPlace": [
       {
         "description": "Holland Park Avenue (W) to Holland Park Avenue (E)",
         "type": "regulationLocation",
         "directedLinear": {
           "version": 1,
           "directedLineString": "SRID=27700;LINESTRING(524811 180305, 524804 180305, 524797 180315)",
           // Banned turns are spatially defined by a set of coordinates from origin to destination
           "origin": [
             {
               "lastUpdateDate": "2024-10-01T00:00:00",
               "uniqueStreetReferenceNumber": [
                 { "usrn": 21701239 }
                 // ... more USRNs if applicable
               ]
             }
           ],
           "destination": [
             {
               "lastUpdateDate": "2024-10-01T00:00:00",
               "uniqueStreetReferenceNumber": [
                 { "usrn": 21701239 }
                 // ... more USRNs if applicable
               ]
             }
           ],
           "intermediateLocation": [
             {
               "lastUpdateDate": "2024-10-01T00:00:00",
               "uniqueStreetReferenceNumber": [
                 { "usrn": 21700912 }
                 // ... more USRNs if applicable
               ]
             }
           ]
         }
       }
     ],
     "regulation": [
       {
         "condition": [
           {
             "timeValidity": {
               "start": "2024-10-22T06:00:00"
               // ... end time or recurrence if applicable
             }
           }
         ],
         "generalRegulation": {
           "regulationType": "bannedMovementNoUTurn"
         },
         "isDynamic": false,
         "timeZone": "Europe/London"
       }
     ],
     ...
   }


Example snippet 2: `mandatoryDirectionAheadOnly`

`Full snippet <#>`_

.. code-block:: json

   {
     ...
     "provision": [
       {
         "actionType": "new",
         "orderReportingPoint": "permanentNoticeOfMaking",
         "provisionDescription": "Mandatory Direction Ahead Only, Bagshot Road, Bracknell",
         "reference": "b1618e6f-f65c-48c7-9cc7-45da9f45fbdc",
         "comingIntoForceDate": "2025-01-01",
         "regulatedPlace": [
           {
             "description": "Bagshot Road, Bracknell, northbound",
             "type": "regulationLocation",
             "directedLinear": {
               // Using directedLinear to define location with origin and destination USRNs
               "version": 1,
               "directedLineString": "SRID=27700;LINESTRING(487226 168010, 487224 168054)",
               "origin": [
                 {
                   "lastUpdateDate": "2024-10-01T00:00:00",
                   "uniqueStreetReferenceNumber": [
                     { "usrn": 3800068 }
                   ]
                 }
               ],
               "destination": [
                 {
                   "lastUpdateDate": "2024-10-01T00:00:00",
                   "uniqueStreetReferenceNumber": [
                     { "usrn": 3800068 }
                     // ... more USRNs if applicable
                   ]
                 }
               ]
             }
           }
         ],
         "regulation": [
           {
             "condition": [
               {
                 "timeValidity": {
                   "start": "2024-10-22T06:00:00"
                   // ... end time or recurrence if applicable
                 }
               }
             ],
             "generalRegulation": {
               "regulationType": "mandatoryDirectionAheadOnly"
             },
             "isDynamic": false,
             "timeZone": "Europe/London"
           }
         ]
       }
     ]
   }

Group 2 - Restriction with measurement condition
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The following regulation types follow a similar approach with specific vehicle characteristics:

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - Regulation Type
     - Associated Condition
   * - dimensionMaximumHeightWithTRO
     - vehicleCharacteristics - maximumHeightCharacteristic (vehicleHeight)
   * - dimensionMaximumLength
     - vehicleCharacteristics - maximumLengthCharacteristic (vehicleLength)
   * - dimensionMaximumWeightEnvironmental
     - vehicleCharacteristics - maximumGrossWeightCharacteristic (grossVehicleWeight)
   * - dimensionMaximumWeightStructural
     - vehicleCharacteristic - maximumGrossWeightCharacteristic (grossVehicleWeight)
   * - dimensionMaximumWidth
     - vehicleCharacteristic - maximumWidthCharacteristic (vehicleWidth)

Example snippet 1: `dimensionMaximumHeightWithTRO`

`Full snippet <#>`_

.. code-block:: json

   {
     "actionType": "new",
     "orderReportingPoint": "ttroTtmoNoticeOfIntention",
     "provisionDescription": "Temporary height restriction (2.5m)",
     "reference": "c962b51f-e1aa-416e-8f0b-aefe39a4c099",
     "comingIntoForceDate": "2025-01-01",
     "regulatedPlace": [
       {
         "description": "East Reach - Taunton",
         "type": "regulationLocation",
         "pointGeometry": {
           "externalReference": [
             {
               "lastUpdateDate": "2024-08-01T00:00:00",
               "uniqueStreetReferenceNumber": [
                 { "usrn": 39608173 }
               ]
             }
           ],
           "point": "SRID=27700;POINT(323544 124622)",
           "representation": "centreLinePoint",
           "version": 1
         }
       }
     ],
     "regulation": [
       {
         "conditionSet": [
           {
             "operator": "and",
             "conditions": [
               {
                 "negate": false,
                 "timeValidity": {
                   "start": "2024-08-22T08:00:00",
                   "end": "2024-08-22T20:00:00"
                 }
               },
               {
                 "negate": false,
                 "vehicleCharacteristics": {
                   "maximumHeightCharacteristic": {
                     "vehicleHeight": 2.5
                     // ... additional characteristics if needed
                   }
                 }
               }
             ]
           }
         ],
         "generalRegulation": {
           "regulationType": "dimensionMaximumHeightWithTRO"
         },
         "isDynamic": false,
         "timeZone": "Europe/London"
       }
     ],
     ...
   }


Group 3 - Kerbside regulations represented using a linear location (no specific direction influence)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

regulationType:

*	`kerbsideDisabledBadgeHoldersOnly`	
*	`kerbsideDoubleRedLines`	
*	`kerbsideFootwayParking`	
*	`kerbsideFootwayParkingProhibited`	
*	`kerbsideLimitedWaiting`	
*	`kerbsideLoadingBay`	
*	`kerbsideLoadingBayPassengerSetDownPermitted`	
*	`kerbsideLoadingBayPassengerSetDownProhibited`	
*	`kerbsideLoadingPlace`	
*	`kerbsideLoadingPlacePassengerSetDownPermitted`	
*	`kerbsideLoadingPlacePassengerSetDownProhibited`	
*	`kerbsideMotorcycleParkingPlace`	
*	`kerbsideNoLoading`	
*	`kerbsideNoLoadingPassengerSetDownPermitted`	
*	`kerbsideNoLoadingPassengerSetDownProhibited`	
*	`kerbsideNoStopping`	
*	`kerbsideNoWaiting`	
*	`kerbsideOtherYellowZigZagMandatory`	
*	`kerbsideParkingPlace`	
*	`kerbsidePermitParkingArea`	
*	`kerbsidePermitParkingPlace`	
*	`kerbsideRedRouteClearway`	
*	`kerbsideRestrictedParkingZone`	
*	`kerbsideRuralClearway`	
*	`kerbsideSchoolKeepClearYellowZigZagMandatory`	
*	`kerbsideSingleRedLines`	
*	`kerbsideTaxiRank`	
*	`kerbsideUrbanClearway`
*	`miscBaySuspension`
* 	`miscSuspensionOfParkingRestriction`
*	`miscSuspensionOfWeightRestriction`
*	`miscTemporaryParkingRestriction`

Example snippet: `kerbsidePaymentParkingPlace`

`Full snippet <#>`_

.. code-block:: json

   {
     "actionType": "new",
     "orderReportingPoint": "permanentNoticeOfMaking",
     "provisionDescription": "Parking restrictions, East Reach, Pay & Display Parking Places - Monday to Sunday 9.00 am to 8.00 pm",
     "reference": "c962b51f-e1aa-416e-8f0b-aefe39a4c099",
     "comingIntoForceDate": "2024-12-10",
     "regulatedPlace": [
       {
         "description": "East Reach, Taunton, northside / eastbound, between 10 metres east from the junction with Tancred Street to 15 metres west of the junction with South Street {approximate - linear}",
         "concession": false,
         "assignment": false,
         "tramcar": false,
         "busRoute": true,
         "bywayType": "road",
         "linearGeometry": {
           // This example uses a linestring to describe a linear location
           "direction": "bidirectional",
           "representation": "linear",
           "lateralPosition": "onKerb",
           "linestring": "SRID=27700;LINESTRING(323158 124529,323252 124546)",
           "externalReference": [
             {
               "lastUpdateDate": "2024-10-01T00:00:00",
               "uniqueStreetReferenceNumber": [
                 { "usrn": 39608173 }
               ]
             }
           ],
           "version": 1
         },
         "type": "regulationLocation"
       }
     ],
     "regulation": [
       {
         "condition": [
           {
             "negate": false,
             "timeValidity": {
               "start": "2024-12-10T09:00:00",
               "validPeriod": [
                 {
                   // ValidPeriod defines days and times of applicability
                   "recurringDayWeekMonthPeriod": [
                     {
                       "applicableDay": [
                         "monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"
                       ]
                     }
                   ],
                   "recurringTimePeriodOfDay": [
                     {
                       "startTimeOfPeriod": "09:00:00",
                       "endTimeOfPeriod": "20:00:00"
                     }
                   ]
                 }
               ]
             }
           }
         ],
         "generalRegulation": {
           "regulationType": "kerbsidePaymentParkingPlace"
         }
       }
     ],
     ...
   }


Group 4 - Regulations representing roads or parts of roads with some directional influence - modelled as a linear location
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

regulationType:

*	`miscBusLaneWithTrafficFlow`	
*	`miscBusOnlyStreet`	
*	`miscContraflowBusLane`	
*	`miscSuspensionOfBusway`	
*	`miscSuspensionOfOneWay`	
*	`movementOrderPriorityOverOncomingTraffic`
*	`movementOrderNoOvertaking` (linear one way or bidirectional)

Example snippet: `miscBusLaneWithTrafficFlow`

`Full snippet <#>`_

.. code-block:: json

   {
     "actionType": "new",
     "orderReportingPoint": "permanentNoticeOfMaking",
     "provisionDescription": "Bus lane, Corporation Street, Taunton",
     "reference": "c962b51f-e1aa-416e-8f0b-aefe39a4c099",
     "comingIntoForceDate": "2024-12-10",
     "regulatedPlace": [
       {
         "description": "Corporation Street, Taunton {approximate - linear}",
         "concession": false,
         "assignment": false,
         "tramcar": false,
         "busRoute": true,
         "bywayType": "road",
         "linearGeometry": {
           // This example uses a linestring to describe a linear location
           "direction": "startToEnd",
           "representation": "representingZone",
           "lateralPosition": "centreline",
           "linestring": "SRID=27700;LINESTRING(322494 124467,322645 124504,322666 124502)",
           "externalReference": [
             {
               "lastUpdateDate": "2024-10-01T00:00:00",
               "uniqueStreetReferenceNumber": [
                 { "usrn": 39608010 }
                 // ... more USRNs if applicable
               ]
             }
           ],
           "version": 1
         },
         "type": "regulationLocation"
       }
     ],
     "regulation": [
       {
         "condition": [
           {
             "negate": false,
             "timeValidity": {
               "start": "2024-12-10T07:00:00",
               "validPeriod": [
                 {
                   "recurringDayWeekMonthPeriod": [
                     {
                       "applicableDay": [
                         "monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"
                       ]
                     }
                   ],
                   "recurringTimePeriodOfDay": [
                     {
                       "startTimeOfPeriod": "07:00:00",
                       "endTimeOfPeriod": "16:00:00"
                     }
                   ]
                 }
               ]
             }
           }
         ],
         "generalRegulation": {
           "regulationType": "miscBusLaneWithTrafficFlow"
         }
       }
     ],
     ...
   }

Similarly, approaches can be used for regular patterns for other regulation types:

linearLocation with bidirectional effect (i.e. both ways)

regulationType:

*	`miscContraflow`
*	`miscCycleLane`
*	`miscCycleLaneClosure`
*	`miscFootwayClosure`
*	`miscLaneClosure`
*	`miscPROWClosure`
*	`miscRoadClosure`
*	`nonOrderKerbsideBusStop`
*	`publicRightOfWayClosure`

Group 5 - Regulations representing roads or parts of roads or zones - modelled as a polygon
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

regulationType:

*	`kerbsideControlledParkingZone`
*	`miscCongestionLowEmissionZone`
*	`miscPedestrianZone`
*	`nonOrderMovementBoxJunction`
*	`movementOrderProhibitedAccess	 - when modelled as a polygon`
*	`miscTemporaryParkingBay - when modelled as a polygon`

Example snippet: `movementOrderProhibitedAccess`

`Full snippet <#>`_

.. code-block:: json

   {
     "actionType": "new",
     "orderReportingPoint": "permanentNoticeOfMaking",
     "provisionDescription": "Bus and taxi access only, Tower Street and Castle Way, Taunton",
     "reference": "c962b51f-e1aa-416e-8f0b-aefe39a4c099",
     "comingIntoForceDate": "2024-12-10",
     "regulatedPlace": [
       {
         "description": "Tower Street (from the junction with Castle Street to Castle Way) and Castle Way, Taunton {approximate - linear}",
         "concession": false,
         "assignment": false,
         "tramcar": false,
         "busRoute": true,
         "bywayType": "road",
         "polygon": {
           // This example uses a polygon to define an area location
           "polygon": "SRID=27700;POLYGON((322493 124517, 322511 124533, 322570 124558, 322587 124497, 322579 124494, 322565 124545, 322526 124531, 322496 124511, 322493 124517))",
           "externalReference": [
             {
               "lastUpdateDate": "2024-10-01T00:00:00",
               "uniqueStreetReferenceNumber": [
                 { "usrn": 39605980 },
                 { "usrn": 39605591 }
                 // ... more USRNs if applicable
               ]
             }
           ],
           "version": 1
         },
         "type": "regulationLocation"
       }
     ],
     "regulation": [
       {
         "isDynamic": false,
         "timeZone": "Europe/London",
         "generalRegulation": {
           "regulationType": "movementOrderProhibitedAccess"
         },
         "conditionSet": [
           {
             // First-level condition set: AND logic
             "operator": "and",
             "conditions": [
               {
                 // Second-level condition set: OR logic for vehicle types
                 "conditionSet": [
                   {
                     "operator": "or",
                     "conditions": [
                       {
                         "negate": false,
                         "vehicleCharacteristics": {
                           "vehicleType": "taxi"
                         }
                       },
                       {
                         "negate": false,
                         "vehicleCharacteristics": {
                           "vehicleType": "bus"
                         }
                       }
                     ]
                   }
                 ]
               },
               {
                 "negate": false,
                 "timeValidity": {
                   "start": "2024-12-10T08:00:00",
                   "validPeriod": [
                     {
                       "recurringDayWeekMonthPeriod": [
                         {
                           "applicableDay": [
                             "monday", "tuesday", "wednesday", "thursday", "friday", "saturday"
                           ]
                         }
                       ]
                       // ... time period of day if applicable
                     }
                   ]
                 }
               }
             ]
           }
         ]
       }
     ],
     ...
   }

Group 6 - Regulations representing roads or parts of roads or zones - modelled as a point
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

regulationType:

*	`miscRoadClosureCrossingPoint`
*	`ovementOrderProhibitedAccess`
*	`nonOrderKerbsidePedestrianCrossing`
*	`miscTemporaryParkingBay`
*	`miscBusGate`

Example snippet: `miscBusGate`

`Full snippet <#>`_

.. code-block:: json

   {
      ...
     "provision": [
       {
         "actionType": "new",
         "orderReportingPoint": "permanentNoticeOfMaking",
         "comingIntoForceDate": "2025-01-01",
         "provisionDescription": "Bus Lane restriction, Collett Road, Norton Fitzwarren {approximate} with fictitious time restrictions",
         "reference": "c962b51f-e1aa-416e-8f0b-bcfd09a4d089",
         "regulatedPlace": [
           {
             "description": "Collett Road, from 125 metres to 158 metres from the junction with Great Western Way Roundabout {approximate - notational point of effect}",
             "concession": false,
             "assignment": false,
             "tramcar": false,
             "busRoute": false,
             "bywayType": "road",
             "pointGeometry": {
               "externalReference": [
                 {
                   "lastUpdateDate": "2024-10-01T00:00:00",
                   "uniqueStreetReferenceNumber": [
                     { "usrn": 39609234 }
                     // ... more USRNs if applicable
                   ]
                 }
               ],
               "point": "SRID=27700;POINT(320329 126155)",
               "representation": "centreLinePoint",
               "version": 2
             },
             "type": "regulationLocation"
           }
         ],
         "regulation": [
           {
             "conditionSet": [
               {
                 // First-level condition set: AND logic
                 "operator": "and",
                 "conditionSet": [
                   {
                     // Second-level condition set: OR logic for vehicle types
                     "operator": "or",
                     "conditions": [
                       {
                         "negate": true,
                         "vehicleCharacteristics": {
                           "vehicleType": "anyVehicle"
                         }
                       },
                       {
                         "negate": false,
                         "vehicleCharacteristics": {
                           "vehicleType": "bus"
                         }
                       },
                       {
                         "negate": false,
                         "vehicleCharacteristics": {
                           "vehicleType": "pedalCycle"
                         }
                       }
                     ]
                   }
                 ],
                 "condition": [
                   {
                     "negate": false,
                     "timeValidity": {
                       "start": "2025-01-01T08:00:00"
                       // ... end time or validPeriod if applicable
                     }
                   }
                 ]
               }
             ],
             "generalRegulation": {
               "regulationType": "miscBusGate"
             },
             "isDynamic": false,
             "timeZone": "Europe/London"
           }
         ]
       }
     ]
   }
