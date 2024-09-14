using Microsoft.AspNetCore.Authorization;
using Microsoft.AspNetCore.Mvc;
using ServiceStack.Mvc;

namespace CrashServer.Controllers;


[Authorize]

public class DataController( IWebHostEnvironment env) : ServiceStackController
{
 

    [HttpGet]
    [Authorize]
    public IActionResult Results() => View();

    [HttpGet]
    [Authorize]
    public IActionResult Predictions() => View();

    [HttpGet]
    [Authorize]
    public IActionResult LiveView() => View();

    
    
 
}
