using System.ComponentModel.DataAnnotations;

namespace CrashServer.Models.AccountViewModels;

public class ForgotPasswordViewModel
{
    [Required]
    [EmailAddress]
    public string Email { get; set; }
}