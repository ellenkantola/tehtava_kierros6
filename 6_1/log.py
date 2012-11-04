
from event import Event

class Log(object):
    '''
    This class C{Log} represents a driver's log. Each log consists of the
    number of operations that has been done to a car. Operations can be
    refuelling and service.
    '''


    def __init__(self, log_file):
        '''
        Creates a new log book. Opens and reads a file where
        all the events have been saved in csv format. Each event
        is in its own row. Fields in a row are enclosed in quotation marks ("")
        and separated by a comma (,). The first row of the file has column titles,
        that are just read from the file and not used anywhere.
        
        The file is read one line at the time and the line is send to the Event class.
        Event class parses the line and returns an object representing that event.
        The received event object is added to a list of events.
        
        @param log_file: file name of the file containing the log information
        @type log_file: string
        '''
        self.events = []
        data = open(log_file, 'r')
        data.readline()
        for line in data:
            self.events.append(Event(line))
        data.close()
    
    def get_all_events(self):
        '''
        Returns the list of all the events.
        
        @return: list of all events
        @rtype: list of event objects
        '''
        return self.events    

    def get_services(self):
        '''
        Searches for service entries in the log. Creates a string representation of each service entry,
        where first is date of the entry, then miles and last, operations done. These are separated by a semicolon.
        If there are more service entries, they are simply added to the string (the newline character of the
        original file is still after the service field). So different service entries are separated by a
        new line.
        
        @return: a string representing all service entries in the log. Entries separated by a new line, 
                fields in one entry by ;. 
        @rtype: string
        '''
        all_services = ''
        for event in self.events:
            if event.get_type() == 'Service':
                all_services += str(event.get_date()) + ';' + str(event.get_miles()) + ';' + event.get_service()
        return all_services
    
    def get_average_consumption(self):
        '''
        Calculates the average consumption from the log. Calculated 
        from the actual miles and gallons instead of averaging the consumptions from the events. 
        For example, if the file looks as follows::
        
            "Type","MPG","Date","Time","Vehicle","Odometer","Filled Up","Cost/Gallon","Gallons",...
            "Service","0.0","2009-11-19","12:30 PM","Suzuki S40","3560","","$0.000","0.000",...
            "Gas","0.0","2009-11-12","6:55 AM","Suzuki S40","3480","Full","$2.629","1.427",...
            "Gas","56.1","2009-10-28","4:13 PM","Suzuki S40","3400","Full","$2.729","2.200",...
            "Gas","54.5","2009-09-07","8:03 PM","Suzuki S40","3280","Full","$2.459","1.914",...
            "Service","0.0","2009-09-01","10:00 AM","Suzuki S40","3200","","$0.000","0.000",...
            "Gas","52.2","2009-08-23","3:44 PM","Suzuki S40","3180","Full","$2.529","1.429",...
            "Gas","53.9","2009-08-03","6:35 PM","Suzuki S40","3103","Full","$2.589","1.232",...
            "Gas","52.8","2009-07-21","10:53 AM","Suzuki S40","3038","Full","$2.379","1.536",...

        Note that the first event is the lowest one (last in the list).
        
        Find the first actual refueling event (2009-07-21). Then go through the list and sum up all gallons from the Gas events except the first one (2009-07-21). Get the miles from the last "Gas" event and subtract miles of the first event from it. These are the driven miles.
        
        @return: the average fuel consumption as miles/gallon
        @rtype: float
        '''
        '''
        @todo: write a code that calculates the fuel consumption as miles/gallon.
        '''
    


if __name__ == '__main__':
    '''
    This is for testing the class.
    '''
#     my_car = Log('../../Toyota4Runner.csv')
#     my_car = Log('../../SuzukiS40.csv')
    my_car = Log('NissanVersa.csv')
    print my_car.get_services()
    print my_car.get_average_consumption()
    
