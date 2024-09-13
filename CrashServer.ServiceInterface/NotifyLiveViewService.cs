using ServiceStack;
using CrashServer.ServiceModel;

namespace CrashServer.ServiceInterface;

public class NotifyLiveViewService(IServerEvents serverEvents) : Service
{
    public NotifyLiveViewDataUpdatedResponse Post(NotifyLiveViewDataUpdatedRequest request)
    {
        serverEvents.NotifyChannelAsync("LiveView",  new NotifyLiveViewDataUpdatedPacket() { Id = request.Id });

        return new NotifyLiveViewDataUpdatedResponse();
    }
}