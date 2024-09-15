namespace CrashServer.Models;

public class ErrorViewModel
{
    // ReSharper disable once PropertyCanBeMadeInitOnly.Global
    public string RequestId { get; set; }= default!;

    public bool ShowRequestId => !string.IsNullOrEmpty(RequestId);
}