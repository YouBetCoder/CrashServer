using System.ComponentModel.DataAnnotations;

namespace CrashServer.Models.AccountViewModels;

public class LoginWithRecoveryCodeViewModel
{
    [Required]
    [DataType(DataType.Text)]
    [Display(Name = "Recovery Code")]
    // ReSharper disable once PropertyCanBeMadeInitOnly.Global
    public string RecoveryCode { get; set; } = default!;
}