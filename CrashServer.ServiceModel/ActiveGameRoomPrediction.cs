using ServiceStack;
using ServiceStack.DataAnnotations;

namespace CrashServer.ServiceModel;

[CompositeKey(nameof(GameNumber), nameof(RoomId), nameof(RoundId))]
public class ActiveGameRoomPrediction
{
    [AutoIncrement] public int Id { get; set; }

    [Index] public int GameNumber { get; set; }

    [Index] public int RoomId { get; set; }


 
    [ForeignKey(typeof(ActiveGameRoom), OnDelete = "SET NULL", OnUpdate = "SET NULL")]

    public int? ActiveGameRoomId { get; set; }

    [Unique] public int RoundId { get; set; }


    public decimal Prediction { get; set; }
    public decimal Prediction2 { get; set; }
    public decimal Prediction3 { get; set; }
    public decimal Prediction4 { get; set; }
    public decimal PredictionArima { get; set; }
}


[ValidateApiKey("api:writegamedata")]
public class CreateActiveGameRoomPrediction : ICreateDb<ActiveGameRoomPrediction>, IReturn<IdResponse>
{
    public int GameNumber { get; set; } = default!;
    public int RoomId { get; set; } = default!;
    public int RoundId { get; set; } = default!;
    public decimal Prediction { get; set; } = default!;
    public decimal Prediction2 { get; set; } = default!;
    public decimal Prediction3 { get; set; } = default!;
    public decimal Prediction4 { get; set; } = default!;
    public decimal PredictionArima { get; set; }
    public int? ActiveGameRoomId { get; set; }
}

[ValidateApiKey("api:querygameprediction")]
[Route("/data/queryactivegameroomprediction")]
public class ApiQueryActiveGameRoomPrediction : QueryDb<ActiveGameRoomPrediction>
{
    public int? Id { get; set; }
}

[Authenticate]
[Route("/query/predicts")]
public class QueryActiveGameRoomPrediction : QueryDb<ActiveGameRoomPrediction>
{
    public int? Id { get; set; }
    public int? RoundId { get; set; }
    public int[] RoundIds { get; set; }
}