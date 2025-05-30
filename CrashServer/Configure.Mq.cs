using ServiceStack.Messaging;
using ServiceStack;
// ReSharper disable UnusedParameter.Local

[assembly: HostingStartup(typeof(ConfigureMq))]

namespace CrashServer;

/**
 * Register ServiceStack Services you want to be able to invoke in a managed Background Thread
 * https://docs.servicestack.net/background-mq
*/
public class ConfigureMq : IHostingStartup
{
    public void Configure(IWebHostBuilder builder) => builder
        .ConfigureServices((context, services) => {
 
     //       services.AddSingleton<IMessageService>(c => new BackgroundMqService());
            services.AddPlugin(new CommandsFeature());
        })
        .ConfigureAppHost(afterAppHostInit: appHost => {
            // var mqService = appHost.Resolve<IMessageService>();

            //Register ServiceStack APIs you want to be able to invoke via MQ
       //     mqService.RegisterHandler<SendEmail>(appHost.ExecuteMessage);
         //   mqService.Start();
        });
}

// // Remove the "else if (EmailSender is IdentityNoOpEmailSender)" block from RegisterConfirmation.razor after updating with a real implementation.
// internal sealed class IdentityNoOpEmailSender : IEmailSender<ApplicationUser>
// {
//     private readonly IEmailSender emailSender = new NoOpEmailSender();
//
//     public Task SendConfirmationLinkAsync(ApplicationUser user, string email, string confirmationLink) =>
//         emailSender.SendEmailAsync(email, "Confirm your email", $"Please confirm your account by <a href='{confirmationLink}'>clicking here</a>.");
//
//     public Task SendPasswordResetLinkAsync(ApplicationUser user, string email, string resetLink) =>
//         emailSender.SendEmailAsync(email, "Reset your password", $"Please reset your password by <a href='{resetLink}'>clicking here</a>.");
//
//     public Task SendPasswordResetCodeAsync(ApplicationUser user, string email, string resetCode) =>
//         emailSender.SendEmailAsync(email, "Reset your password", $"Please reset your password using the following code: {resetCode}");
// }

// public class EmailSender(IMessageService messageService) : IEmailSender<ApplicationUser>
// {
//     public Task SendEmailAsync(string email, string subject, string htmlMessage)
//     {
//         using var mqClient = messageService.CreateMessageProducer();
//         mqClient.Publish(new SendEmail
//         {
//             To = email,
//             Subject = subject,
//             BodyHtml = htmlMessage,
//         });
//
//         return Task.CompletedTask;
//     }
//
//     public Task SendConfirmationLinkAsync(ApplicationUser user, string email, string confirmationLink) =>
//         SendEmailAsync(email, "Confirm your email", $"Please confirm your account by <a href='{confirmationLink}'>clicking here</a>.");
//
//     public Task SendPasswordResetLinkAsync(ApplicationUser user, string email, string resetLink) =>
//         SendEmailAsync(email, "Reset your password", $"Please reset your password by <a href='{resetLink}'>clicking here</a>.");
//
//     public Task SendPasswordResetCodeAsync(ApplicationUser user, string email, string resetCode) =>
//         SendEmailAsync(email, "Reset your password", $"Please reset your password using the following code: {resetCode}");
// }
