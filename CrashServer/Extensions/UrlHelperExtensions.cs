using Microsoft.AspNetCore.Mvc;
using CrashServer.Controllers;

namespace CrashServer.Extensions;

public static class UrlHelperExtensions
{
    public static string EmailConfirmationLink(this IUrlHelper urlHelper, string userId, string code, string scheme)
    {
        return urlHelper.Action(
            action: nameof(AccountController.ConfirmEmail),
            controller: "Account",
            values: new { userId, code },
            protocol: scheme) ?? string.Empty;
    }

    public static string ResetPasswordCallbackLink(this IUrlHelper urlHelper, string userId, string code, string scheme)
    {
        return urlHelper.Action(
            action: nameof(AccountController.ResetPassword),
            controller: "Account",
            values: new { userId, code },
            protocol: scheme) ?? string.Empty;
    }
}