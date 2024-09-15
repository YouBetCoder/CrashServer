using CrashServer.ServiceModel.Data;
using ServiceStack;

[assembly: HostingStartup(typeof(ConfigureOpenApi))]

namespace CrashServer;

public class ConfigureOpenApi : IHostingStartup
{
    public void Configure(IWebHostBuilder builder) => builder
        .ConfigureServices((context, services) =>
        {
            if (!context.HostingEnvironment.IsDevelopment()) return;
            services.AddEndpointsApiExplorer();
            services.AddSwaggerGen();

            services.AddServiceStackSwagger();
            services.AddBasicAuth<ApplicationUser>();
            //services.AddJwtAuth();

            services.AddTransient<IStartupFilter, StartupFilter>();
        });

    public class StartupFilter : IStartupFilter
    {
        public Action<IApplicationBuilder> Configure(Action<IApplicationBuilder> next) => app =>
        {
            app.UseSwagger();
            app.UseSwaggerUI();
            next(app);
        };
    }
}