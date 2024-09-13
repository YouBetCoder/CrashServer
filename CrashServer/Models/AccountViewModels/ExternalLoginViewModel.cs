using System.ComponentModel.DataAnnotations;

namespace CrashServer.Models.AccountViewModels;

public class ExternalLoginViewModel
{
    [Required]
    [EmailAddress]
    public string Email { get; set; }
}