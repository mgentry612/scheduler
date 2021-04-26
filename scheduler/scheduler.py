class Event():
    def __init__(self, id, dateTime, userId):
        self.id = id
        self.dateTime = dateTime
        self.userId = userId

    def getDateTime(self):
        return self.dateTime

    def getUserId(self):
        return self.userId

class Scheduler():

    def __init__(self):
        self.calendar = {}
        self.userIdIndex = {}
        self.dateIndex = {}
        self.eventId = 0
        self.dateTimeFormat = '%Y-%m-%d %H:%M'

    def getDateTimeFormat(self):
        return self.dateTimeFormat

    def getEvents(self, userId):
        """
        Get events of a specific user
        :param userId: ID of user
        """
        events = []
        if userId in self.userIdIndex.keys():
            eventIds = self.userIdIndex[userId]

            for eventId in eventIds:
                event = self.calendar[eventId]
                responseEvent = {}
                responseEvent['date_time'] = event.getDateTime()
                responseEvent['user_id'] = event.getUserId()
                events.append(responseEvent)
            
            # Sort
            events = sorted(events, key=lambda event: event['date_time'].timestamp())

        return events
            

    def addEvent(self, dateTime, userId):
        """
        Add a single event at the date-time for the user with userId
        :param dateTime: date-time
        :param userId: ID of user
        """

        # Check for other events on same day
        dateFormat = self.getDateTimeFormat().split()[0]
        date = dateTime.strftime(dateFormat)
        if userId in self.dateIndex.keys() and date in self.dateIndex[userId].keys():
            return {
                "success": False,
                "error": "Only one event allowed on the same day.",
            }


        self.eventId += 1

        # Create new event
        event = Event(self.eventId, dateTime, userId)
        self.calendar[self.eventId] = event

        # Update user Id index
        if userId not in self.userIdIndex.keys():
            self.userIdIndex[userId] = []

        self.userIdIndex[userId].append(self.eventId)

        # Update date index
        if userId not in self.dateIndex.keys():
            self.dateIndex[userId] = {}
        self.dateIndex[userId][date] = self.eventId

        return {
            "success": True,
        }