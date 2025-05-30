using System.ComponentModel.DataAnnotations;
// ReSharper disable PropertyCanBeMadeInitOnly.Global

namespace CrashServer.Models.ManageViewModels;

public class IndexViewModel
{
    public string? Username { get; set; }

    public bool IsEmailConfirmed { get; set; }

    [Required]
    [EmailAddress]
    public string? Email { get; set; }
    //
    // [Phone]
    // [Display(Name = "Phone number")]
    // public string PhoneNumber { get; set; }

    public string? StatusMessage { get; set; }
}