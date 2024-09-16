using ServiceStack;
using ServiceStack.DataAnnotations;

// ReSharper disable UnusedAutoPropertyAccessor.Global
// ReSharper disable ClassNeverInstantiated.Global
// ReSharper disable UnusedType.Global
// ReSharper disable UnusedMember.Global

namespace CrashServer.ServiceModel;

public class NotifyLiveViewDataUpdatedPacket
{
    public int Id { get; set; }
    public bool TeaCup { get; set; }
}
[Exclude(Feature.Metadata)] 
[ValidateApiKey("api:writegamedata")]
[Route("/notify")]
public class NotifyLiveViewDataUpdatedRequest : IReturn<NotifyLiveViewDataUpdatedResponse>
{
    public int Id { get; set; }
    public bool TeaCup { get; set; }
}

public class NotifyLiveViewDataUpdatedResponse;
[Exclude(Feature.Metadata)] 
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
    public long TimeRecorded { get; set; }
}



[ValidateApiKey("api:querygamedata")]
public class ApiQueryActiveGameRoom : QueryDb<ActiveGameRoom>
{
    public int? Id { get; set; }
    public int? RoundId { get; set; }
    public int? RoomId { get; set; }
    public long? TimeRecorded { get; set; }
}

[Authenticate]
[Route("/query/activeroom", Verbs = "GET")]
public class QueryActiveGameRoom : QueryDb<ActiveGameRoom>
{
    public int? Id { get; set; }
    public int? RoundId { get; set; }
    public int? RoomId { get; set; }
    public long? TimeRecorded { get; set; }
}

[ValidateApiKey("api:querygameprediction")]
public class ApiQueryActiveRoomPredictionResults
    : QueryDb<ActiveGameRoom, ActiveGameResult>, IJoin< ActiveGameRoom,ActiveGameRoomPrediction>;


[Authenticate]
[EnableCors(allowedMethods: "GET,POST")]
[Route("/query/activeroomprediction", Verbs = "GET")]
public class QueryActiveRoomPredictionResults
    : QueryDb<ActiveGameRoom, ActiveGameResult>, IJoin< ActiveGameRoom,ActiveGameRoomPrediction>;




 
public class ActiveGameResult
{
    [Alias("ActiveGameRoomId.Id")]
    public int Id { get; set; }
    public int GameNumber { get; set; }
    public int RoomId { get; set; }
    public int ActiveGameRoomRoundId { get; set; }
    public decimal GameResult { get; set; }

    public decimal Prediction { get; set; }
    public decimal Prediction2 { get; set; }
    public decimal Prediction3 { get; set; }
    public decimal Prediction4 { get; set; }
    public decimal PredictionArima { get; set; }
    public long NoMoreBetsAt { get; set; }
}