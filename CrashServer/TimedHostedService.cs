using ServiceStack.Data;
using ServiceStack.OrmLite;

namespace CrashServer;

public class TimedHostedService(IDbConnectionFactory dbConnectionFactory, ILogger<TimedHostedService> logger) : IHostedService, IDisposable
{
    private Timer? _timer;

    public Task StartAsync(CancellationToken cancellationToken)
    {
        _timer = new Timer(DoWork, null, TimeSpan.Zero,
            TimeSpan.FromSeconds(15));

        return Task.CompletedTask;
    }

    private async void DoWork(object? state)
    {
        await ExecuteSqlAsync();
    }

    public Task StopAsync(CancellationToken cancellationToken)
    {
        _timer?.Change(Timeout.Infinite, 0);

        return Task.CompletedTask;
    }

    public void Dispose()
    {
        GC.SuppressFinalize(this);
        _timer?.Dispose();
    }

    private async Task ExecuteSqlAsync()
    {
        using var db = await dbConnectionFactory.OpenAsync();
        try
        {
            await db.ExecuteSqlAsync(
                """
                UPDATE ActiveGameRoomPrediction
                SET ActiveGameRoomId = ActiveGameRoom.ID
                FROM ActiveGameRoom
                WHERE ActiveGameRoomPrediction.RoundId = ActiveGameRoom.RoundId and ActiveGameRoomId is Null
                """);
        }
        catch (Exception ex)
        {
            logger.LogError(ex, "Error during join update");
        }
    }
}