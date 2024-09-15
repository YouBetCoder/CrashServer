using ServiceStack;
using CrashServer.ServiceModel;
// ReSharper disable UnusedMember.Global

namespace CrashServer.ServiceInterface;

public class NotifyLiveViewService(IServerEvents serverEvents) : Service
{
    public NotifyLiveViewDataUpdatedResponse Post(NotifyLiveViewDataUpdatedRequest request)
    {
        serverEvents.NotifyChannelAsync("LiveView",  new NotifyLiveViewDataUpdatedPacket { Id = request.Id, TeaCup=request.TeaCup });

        return new NotifyLiveViewDataUpdatedResponse();
    }
}