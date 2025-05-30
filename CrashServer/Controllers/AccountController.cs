using CrashServer.Models.AccountViewModels;
using CrashServer.ServiceModel.Data;
using Microsoft.AspNetCore.Authentication;
using Microsoft.AspNetCore.Authorization;
using Microsoft.AspNetCore.Identity;
using Microsoft.AspNetCore.Mvc;
using ServiceStack.Mvc;

namespace CrashServer.Controllers;

[Authorize]
[Route("[controller]/[action]")]
public class AccountController(
    UserManager<ApplicationUser> userManager,
    SignInManager<ApplicationUser> signInManager,
    ILogger<AccountController> logger)
    : ServiceStackController
{
    // private IExternalLoginAuthInfoProvider _authInfoProvider;
    // private readonly IEmailSender<ApplicationUser> _emailSender;
    private readonly ILogger _logger = logger;

    // IExternalLoginAuthInfoProvider authInfoProvider,
    // IEmailSender<ApplicationUser> emailSender,
    // _authInfoProvider = authInfoProvider;
    // _emailSender = emailSender;

    // ReSharper disable once UnusedMember.Global
    [TempData] public string? ErrorMessage { get; set; }

    [HttpGet]
    [AllowAnonymous]
    public async Task<IActionResult> Login(string? returnUrl = null)
    {
        // Clear the existing external cookie to ensure a clean login process
        await HttpContext.SignOutAsync(IdentityConstants.ExternalScheme);

        ViewData["ReturnUrl"] = returnUrl;
        return View(SessionAs<CustomUserSession>());
    }

    [HttpPost]
    [AllowAnonymous]
    [ValidateAntiForgeryToken]
    public async Task<IActionResult> Login(LoginViewModel model, string? returnUrl = null)
    {
        ViewData["ReturnUrl"] = returnUrl;
        if (!ModelState.IsValid) return View(model);
        // This doesn't count login failures towards account lockout
        // To enable password failures to trigger account lockout, set lockoutOnFailure: true
        var signedUser = await userManager.FindByEmailAsync(model.Email);
        if (signedUser == null)
        {
            ModelState.AddModelError(string.Empty, "Invalid login attempt.");
            return View(model);
        }

        if (signedUser.UserName == null)
        {
            ModelState.AddModelError(string.Empty, "Invalid account login attempt.");
            return View(model);
        }

        var result = await signInManager.PasswordSignInAsync(signedUser.UserName, model.Password, model.RememberMe, lockoutOnFailure: false);
        if (result.Succeeded)
        {
            _logger.LogInformation("User logged in");
            return RedirectToLocal(returnUrl ?? "/home");
        }

        if (result.RequiresTwoFactor)
        {
            return RedirectToAction(nameof(LoginWith2fa), new { returnUrl, model.RememberMe });
        }

        if (result.IsLockedOut)
        {
            _logger.LogWarning("User account locked out");
            return RedirectToAction(nameof(Lockout));
        }

        ModelState.AddModelError(string.Empty, "Invalid login attempt.");
        return View(model);
    }

    [HttpGet]
    [AllowAnonymous]
    public async Task<IActionResult> LoginWith2fa(bool rememberMe, string? returnUrl = null)
    {
        // Ensure the user has gone through the username & password screen first
        var user = await signInManager.GetTwoFactorAuthenticationUserAsync();

        if (user == null)
        {
            throw new ApplicationException("Unable to load two-factor authentication user.");
        }

        var model = new LoginWith2faViewModel { RememberMe = rememberMe };
        ViewData["ReturnUrl"] = returnUrl;

        return View(model);
    }

    [HttpPost]
    [AllowAnonymous]
    [ValidateAntiForgeryToken]
    public async Task<IActionResult> LoginWith2fa(LoginWith2faViewModel model, bool rememberMe, string? returnUrl = null)
    {
        if (!ModelState.IsValid)
        {
            return View(model);
        }

        var user = await signInManager.GetTwoFactorAuthenticationUserAsync();
        if (user == null)
        {
            throw new ApplicationException($"Unable to load user with ID '{userManager.GetUserId(User)}'.");
        }

        var authenticatorCode = model.TwoFactorCode.Replace(" ", string.Empty).Replace("-", string.Empty);

        var result = await signInManager.TwoFactorAuthenticatorSignInAsync(authenticatorCode, rememberMe, model.RememberMachine);

        if (result.Succeeded)
        {
            _logger.LogInformation("User with ID {UserId} logged in with 2fa", user.Id);
            return RedirectToLocal(returnUrl ?? "/home?weirdReturnUrl2");
        }

        if (result.IsLockedOut)
        {
            _logger.LogWarning("User with ID {UserId} account locked out", user.Id);
            return RedirectToAction(nameof(Lockout));
        }

        _logger.LogWarning("Invalid authenticator code entered for user with ID {UserId}", user.Id);
        ModelState.AddModelError(string.Empty, "Invalid authenticator code.");
        return View();
    }

    [HttpGet]
    [AllowAnonymous]
    public async Task<IActionResult> LoginWithRecoveryCode(string? returnUrl = null)
    {
        // Ensure the user has gone through the username & password screen first
        var user = await signInManager.GetTwoFactorAuthenticationUserAsync();
        if (user == null)
        {
            throw new ApplicationException("Unable to load two-factor authentication user.");
        }

        ViewData["ReturnUrl"] = returnUrl;

        return View();
    }

    [HttpPost]
    [AllowAnonymous]
    [ValidateAntiForgeryToken]
    public async Task<IActionResult> LoginWithRecoveryCode(LoginWithRecoveryCodeViewModel model, string? returnUrl = null)
    {
        if (!ModelState.IsValid)
        {
            return View(model);
        }

        var user = await signInManager.GetTwoFactorAuthenticationUserAsync();
        if (user == null)
        {
            throw new ApplicationException("Unable to load two-factor authentication user.");
        }

        var recoveryCode = model.RecoveryCode.Replace(" ", string.Empty);

        var result = await signInManager.TwoFactorRecoveryCodeSignInAsync(recoveryCode);

        if (result.Succeeded)
        {
            _logger.LogInformation("User with ID {UserId} logged in with a recovery code", user.Id);
            return RedirectToLocal(returnUrl ?? "/home?weirdReturnUrl3");
        }

        if (result.IsLockedOut)
        {
            _logger.LogWarning("User with ID {UserId} account locked out", user.Id);
            return RedirectToAction(nameof(Lockout));
        }

        _logger.LogWarning("Invalid recovery code entered for user with ID {UserId}", user.Id);
        ModelState.AddModelError(string.Empty, "Invalid recovery code entered.");
        return View();
    }

    [HttpGet]
    [AllowAnonymous]
    public IActionResult Lockout()
    {
        return View();
    }

    // [HttpGet]
    // [AllowAnonymous]
    // public IActionResult Register(string returnUrl = null)
    // {
    //     return View();
    //     ViewData["ReturnUrl"] = returnUrl;
    //     return View();
    // }
    //
    // [HttpPost]
    // [AllowAnonymous]
    // [ValidateAntiForgeryToken]
    // public async Task<IActionResult> Register(RegisterViewModel model, string returnUrl = null)
    // {
    //     return View();
    //     ViewData["ReturnUrl"] = returnUrl;
    //     if (ModelState.IsValid)
    //     {
    //         var user = new ApplicationUser {
    //             FirstName = model.FirstName,
    //             LastName = model.LastName,
    //             DisplayName = $"{model.FirstName} {model.LastName}",
    //             UserName = model.Email, 
    //             Email = model.Email,
    //         };
    //         var result = await _userManager.CreateAsync(user, model.Password);
    //         if (result.Succeeded)
    //         {
    //             _logger.LogInformation("User created a new account with password.");
    //
    //             var code = await _userManager.GenerateEmailConfirmationTokenAsync(user);
    //             var callbackUrl = Url.EmailConfirmationLink(user.Id, code, Request.Scheme);
    //             await _emailSender.SendConfirmationLinkAsync(user, model.Email, callbackUrl);
    //
    //             await _signInManager.SignInAsync(user, isPersistent: false);
    //             _logger.LogInformation("User created a new account with password.");
    //             return RedirectToLocal(returnUrl);
    //         }
    //         AddErrors(result);
    //     }
    //
    //     // If we got this far, something failed, redisplay form
    //     return View(model);
    // }

    [HttpPost]
    [ValidateAntiForgeryToken]
    public async Task<IActionResult> Logout()
    {
        await signInManager.SignOutAsync();
        _logger.LogInformation("User logged out");
        return RedirectToAction(nameof(SignedOut));
    }
    //
    // [HttpPost]
    // [AllowAnonymous]
    // [ValidateAntiForgeryToken]
    // public IActionResult ExternalLogin(string provider, string returnUrl = null)
    // {
    //     return View();
    //     // Request a redirect to the external login provider.
    //     var redirectUrl = Url.Action(nameof(ExternalLoginCallback), "Account", new { returnUrl });
    //     var properties = _signInManager.ConfigureExternalAuthenticationProperties(provider, redirectUrl);
    //     return Challenge(properties, provider);
    // }
    //
    // [HttpGet]
    // [AllowAnonymous]
    // public async Task<IActionResult> ExternalLoginCallback(string returnUrl = null, string remoteError = null)
    // {
    //     return View();
    //     if (remoteError != null)
    //     {
    //         ErrorMessage = $"Error from external provider: {remoteError}";
    //         return RedirectToAction(nameof(Login));
    //     }
    //     var info = await _signInManager.GetExternalLoginInfoAsync();
    //     if (info == null)
    //     {
    //         return RedirectToAction(nameof(Login));
    //     }
    //         
    //     // Sign in the user with this external login provider if the user already has a login.
    //     var result = await _signInManager.ExternalLoginSignInAsync(info.LoginProvider, info.ProviderKey, isPersistent: false, bypassTwoFactor: true);
    //     if (result.Succeeded)
    //     {
    //         _logger.LogInformation("User logged in with {Name} provider.", info.LoginProvider);
    //         return RedirectToLocal(returnUrl);
    //     }
    //     if (result.IsLockedOut)
    //     {
    //         return RedirectToAction(nameof(Lockout));
    //     }
    //     else
    //     {
    //         // If the user does not have an account, then ask the user to create an account.
    //         ViewData["ReturnUrl"] = returnUrl;
    //         ViewData["LoginProvider"] = info.LoginProvider;
    //         var email = info.Principal.FindFirstValue(ClaimTypes.Email);
    //         return View("ExternalLogin", new ExternalLoginViewModel { Email = email });
    //     }
    // }
    //
    // [HttpPost]
    // [AllowAnonymous]
    // [ValidateAntiForgeryToken]
    // public async Task<IActionResult> ExternalLoginConfirmation(ExternalLoginViewModel model, string returnUrl = null)
    // {
    //     return View();
    //     if (ModelState.IsValid)
    //     {
    //         // Get the information about the user from the external login provider
    //         var info = await _signInManager.GetExternalLoginInfoAsync();
    //         if (info == null)
    //         {
    //             throw new ApplicationException("Error loading external login information during confirmation.");
    //         }
    //
    //         var user = new ApplicationUser {
    //             UserName = model.Email, 
    //             Email = model.Email ?? info.Principal?.Claims.FirstOrDefault(x => x.Type == ClaimTypes.Email)?.Value,
    //             DisplayName = info.Principal?.Identity.Name,
    //         };
    //
    //         _authInfoProvider.PopulateUser(info, user);
    //
    //         var result = await _userManager.CreateAsync(user);
    //         if (result.Succeeded)
    //         {
    //             result = await _userManager.AddLoginAsync(user, info);
    //             if (result.Succeeded)
    //             {
    //                 await _signInManager.SignInAsync(user, isPersistent: false);
    //                 _logger.LogInformation("User created an account using {Name} provider.", info.LoginProvider);
    //                 return RedirectToLocal(returnUrl);
    //             }
    //         }
    //         AddErrors(result);
    //     }
    //
    //     ViewData["ReturnUrl"] = returnUrl;
    //     return View(nameof(ExternalLogin), model);
    // }
    //
    // [HttpGet]
    // [AllowAnonymous]
    // public async Task<IActionResult> ConfirmEmail(string userId, string code)
    // {
    //     if (userId == null || code == null)
    //     {
    //         return RedirectToAction(nameof(HomeController.Index), "Home");
    //     }
    //     var user = await _userManager.FindByIdAsync(userId);
    //     if (user == null)
    //     {
    //         throw new ApplicationException($"Unable to load user with ID '{userId}'.");
    //     }
    //     var result = await _userManager.ConfirmEmailAsync(user, code);
    //     return View(result.Succeeded ? "ConfirmEmail" : "Error");
    // }

    [HttpGet]
    [AllowAnonymous]
    public IActionResult ForgotPassword()
    {
        return View();
    }

    // [HttpPost]
    // [AllowAnonymous]
    // [ValidateAntiForgeryToken]
    // public async Task<IActionResult> ForgotPassword(ForgotPasswordViewModel model)
    // {
    //     if (ModelState.IsValid)
    //     {
    //         var user = await _userManager.FindByEmailAsync(model.Email);
    //         if (user == null || !(await _userManager.IsEmailConfirmedAsync(user)))
    //         {
    //             // Don't reveal that the user does not exist or is not confirmed
    //             return RedirectToAction(nameof(ForgotPasswordConfirmation));
    //         }
    //
    //         // For more information on how to enable account confirmation and password reset please
    //         // visit https://go.microsoft.com/fwlink/?LinkID=532713
    //         var code = await _userManager.GeneratePasswordResetTokenAsync(user);
    //         var callbackUrl = Url.ResetPasswordCallbackLink(user.Id, code, Request.Scheme);
    //         await _emailSender.SendPasswordResetLinkAsync(user, model.Email, callbackUrl);
    //         return RedirectToAction(nameof(ForgotPasswordConfirmation));
    //     }
    //
    //     // If we got this far, something failed, redisplay form
    //     return View(model);
    // }

    // [HttpGet]
    // [AllowAnonymous]
    // public IActionResult ForgotPasswordConfirmation()
    // {
    //     return View();
    // }

    // [HttpGet]
    // [AllowAnonymous]
    // public IActionResult ResetPassword(string code = null)
    // {
    //     return View();
    //     if (code == null)
    //     {
    //         throw new ApplicationException("A code must be supplied for password reset.");
    //     }
    //     var model = new ResetPasswordViewModel { Code = code };
    //     return View(model);
    // }

    // [HttpPost]
    // [AllowAnonymous]
    // [ValidateAntiForgeryToken]
    // public async Task<IActionResult> ResetPassword(ResetPasswordViewModel model)
    // {
    //     return View();
    //     if (!ModelState.IsValid)
    //     {
    //         return View(model);
    //     }
    //     var user = await _userManager.FindByEmailAsync(model.Email);
    //     if (user == null)
    //     {
    //         // Don't reveal that the user does not exist
    //         return RedirectToAction(nameof(ResetPasswordConfirmation));
    //     }
    //     var result = await _userManager.ResetPasswordAsync(user, model.Code, model.Password);
    //     if (result.Succeeded)
    //     {
    //         return RedirectToAction(nameof(ResetPasswordConfirmation));
    //     }
    //     AddErrors(result);
    //     return View();
    // }

    // [HttpGet]
    // [AllowAnonymous]
    // public IActionResult ResetPasswordConfirmation()
    // {
    //     return View();
    // }


    [HttpGet]
    public IActionResult AccessDenied()
    {
        return View();
    }

    [HttpGet]
    [AllowAnonymous]
    [Route("/Account/Logout")]
    public IActionResult SignedOut()
    {
        return View("Logout");
    }

    #region Helpers

    // private void AddErrors(IdentityResult result)
    // {
    //     foreach (var error in result.Errors)
    //     {
    //         ModelState.AddModelError(string.Empty, error.Description);
    //     }
    // }

    private IActionResult RedirectToLocal(string returnUrl)
    {
        if (Url.IsLocalUrl(returnUrl))
        {
            return Redirect(returnUrl);
        }

        return RedirectToAction(nameof(HomeController.Index), "Home");
    }

    #endregion
}