using Microsoft.AspNetCore.Identity;
using ServiceStack;
using ServiceStack.DataAnnotations;

// ReSharper disable UnusedAutoPropertyAccessor.Global
// ReSharper disable UnusedMember.Global

namespace CrashServer.ServiceModel.Data;

[Alias("AspNetUsers")]
public class AppUser
{
    public string Id { get; set; } = default!;
    public string? FirstName { get; set; }
    public string? UserName { get; set; }
    public string? LastName { get; set; }
    public string? DisplayName { get; set; }
 
}

public class ApplicationUser : IdentityUser
{
    public string? FirstName { get; set; }
    public string? LastName { get; set; }
    public string? DisplayName { get; set; }
    public string? ProfileUrl { get; set; }
    public string? FacebookUserId { get; set; }
    public string? GoogleUserId { get; set; }
    public string? GoogleProfilePageUrl { get; set; }
    public string? MicrosoftUserId { get; set; }
}