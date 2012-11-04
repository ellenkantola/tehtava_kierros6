'''
Created on Aug 17, 2011

@author: santtu
'''

import datetime

class Event(object):
    '''
    The class C{Event} represents entries in a driver's
    log. Each entry consists of all the information there
    was in the file of the entry. 
    
    An event object is immutable once created; there are no
    methods to change any of its attributes.

    '''


    def __init__(self, text_line):
        '''
        Creates a new event object from the data received. 
        
        Receives one line from the log file and extracts the 
        information to object variables.
        
        The meaning of the strings in the line are(from left to right)::
        
            "Type","MPG","Date","Time","Vehicle","Odometer","Filled Up","Cost/Gallon","Gallons","Total Cost","Octane","Gas Brand","Location","Tags","Payment Type","Tire Pressure","Notes","Total Cost","Services"
        
        And one line is (for example):: 
        
            "Gas","0.0","2010-01-18","10:39 PM","Nissan Versa SL","20406","Full","$2.729","7.255","$19.80","87","Kwik Trip","","","Debit","0.0","","$19.80",""
        
        Types of the fields are as follows.
        Common fields for all entries::
        
             type: string
             date: a date object        
             time: a time object with hours an minutes       
             vehicle: string
             odometer: integer
             gas brand: string
             location: string
             payment type: string
             tire pressure: float
             notes: string
             total cost: float
        
        Fields for service entry::
        
             tags: string
             service: string, multiple operations separated by comma
        
        Fields for refueling entry::
        
             mpg: float
             filled up: string
             cost/gallon: float
             gallons: float
             total_cost 1: float
             octane: int

        @param text_line: one line from the log file as it is there.
        '''
        '''
        @todo: handle the line so, that the values are in a list 'data_list'
        @todo: the first value Service or Gas goes to the object variable 'type'
        @todo: the second value mpg is ignored. Don't do anything with it.
        @todo: the third value date has to be transformed to a date object and 
                saved to the variable 'date'.
        @todo: the fourth value time needs to be converted into the 24 h format 
                and the resulting time object saved into 'time'
        '''     
        data_list=text_line.split(",")
        
        self.type=data_list[0]
        self.date=datetime.date(data_list[1][0:4],data_list[1][5:7], data_list[1][8:10])
        
        self.vehicle = data_list[4]
        self.miles = int(data_list[5])
        self.brand = data_list[11]
        self.location = data_list[12]
        self.payment_type = data_list[14]
        self.tire_pressure = float(data_list[15])
        self.notes = data_list[16]
        self.total_cost = float(data_list[17][1:])
        if self.type == 'Service':
            self.tags = data_list[13]
            '''
            @note: variable service is a string, where different 
            service tasks are separated by a comma.
            for example: , 'oil change', 'inspection'] becomes 'oil change, inspection'
            '''
            self.service = ', '.join(data_list[18:])
        if self.type == 'Gas':
            self.mpg = float(data_list[1])
            self.filled_up = data_list[6]
            self.cost_per_callon = float(data_list[7][1:])
            self.gallons = float(data_list[8])
            self.gas_cost = float(data_list[9][1:])
            self.octane = data_list[10]


    def get_type(self):
        '''
        Returns the type of the entry.
        @return: entry type
        @rtype: string
        '''
        return self.type
        
    def get_date(self):
        '''
        Returns the date of the entry.
        @return: entry date
        @rtype: date object
        '''
        return self.date
        
    def get_time(self):
        '''
        Returns the time of the entry.
        @return: entry time
        @rtype: time object
        '''
        return self.time
        
    def get_miles(self):
        '''
        Returns the number of miles in the entry moment.
        @return: odometer reading
        @rtype: int
        '''
        return self.miles
        
    def get_gallons(self):
        '''
        Returns the amount of gallons used to fill in the tank.
        @return: haw many gallons
        @rtype: float
        '''
        return self.gallons
        
    def get_brand(self):
        '''
        Returns the pruduct brand used in refuelling/oil change.
        @return: product brand
        @rtype: string
        '''
        return self.brand
        
    def get_total_cost(self):
        '''
        Returns the total cost of the entry.
        @return: total costs
        @rtype: float
        '''
        return self.total_cost
        
    def get_service(self):
        '''
        Returns the list of service tasks done.
        @return: service tasks
        @rtype: string
        '''
        return self.service
