using CrashServer.ServiceModel.Data;
using ServiceStack;
using ServiceStack.DataAnnotations;
using ServiceStack.OrmLite;

// ReSharper disable MemberCanBePrivate.Global
// ReSharper disable ClassNeverInstantiated.Global
// ReSharper disable UnusedType.Global
// ReSharper disable UnusedMember.Global

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

public class Migration1005 : MigrationBase
{
    [CompositeKey(nameof(GameNumber), nameof(RoomId), nameof(RoundId))]
    public class ActiveGameRoom
    {
        [AutoIncrement] public int Id { get; set; }

        [Index] public int GameNumber { get; set; } = default!;
        [Index] public int RoomId { get; set; } = default!;
        [Unique] public int RoundId { get; set; }
        [StringLength(255)] public string GameStatus { get; set; } = default!;

        [StringLength(255)] public string GamePhase { get; set; } = default!;

        public decimal GameResult { get; set; } = default!;

        public long NoMoreBetsAt { get; set; }


        [Index] public long? TimeRecorded { get; set; }
    }

    public override void Down()
    {
        Db.DropColumn<ActiveGameRoom>(a => a.TimeRecorded);
    }

    public override void Up()
    {
        Db.AddColumn<ActiveGameRoom>(a => a.TimeRecorded);
        Db.CreateIndex<ActiveGameRoom>(a => a.TimeRecorded);
        var items = Db.Select<ActiveGameRoom>(a => true);
        foreach (var activeGameRoom in items)
        {
            activeGameRoom.TimeRecorded = activeGameRoom.NoMoreBetsAt + 7200;
        }

        Db.SaveAll(items);
    }
}

public class Migration1006 : MigrationBase
{
 
    public class ApplicationUserPaymentLog
    {
        [AutoIncrement] public int Id { get; set; }
        public DateTime PaymentCoversFrom { get; set; } = DateTime.Now;
        public DateTime PaymentCoversUntil { get; set; } = DateTime.Now.AddDays(7);

        [IntlNumber(Currency = NumberCurrency.USD)]
        public decimal CostUsd { get; set; }

        public decimal CostSol { get; set; }

        [Ref(Model = nameof(AppUser), RefId = nameof(AppUser.UserName), RefLabel = nameof(AppUser.UserName))]
        [References(typeof(AppUser))]
        public string? UsersId { get; set; }

        [Reference] public AppUser AppUser { get; set; } = default!;

        [Unique] public string TransactionHash { get; set; }= default!;
        public string Notes { get; set; } = default!;
    
    }

    public override void Down()
    {
        Db.DropTable<ApplicationUserPaymentLog>();
    }

    public override void Up()
    {
        Db.CreateTable<ApplicationUserPaymentLog>();
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
        [Unique] public int RoundId { get; set; }
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