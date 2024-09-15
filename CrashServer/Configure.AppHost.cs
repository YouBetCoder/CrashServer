using ServiceStack;
using ServiceStack.IO;
using ServiceStack.Logging;
using ServiceStack.OrmLite;
// ReSharper disable AutoPropertyCanBeMadeGetOnly.Global

[assembly: HostingStartup(typeof(AppHost))]

namespace CrashServer;

public class AppHost() : AppHostBase("CrashServer"), IHostingStartup
{
    public void Configure(IWebHostBuilder builder) => builder
        .ConfigureServices((context, services) =>
        {
            services.AddHostedService<TimedHostedService>();
#if DEBUG
#else
            services.AddLettuceEncrypt().PersistDataToDirectory(new DirectoryInfo("/home/crash/crashPredict/crashServer/certs"), "thecertpass");


#endif
            // Configure ASP.NET Core IOC Dependencies
            context.Configuration.GetSection(nameof(AppConfig)).Bind(AppConfig.Instance);
            services.AddSingleton(AppConfig.Instance);
        });

// Configure your AppHost with the necessary configuration and dependencies your App needs
    public override void Configure()
    {
        SetConfig(new HostConfig());
#if DEBUG
        LogManager.LogFactory = new ConsoleLogFactory(debugEnabled: true); //or console log
        OrmLiteConfig.BeforeExecFilter = dbCmd => { Console.WriteLine(dbCmd.GetDebugString()); };
#else
LogManager.LogFactory = new ConsoleLogFactory( );
#endif
        //Allow Referencing in #Script expressions, e.g. [Input(EvalAllowableEntries)]
        ScriptContext.Args[nameof(AppData)] = AppData.Instance;
        AppConfig.Instance.GitPagesBaseUrl ??= ResolveGitBlobBaseUrl(ContentRootDirectory);
    }

    private static string? ResolveGitBlobBaseUrl(IVirtualDirectory contentDir)
    {
        var srcDir = new DirectoryInfo(contentDir.RealPath);
        var gitConfig = new FileInfo(Path.Combine(srcDir.Parent!.FullName, ".git", "config"));
        if (!gitConfig.Exists) return null;
        var txt = gitConfig.ReadAllText();
        var pos = txt.IndexOf("url = ", StringComparison.Ordinal);
        if (pos < 0) return null;
        var url = txt[(pos + "url = ".Length)..].LeftPart(".git").LeftPart('\n').Trim();
        var gitBaseUrl = url.CombineWith($"blob/main/{srcDir.Name}");
        return gitBaseUrl;

    }
}

public class AppConfig
{
    public static AppConfig Instance { get; } = new();
    // ReSharper disable once UnusedMember.Global
    public string LocalBaseUrl { get; set; } = default!;
    // ReSharper disable once UnusedMember.Global
    public string PublicBaseUrl { get; set; } = default!;
    public string? GitPagesBaseUrl { get; set; }
}

 
// Shared App Data
public class AppData
{
    public static readonly AppData Instance = new();
}