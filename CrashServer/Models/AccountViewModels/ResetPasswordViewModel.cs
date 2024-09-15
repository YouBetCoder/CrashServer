using System.ComponentModel.DataAnnotations;

namespace CrashServer.Models.AccountViewModels;

public class ResetPasswordViewModel
{
    // ReSharper disable once PropertyCanBeMadeInitOnly.Global
    [Required]
    [EmailAddress]
    public string Email { get; set; } = default!;
    // ReSharper disable once PropertyCanBeMadeInitOnly.Global
    [Required]
    [StringLength(100, ErrorMessage = "The {0} must be at least {2} and at max {1} characters long.", MinimumLength = 6)]
    [DataType(DataType.Password)]
    public string Password { get; set; } = default!;
    // ReSharper disable once PropertyCanBeMadeInitOnly.Global
    [DataType(DataType.Password)]
    [Display(Name = "Confirm password")]
    [Compare("Password", ErrorMessage = "The password and confirmation password do not match.")]
    public string ConfirmPassword { get; set; } = default!;
    // ReSharper disable once PropertyCanBeMadeInitOnly.Global
    public string Code { get; set; } = default!;
}
