using NUnit.Framework;
using ServiceStack;
using ServiceStack.Testing;
using CrashServer.ServiceInterface;

namespace CrashServer.Tests;

public class UnitTest
{
    private readonly ServiceStackHost appHost;

    public UnitTest()
    {
        appHost = new BasicAppHost().Init();
        appHost.Container.AddTransient<NotifyLiveViewService>();
    }

    [OneTimeTearDown]
    public void OneTimeTearDown() => appHost.Dispose();

    [Test]
    public void Can_call_MyServices()
    {
    
    }
}