using ServiceStack;

[assembly: HostingStartup(typeof(ConfigureServerEvents))]

namespace CrashServer;

public class ConfigureServerEvents : IHostingStartup
{
    public void Configure(IWebHostBuilder builder) => builder
        .ConfigureServices(services => {
            services.AddPlugin(new ServerEventsFeature());
        });
}
