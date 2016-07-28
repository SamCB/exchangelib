from .services import Subscribe, Unsubscribe, GetEvents

class Subscription:

    COPIED_EVENT="CopiedEvent"
    CREATED_EVENT="CreatedEvent"
    DELETED_EVENT="DeletedEvent"
    MODIFIED_EVENT="ModifiedEvent"
    MOVED_EVENT="MovedEvent"
    NEW_MAIL_EVENT="NewMailEvent"
    FREE_BUSY_CHANGED_EVENT="FreeBusyChangedEvent"

    ALL_EVENTS=[
        COPIED_EVENT,
        CREATED_EVENT,
        DELETED_EVENT,
        MODIFIED_EVENT,
        MOVED_EVENT,
        NEW_MAIL_EVENT,
        FREE_BUSY_CHANGED_EVENT
    ]

    def __init__(self, folder, events, timeout=20):

        self.sub = Subscribe(
                            protocol=folder.account.protocol,
                            # PULL is only one supported right now
                            subscription_type=Subscribe.PULL_SUBSCRIPTION
                        )

        self.subscription = self.sub.call(
                            events=events,
                            folder=folder,
                            timeout=timeout
                        )

        self.unsub = Unsubscribe(protocol=folder.account.protocol)
        self.event_getter = GetEvents(protocol=folder.account.protocol)

    def get_events(self):
        events, self.subscription = self.event_getter.call(self.subscription)
        return events

    def unsubscribe(self):
        result = self.unsub.call(self.subscription)
        return result
