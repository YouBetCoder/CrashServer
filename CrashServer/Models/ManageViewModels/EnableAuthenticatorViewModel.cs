using System.ComponentModel.DataAnnotations;
using Microsoft.AspNetCore.Mvc.ModelBinding;

namespace CrashServer.Models.ManageViewModels;

public class EnableAuthenticatorViewModel
{
    // ReSharper disable once PropertyCanBeMadeInitOnly.Global
    [Required]
    [StringLength(7, ErrorMessage = "The {0} must be at least {2} and at max {1} characters long.", MinimumLength = 6)]
    [DataType(DataType.Text)]
    [Display(Name = "Verification Code")]
    public string Code { get; set; } = default!;

    [BindNever]
    public string SharedKey { get; set; } = default!;

    [BindNever]
    public string AuthenticatorUri { get; set; } = default!;
}
