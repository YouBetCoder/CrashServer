""" Options:
Date: 2024-09-14 21:29:22
Version: 8.40
Tip: To override a DTO option, remove "#" prefix before updating
BaseUrl: https://crash.digitalstar.co

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
class IdentityUser(IdentityUser1[str]):
    pass


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class ApplicationUser(IdentityUser):
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    display_name: Optional[str] = None
    profile_url: Optional[str] = None
    facebook_user_id: Optional[str] = None
    google_user_id: Optional[str] = None
    google_profile_page_url: Optional[str] = None
    microsoft_user_id: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class ApplicationUserPaymentLog:
    id: int = 0
    payment_covers_from: datetime.datetime = datetime.datetime(1, 1, 1)
    payment_covers_until: datetime.datetime = datetime.datetime(1, 1, 1)
    cost_usd: Decimal = decimal.Decimal(0)
    cost_sol: Decimal = decimal.Decimal(0)
    # @References(typeof(ApplicationUser))
    application_user_id: Optional[str] = None

    application_user: Optional[ApplicationUser] = None
    notes: Optional[str] = None


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
    no_more_bets_at: int = 0


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


TKey = TypeVar('TKey')


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class IdentityUser1(Generic[TKey]):
    id: Optional[TKey] = None
    user_name: Optional[str] = None
    normalized_user_name: Optional[str] = None
    email: Optional[str] = None
    normalized_email: Optional[str] = None
    email_confirmed: bool = False
    password_hash: Optional[str] = None
    security_stamp: Optional[str] = None
    concurrency_stamp: Optional[str] = None
    phone_number: Optional[str] = None
    phone_number_confirmed: bool = False
    two_factor_enabled: bool = False
    lockout_end: Optional[datetime.datetime] = None
    lockout_enabled: bool = False
    access_failed_count: int = 0


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class NotifyLiveViewDataUpdatedResponse:
    pass


# @Route("/notify")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class NotifyLiveViewDataUpdatedRequest(IReturn[NotifyLiveViewDataUpdatedResponse]):
    id: int = 0


# @Route("/data/queryactivegameroomprediction")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class ApiQueryActiveGameRoomPrediction(QueryDb[ActiveGameRoomPrediction], IReturn[QueryResponse[ActiveGameRoomPrediction]]):
    id: Optional[int] = None


# @Route("/query/predicts")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class QueryActiveGameRoomPrediction(QueryDb[ActiveGameRoomPrediction], IReturn[QueryResponse[ActiveGameRoomPrediction]]):
    id: Optional[int] = None
    round_id: Optional[int] = None
    round_ids: Optional[List[int]] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class QueryApplicationUserPaymentLog(QueryDb[ApplicationUserPaymentLog], IReturn[QueryResponse[ApplicationUserPaymentLog]]):
    id: Optional[int] = None
    payment_covers_from: Optional[datetime.datetime] = None
    payment_covers_until: Optional[datetime.datetime] = None
    application_user_id: Optional[str] = None


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
    room_id: Optional[int] = None


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


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class CreateApplicationUserPaymentLog(IReturn[IdResponse], ICreateDb[ApplicationUserPaymentLog]):
    pass


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

