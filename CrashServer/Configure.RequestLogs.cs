using ServiceStack;

[assembly: HostingStartup(typeof(ConfigureRequestLogs))]

namespace CrashServer;

public class ConfigureRequestLogs : IHostingStartup
{
    public void Configure(IWebHostBuilder builder) => builder
        .ConfigureServices((context, services) => {
            if (context.HostingEnvironment.IsDevelopment())
            {
                services.AddPlugin(new RequestLogsFeature
                {
                    EnableResponseTracking = true,
                        EnableErrorTracking = true
                });
            }
        });
}
