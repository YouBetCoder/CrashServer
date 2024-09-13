using ServiceStack.DataAnnotations;

namespace CrashServer.ServiceModel;

[CompositeKey(nameof(GameNumber), nameof(RoomId), nameof(RoundId))]
public class ActiveGameRoom
{
    [AutoIncrement] public int Id { get; set; }

    [Index] public int GameNumber { get; set; } = default!;
    [Index] public int RoomId { get; set; } = default!;
    [Unique]
    public int RoundId { get; set; }
    [StringLength(255)] public string GameStatus { get; set; } = default!;

    [StringLength(255)] public string GamePhase { get; set; } = default!;

    public decimal GameResult { get; set; } = default!;

    public long NoMoreBetsAt { get; set; }
}

