using ServiceStack;

namespace CrashServer.ServiceModel;
public class NotifyLiveViewDataUpdatedPacket
{
    public int Id { get; set; }
}

[ValidateApiKey("api:writegamedata")]
[Route("/notify")]
public class NotifyLiveViewDataUpdatedRequest : IReturn<NotifyLiveViewDataUpdatedResponse>
{
    public int Id { get; set; }
}


public class NotifyLiveViewDataUpdatedResponse
{
}

[ValidateApiKey("api:writegamedata")]
[Route("/createdata")]
public class CreateActiveGameRoom : ICreateDb<ActiveGameRoom>, IReturn<IdResponse>
{
    public int GameNumber { get; set; } = default!;
    public int RoomId { get; set; } = default!;

    public int RoundId { get; set; }

    public string GameStatus { get; set; } = default!;

    public string GamePhase { get; set; } = default!;

    public decimal GameResult { get; set; } = default!;

    public long NoMoreBetsAt { get; set; }
}

[ValidateApiKey("api:querygameprediction")]

public class ApiQueryActiveRoomPredictionResults
    : QueryDb<ActiveGameRoomPrediction, ActiveGameResult>, IJoin<ActiveGameRoomPrediction, ActiveGameRoom>
{
}


[ValidateApiKey("api:querygamedata")]
public class ApiQueryActiveGameRoom : QueryDb<ActiveGameRoom>
{
    public int? Id { get; set; }
    public int? RoundId { get; set; }
    public int? RoomId { get; set; }
}

[Authenticate]
[Route("/query/activeroom", Verbs = "GET")]
public class QueryActiveGameRoom : QueryDb<ActiveGameRoom>
{
    public int? Id { get; set; }
    public int? RoundId { get; set; }
    public int? RoomId { get; set; }
}

[Authenticate]
[EnableCors(allowedMethods: "GET,POST")]
[Route("/query/activeroomprediction", Verbs = "GET")]
public class QueryActiveRoomPredictionResults
    : QueryDb<ActiveGameRoomPrediction, ActiveGameResult>, IJoin<ActiveGameRoomPrediction, ActiveGameRoom>
{
}

public class ActiveGameResult
{
    public int ActiveGameRoomGameNumber { get; set; }
    public int ActiveGameRoomRoomId { get; set; }
    public int ActiveGameRoomRoundId { get; set; }
    public decimal GameResult { get; set; }

    public decimal Prediction { get; set; }
    public decimal Prediction2 { get; set; }
    public decimal Prediction3 { get; set; }
    public decimal Prediction4 { get; set; }
    public decimal PredictionArima { get; set; }
    public long NoMoreBetsAt { get; set; }
}