using ServiceStack;

[assembly: HostingStartup(typeof(CrashServer.ConfigureServerEvents))]

namespace CrashServer;

public class ConfigureServerEvents : IHostingStartup
{
    public void Configure(IWebHostBuilder builder) => builder
        .ConfigureServices(services => {
            services.AddPlugin(new ServerEventsFeature());
        });
}
