""" Options:
Date: 2024-09-11 20:22:22
Version: 8.40
Tip: To override a DTO option, remove "#" prefix before updating
BaseUrl: https://localhost:5001

#GlobalNamespace: 
#AddServiceStackTypes: True
#AddResponseStatus: False
#AddImplicitVersion: 
#AddDescriptionAsComments: True
#IncludeTypes: 
#ExcludeTypes: 
#DefaultImports: datetime,decimal,marshmallow.fields:*,servicestack:*,typing:*,dataclasses:dataclass/field,dataclasses_json:dataclass_json/LetterCase/Undefined/config,enum:Enum/IntEnum
#DataClass: 
#DataClassJson: 
"""

import datetime
import decimal
from marshmallow.fields import *
from servicestack import *
from typing import *
from dataclasses import dataclass, field
from dataclasses_json import dataclass_json, LetterCase, Undefined, config
from enum import Enum, IntEnum


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class ActiveGameRoomPrediction:
    id: int = 0
    game_number: int = 0
    room_id: int = 0
    active_game_room_id: Optional[int] = None
    round_id: int = 0
    prediction: Decimal = decimal.Decimal(0)
    prediction2: Decimal = decimal.Decimal(0)
    prediction3: Decimal = decimal.Decimal(0)
    prediction4: Decimal = decimal.Decimal(0)
    prediction_arima: Decimal = decimal.Decimal(0)


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class ActiveGameResult:
    active_game_room_game_number: int = 0
    active_game_room_room_id: int = 0
    active_game_room_round_id: int = 0
    game_result: Decimal = decimal.Decimal(0)
    prediction: Decimal = decimal.Decimal(0)
    prediction2: Decimal = decimal.Decimal(0)
    prediction3: Decimal = decimal.Decimal(0)
    prediction4: Decimal = decimal.Decimal(0)
    prediction_arima: Decimal = decimal.Decimal(0)


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class ActiveGameRoom:
    id: int = 0
    game_number: int = 0
    room_id: int = 0
    round_id: int = 0
    # @StringLength(255)
    game_status: Optional[str] = None

    # @StringLength(255)
    game_phase: Optional[str] = None

    game_result: Decimal = decimal.Decimal(0)
    no_more_bets_at: int = 0


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class NotifyLiveViewDataUpdatedResponse:
    pass


# @Route("/notify")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class NotifyLiveViewDataUpdatedRequest(IReturn[NotifyLiveViewDataUpdatedResponse]):
    id: int = 0


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class QueryActiveGameRoomPrediction(QueryDb[ActiveGameRoomPrediction], IReturn[QueryResponse[ActiveGameRoomPrediction]]):
    id: Optional[int] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class ApiQueryActiveRoomPredictionResults(QueryDb2[ActiveGameRoomPrediction, ActiveGameResult], IReturn[QueryResponse[ActiveGameResult]]):
    pass


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class ApiQueryActiveGameRoom(QueryDb[ActiveGameRoom], IReturn[QueryResponse[ActiveGameRoom]]):
    id: Optional[int] = None
    round_id: Optional[int] = None
    room_id: Optional[int] = None

# @Route("/query/activeroom", "GET")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class QueryActiveGameRoom(QueryDb[ActiveGameRoom], IReturn[QueryResponse[ActiveGameRoom]]):
    id: Optional[int] = None
    round_id: Optional[int] = None


# @Route("/query/activeroomprediction", "GET")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class QueryActiveRoomPredictionResults(QueryDb2[ActiveGameRoomPrediction, ActiveGameResult], IReturn[QueryResponse[ActiveGameResult]]):
    pass


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class CreateActiveGameRoomPrediction(IReturn[IdResponse], ICreateDb[ActiveGameRoomPrediction]):
    game_number: int = 0
    room_id: int = 0
    round_id: int = 0
    prediction: Decimal = decimal.Decimal(0)
    prediction2: Decimal = decimal.Decimal(0)
    prediction3: Decimal = decimal.Decimal(0)
    prediction4: Decimal = decimal.Decimal(0)
    prediction_arima: Decimal = decimal.Decimal(0)
    active_game_room_id: Optional[int] = None


# @Route("/createdata")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class CreateActiveGameRoom(IReturn[IdResponse], ICreateDb[ActiveGameRoom]):
    game_number: int = 0
    room_id: int = 0
    round_id: int = 0
    game_status: Optional[str] = None
    game_phase: Optional[str] = None
    game_result: Decimal = decimal.Decimal(0)
    no_more_bets_at: int = 0

