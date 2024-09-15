[assembly: HostingStartup(typeof(ConfigureCors))]

namespace CrashServer;

public class ConfigureCors : IHostingStartup
{
    public void Configure(IWebHostBuilder builder) => builder
        .ConfigureServices(services =>
        {
            services.AddCors(options => {
                options.AddDefaultPolicy(policy => {
                    policy
                    //     .WithOrigins([
                    //     "http://localhost:5000", "https://localhost:5001", 
                    //     "https://localhost:5173", "http://localhost:5173",
                    //     "https://crash.degencoinflip.com/"
                    // ])
                        .AllowAnyOrigin()
                    //.AllowCredentials()
                    .WithHeaders(["Content-Type", "Allow", "Authorization"])
                    .SetPreflightMaxAge(TimeSpan.FromHours(1));
                });
            });
            services.AddTransient<IStartupFilter, StartupFilter>();
        });

    public class StartupFilter : IStartupFilter
    {
        public Action<IApplicationBuilder> Configure(Action<IApplicationBuilder> next) => app =>
        {
            app.UseCors();
            next(app);
        };
    }        
}
