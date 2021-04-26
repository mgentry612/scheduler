from datetime import datetime
from scheduler.scheduler import Scheduler

class Controller():
    def __init__(self):
        self.scheduler = Scheduler()
        self.dateTimeFormat = self.scheduler.getDateTimeFormat()

    def getEvents(self, userId):
        """
        Get events of a specific user
        :param userId: ID of user
        """
        
        # Validate userId
        if not self.isUserIdValid(userId):
            return {
                "status": 422,
                "error": "User ID is required and must be of type integer",
            }

        else:
            # Inputs valid
            events = self.scheduler.getEvents(int(userId))
            return {
                "status": 200,
                "events": events,
            }

    def addEvent(self, dateTimeStr, userId):
        """
        Add a single event at the date-time for the user with userId
        :param dateTime: date-time
        :param userId: ID of user
        """

        userId = str(userId)

        # Validate date-time
        dateTimeObj = self.getDateTimeObj(dateTimeStr)
        if dateTimeObj is None:
            return {
                "status": 422,
                "error": "Date-time must be in the format: yyyy-mm-dd hh:mm and must be on the hour or half-hour.",
            }
            

        # Validate userId
        if not self.isUserIdValid(userId):
            return {
                "status": 422,
                "error": "User ID is required and must be of type integer",
            }

        else:
            # Inputs valid
            response = self.scheduler.addEvent(dateTimeObj, int(userId))
            if response["success"]:
                return {
                    "status": 200,
                }
            else:
                return {
                    "status": 422,
                    "error": response["error"],
                }

    def isUserIdValid(self, userId):
        return (userId is not None and str.isnumeric(userId))

    def getDateTimeObj(self, dateTimeStr):
        dateTimeObj = None
        try:
            dateTimeObj = datetime.strptime(dateTimeStr, self.dateTimeFormat)
        except ValueError:
            return None
        
        if dateTimeObj.minute not in [0, 30]:
            return None
        
        return dateTimeObj