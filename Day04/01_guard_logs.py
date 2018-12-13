import os
import re
from pprint import pprint
from datetime import datetime

# Problem 1 - determine which guard sleeps the most and which minute he is asleep the most
#              return guardID * minute he sleeps the most

# Problem 2 - 

# analyze the guard logs and create hash table of month-day -> array of midnight minutes
def analyze_guard_logs(logs): 
    # convert each log in to a class that holds the date and action 
    logs = map( lambda log: Log(log), logs )
    # sort the logs in oldest to newest date order
    logs.sort(key = lambda log: log.date)
    pprint(map(lambda log: log.date, logs))

    # process the logs and create a hash table by the month date year combo with an array of all the minutes for the midnight hour
    # for each log
        # if start of new shift create entry in hash table 

        # else if guard falling asleep, set the time of falling asleep

        # if waking up, go fill in the hash table from minute he fell asleep up to minute he woke up


class Log:

    log_pattern = re.compile('(\d{4})-(\d{2})-(\d{2})\s(\d{2}):(\d{2}).\s(.*)')
    # log_pattern = re.compile('Guard')

    def __init__(self, log):
        matches = Log.log_pattern.search(log)
        if matches is not None:
            date_pieces = matches.groups()[:5]
            # get pieces of date as int to create a date
            self.year, self.month, self.day, self.hour, self.minute = map(int, date_pieces)
            self.date = datetime(self.year, self.month, self.day, self.hour, self.minute)
            # string description of the guard action
            self.action = matches.groups()[-1]
            self.action_type = self.assign_action(self.action)
        else:
            raise Exception('Could not parse data')
    
    def is_new_shift(log):
        pass

    def assign_action(self, log_action):
        # if matches Guard (#) begins shift 

        new_guard_match = re.search("Guard #(\d*) begins shift", log_action)
        if (new_guard_match):
            # assign guard id, assign type of 'BEGIN'
            print ('BEGIN SHIFT', new_guard_match.group(1))
            return

        asleep_match = re.search("falls asleep", log_action)
        if (asleep_match):
            print ('FALL ASLEEP')
            return
        
        wake_match = re.search("wakes up", log_action)
        if (wake_match):
            print ("WAKES UP")
            return 

        raise Exception('Could not assign a type to log!', log_action)
        # if matches falls asleep
            # assign type of 'START SLEEP'
        # if matches wakes up
            # assign type of 'WAKE UP'
        

def find_guard_and_minute():
    pass

def get_file_lines():
    file_name = os.path.join(os.getcwd(), 'input.txt')
    file = open(file_name, "r")
    lines = file.read().splitlines()
    return lines

if __name__ == "__main__":
    input = get_file_lines()
    test_input = """[1518-11-01 00:00] Guard #10 begins shift
[1518-11-01 00:05] falls asleep
[1518-11-01 00:25] wakes up
[1518-11-01 00:30] falls asleep
[1518-11-01 00:55] wakes up
[1518-11-01 23:58] Guard #99 begins shift
[1518-11-02 00:40] falls asleep
[1518-11-04 00:02] Guard #99 begins shift
[1518-11-04 00:36] falls asleep
[1518-11-04 00:46] wakes up
[1518-11-05 00:03] Guard #99 begins shift
[1518-11-02 00:50] wakes up
[1518-11-03 00:05] Guard #10 begins shift
[1518-11-03 00:24] falls asleep
[1518-11-03 00:29] wakes up
[1518-11-05 00:45] falls asleep
[1518-11-05 00:55] wakes up"""
    test_input = test_input.split('\n')
    # input = test_input
    print ('Result: ', analyze_guard_logs(input))