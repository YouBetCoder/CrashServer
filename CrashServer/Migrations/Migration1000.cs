using System.Data;
using ServiceStack;
using ServiceStack.DataAnnotations;
using ServiceStack.OrmLite;

namespace CrashServer.Migrations;

public class Migration1003 : MigrationBase
{
    public class ActiveGameRoomPrediction
    {
        [AutoIncrement] public int Id { get; set; }

        [Index] public int GameNumber { get; set; }

        [Index] public int RoomId { get; set; }

        [Unique]
        [ForeignKey(typeof(ActiveGameRoom), OnDelete = "SET NULL", OnUpdate = "SET NULL")]
        public int? RoundId { get; set; }


        public decimal Prediction { get; set; }
        public decimal Prediction2 { get; set; }
        public decimal Prediction3 { get; set; }
        public decimal Prediction4 { get; set; }
        public decimal PredictionArima { get; set; }
    }

    public override void Up()
    {
        Db.DropAndCreateTable<ActiveGameRoomPrediction>();
    }

    public override void Down()
    {
        Db.DropTable<ActiveGameRoomPrediction>();
    }
}

public class Migration1002 : MigrationBase
{
  
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

    public override void Up()
    {
        Db.CreateTable<ActiveGameRoomPrediction>();
    }

    public override void Down()
    {
        Db.DropTable<ActiveGameRoomPrediction>();
    }
}

public class Migration1000 : MigrationBase
{
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

    public override void Up()
    {
        Db.CreateTable<ActiveGameRoom>();
    }

    public override void Down()
    {
        Db.DropTable<ActiveGameRoom>();
    }
}