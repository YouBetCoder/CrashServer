using Funq;
using ServiceStack;
using NUnit.Framework;
using CrashServer.ServiceInterface;
// ReSharper disable UnusedMember.Global

namespace CrashServer.Tests;

public class IntegrationTest
{
    private const string BaseUri = "http://localhost:2000/";
    private readonly ServiceStackHost _appHost = new AppHost()
        .Init()
        .Start(BaseUri);

    private class AppHost() : AppSelfHostBase(nameof(IntegrationTest), typeof(NotifyLiveViewService).Assembly)
    {
        public override void Configure(Container container)
        {
        }
    }

    [OneTimeTearDown]
    public void OneTimeTearDown() => _appHost.Dispose();

    public static IServiceClient CreateClient() => new JsonServiceClient(BaseUri);

    [Test]
    public void Can_call_Hello_Service()
    {
    
    }
}