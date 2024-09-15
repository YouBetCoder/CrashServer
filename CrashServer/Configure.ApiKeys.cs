using ServiceStack;
using ServiceStack.Data;
using ServiceStack.OrmLite;

[assembly: HostingStartup(typeof(ConfigureApiKeys))]

namespace CrashServer;

public class ConfigureApiKeys : IHostingStartup
{
    public void Configure(IWebHostBuilder builder) => builder
        .ConfigureServices(services =>
        {
            services.AddPlugin(new ApiKeysFeature
            {
                //admins can give people these. write is restricted.
                Scopes = [
                    "api:querygamedata",
                    "api:querygameprediction",
                    "api:writegamedata"
                ],
                 //users can create api keys that can read
                UserScopes = [
                    "api:querygamedata",
                    "api:querygameprediction"
                ]
          
            });
        })
        .ConfigureAppHost(appHost =>
        {
            using var db = appHost.Resolve<IDbConnectionFactory>().Open();
            var feature = appHost.GetPlugin<ApiKeysFeature>();
            feature.InitSchema(db);
            
            // Optional: Create API Key for specified Users on Startup
            // if (feature.ApiKeyCount(db) != 0 || !db.TableExists(IdentityUsers.TableName)) return;
            // // var createApiKeysFor = new [] { "admin@email.com", "manager@email.com" };
            // var users = IdentityUsers.GetByUserNames(db, createApiKeysFor);
            // foreach (var user in users)
            // {
            //     List<string> scopes = user.UserName == "admin@email.com"
            //         ? [RoleNames.Admin] 
            //         : [];
            //     feature.Insert(db, 
            //         new() { Name = "Seed API Key", UserId = user.Id, UserName = user.UserName, Scopes = scopes });
            // }
        });
}