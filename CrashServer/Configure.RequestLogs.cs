using ServiceStack;
using ServiceStack.IO;

[assembly: HostingStartup(typeof(ConfigureRequestLogs))]

namespace CrashServer;

public class ConfigureRequestLogs : IHostingStartup
{
    public void Configure(IWebHostBuilder builder) => builder
        .ConfigureServices((context, services) =>
        {
            if (context.HostingEnvironment.IsDevelopment())
            {
                return;
            }

            services.AddPlugin(new RequestLogsFeature
            {
                EnableResponseTracking = true,
                EnableErrorTracking = true,
                RequestLogger = new CsvRequestLogger(files: new FileSystemVirtualFiles("/var/log/"),
                    requestLogsPattern: "{year}-{month}/{year}-{month}-{day}.log",
                    errorLogsPattern: "{year}-{month}/{year}-{month}-{day}-errors.log",
                    appendEvery: TimeSpan.FromSeconds(10))
            });
        });
}