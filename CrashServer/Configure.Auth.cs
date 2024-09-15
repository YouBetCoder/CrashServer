using CrashServer.ServiceModel.Data;
using ServiceStack;
using ServiceStack.Auth;

[assembly: HostingStartup(typeof(ConfigureAuth))]

namespace CrashServer;

public class ConfigureAuth : IHostingStartup
{
    public void Configure(IWebHostBuilder builder) => builder
        .ConfigureServices(services =>
        {
            services.AddSingleton<IAuthHttpGateway, AuthHttpGateway>();
        //    services.AddTransient<IExternalLoginAuthInfoProvider, ExternalLoginAuthInfoProvider>();

            services.AddPlugin(new AuthFeature(IdentityAuth.For<ApplicationUser>(options =>
            {
                options.SessionFactory = () => new CustomUserSession();
                options.CredentialsAuth();
                options.AdminUsersFeature();
            })));
        });
}
//
// public interface IExternalLoginAuthInfoProvider
// {
//     void PopulateUser(ExternalLoginInfo info, ApplicationUser user);
// }
//
// // Populate ApplicationUser with Auth Info
// public class ExternalLoginAuthInfoProvider(IConfiguration configuration, IAuthHttpGateway authGateway)
//     : IExternalLoginAuthInfoProvider
// {
//     public void PopulateUser(ExternalLoginInfo info, ApplicationUser user)
//     {
//         var accessToken = info.AuthenticationTokens?.FirstOrDefault(x => x.Name == "access_token");
//         //var accessTokenSecret = info.AuthenticationTokens?.FirstOrDefault(x => x.Name == "access_token_secret");
//
//         switch (info.LoginProvider)
//         {
//             case "Facebook":
//             {
//                 // user.FacebookUserId = info.Principal.Claims.FirstOrDefault(x => x.Type == ClaimTypes.NameIdentifier)?.Value;
//                 // user.DisplayName = info.Principal.Claims.FirstOrDefault(x => x.Type == ClaimTypes.Name)?.Value;
//                 // user.FirstName = info.Principal.Claims.FirstOrDefault(x => x.Type == ClaimTypes.GivenName)?.Value;
//                 // user.LastName = info.Principal.Claims.FirstOrDefault(x => x.Type == ClaimTypes.Surname)?.Value;
//                 //
//                 // if (accessToken == null)
//                 // {
//                 //     break;
//                 // }
//                 //
//                 // var facebookInfo = JsonObject.Parse(authGateway.DownloadFacebookUserInfo(accessToken.Value, "picture"));
//                 // var picture = facebookInfo.Object("picture");
//                 // var data = picture?.Object("data");
//                 // if (data != null)
//                 // {
//                 //     if (data.TryGetValue("url", out var profileUrl))
//                 //     {
//                 //         user.ProfileUrl = profileUrl.SanitizeOAuthUrl();
//                 //     }
//                 // }
//
//                 break;
//             }
//             case "Google":
//             {
//                 // user.GoogleUserId = info.Principal?.Claims.FirstOrDefault(x => x.Type == ClaimTypes.NameIdentifier)?.Value;
//                 // user.DisplayName = info.Principal?.Claims.FirstOrDefault(x => x.Type == ClaimTypes.Name)?.Value;
//                 // user.FirstName = info.Principal?.Claims.FirstOrDefault(x => x.Type == ClaimTypes.GivenName)?.Value;
//                 // user.LastName = info.Principal?.Claims.FirstOrDefault(x => x.Type == ClaimTypes.Surname)?.Value;
//                 // user.GoogleProfilePageUrl = info.Principal?.Claims.FirstOrDefault(x => x.Type == "urn:google:profile")?.Value;
//                 //
//                 // if (accessToken != null)
//                 // {
//                 //     var googleInfo = JsonObject.Parse(authGateway.DownloadGoogleUserInfo(accessToken.Value));
//                 //     user.ProfileUrl = googleInfo.Get("picture").SanitizeOAuthUrl();
//                 // }
//
//                 break;
//             }
//             case "Microsoft":
//             {
//                 // user.MicrosoftUserId = info.Principal?.Claims.FirstOrDefault(x => x.Type == ClaimTypes.NameIdentifier)?.Value;
//                 // user.DisplayName = info.Principal?.Claims.FirstOrDefault(x => x.Type == ClaimTypes.Name)?.Value;
//                 // user.FirstName = info.Principal?.Claims.FirstOrDefault(x => x.Type == ClaimTypes.GivenName)?.Value;
//                 // user.LastName = info.Principal?.Claims.FirstOrDefault(x => x.Type == ClaimTypes.Surname)?.Value;
//                 // if (accessToken != null)
//                 // {
//                 //     user.ProfileUrl = authGateway.CreateMicrosoftPhotoUrl(accessToken.Value, "96x96");
//                 // }
//
//                 break;
//             }
//         }
//     }
// }