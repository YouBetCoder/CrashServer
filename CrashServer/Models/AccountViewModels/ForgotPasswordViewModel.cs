using System.ComponentModel.DataAnnotations;

namespace CrashServer.Models.AccountViewModels;

public class ForgotPasswordViewModel
{
    // ReSharper disable once PropertyCanBeMadeInitOnly.Global
    [Required]
    [EmailAddress]
    public string Email { get; set; }= default!;
}