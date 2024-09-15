using Microsoft.AspNetCore.Authorization;
using Microsoft.AspNetCore.Mvc;
using ServiceStack.Mvc;

namespace CrashServer.Controllers;


[Authorize]
//IWebHostEnvironment env
public class DataController : ServiceStackController
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
