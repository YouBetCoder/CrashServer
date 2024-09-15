using CrashServer.ServiceModel.Data;
using ServiceStack;
using ServiceStack.DataAnnotations;
// ReSharper disable ClassNeverInstantiated.Global
// ReSharper disable UnusedType.Global
// ReSharper disable UnusedMember.Global

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
    public int[] RoundIds { get; set; } = default!;
}

public class ApplicationUserPaymentLog
{
    [AutoIncrement] public int Id { get; set; }
    public DateTime PaymentCoversFrom { get; set; } = DateTime.Now;
    public DateTime PaymentCoversUntil { get; set; } = DateTime.Now.AddDays(7);

    [IntlNumber(Currency = NumberCurrency.USD)]
    public decimal CostUsd { get; set; }

    public decimal CostSol { get; set; }

    [Ref(Model = nameof(ApplicationUser), RefId = nameof(ApplicationUser.UserName), RefLabel = nameof(ApplicationUser.UserName))]
    [References(typeof(ApplicationUser))]
    public string? ApplicationUserId { get; set; }

    [Reference] public ApplicationUser ApplicationUser { get; set; } = default!;

    public string Notes { get; set; } = default!;
}

[Authenticate]
[RequiredRole("Admin")]
public class QueryApplicationUserPaymentLog : QueryDb<ApplicationUserPaymentLog>
{
    public int? Id { get; set; }
    public DateTime? PaymentCoversFrom { get; set; } 
    public DateTime? PaymentCoversUntil { get; set; } 
    public string? ApplicationUserId { get; set; }
}
 
[Authenticate]
[RequiredRole("Admin")]
public class CreateApplicationUserPaymentLog : ICreateDb<ApplicationUserPaymentLog>, IReturn<IdResponse>
{
    // public DateTime PaymentCoversFrom { get; set; } = DateTime.Now;
    // public DateTime PaymentCoversUntil { get; set; } = DateTime.Now.AddDays(7);
    //
    // [IntlNumber(Currency = NumberCurrency.USD)]
    // public decimal CostUsd { get; set; }
    //
    // public decimal CostSol { get; set; }
    //
    // [Ref(Model = nameof(ApplicationUser), RefId = nameof(ApplicationUser.UserName), RefLabel = nameof(ApplicationUser.UserName))]
    // [References(typeof(ApplicationUser))]
    // public string? ApplicationUserId { get; set; }
    //
    // [Reference] public ApplicationUser ApplicationUser { get; set; } = default!;
    //
    // public string Notes { get; set; } = default!;
}