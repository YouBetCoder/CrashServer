using Microsoft.AspNetCore.Mvc.Rendering;
using Microsoft.AspNetCore.Mvc.ViewFeatures;

namespace CrashServer.Views.Manage;

public static class ManageNavPages
{
    // ReSharper disable once MemberCanBePrivate.Global
    public static string ActivePageKey => "ActivePage";

    public static string Index => "Index";

    public static string ChangePassword => "ChangePassword";
 
    public static string TwoFactorAuthentication => "TwoFactorAuthentication";

    public static string ApiKeys => "ApiKeys";

    public static string? IndexNavClass(ViewContext viewContext) => PageNavClass(viewContext, Index);

    public static string? ChangePasswordNavClass(ViewContext viewContext) => PageNavClass(viewContext, ChangePassword);

     
    public static string? TwoFactorAuthenticationNavClass(ViewContext viewContext) => PageNavClass(viewContext, TwoFactorAuthentication);
    
    public static string? ApiKeysNavClass(ViewContext viewContext) => PageNavClass(viewContext, ApiKeys);
    
    // ReSharper disable once MemberCanBePrivate.Global
    public static string? PageNavClass(ViewContext viewContext, string page)
    {
        var activePage = viewContext.ViewData["ActivePage"] as string;
        return string.Equals(activePage, page, StringComparison.OrdinalIgnoreCase) ? "active" : null;
    }

    public static void AddActivePage(this ViewDataDictionary viewData, string activePage) => viewData[ActivePageKey] = activePage;
}