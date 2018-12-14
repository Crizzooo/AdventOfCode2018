import os
import re
from pprint import pprint
from datetime import datetime

FALL_ASLEEP = "FALL ASLEEP"
WAKE_UP = "WAKES UP"
BEGIN_SHIFT = "BEGIN SHIFT"

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

# Problem 1 - determine which guard sleeps the most and which minute he is asleep the most
#              return guardID * minute he sleeps the most

# Problem 2 - 

# analyze the guard logs and create hash table of month-day -> array of midnight minutes
def create_guard_schedule(logs): 
    # convert each log in to a class that holds the date and action
    logs = map(lambda log: Log(log), logs )
    # print('hi')
    # sort the logs in oldest to newest date order
    logs.sort(key=lambda log: log.date)
    # pprint(map(lambda log: log.action, logs))
    schedule = {}

    # process the logs and create a hash table by the month date year combo with an array of all the minutes for the midnight hour
    # for each log
    current_guard = None
    min_asleep = None

    for log in logs:
        date = log.date_code
        # if we havent seen this day before
        if date not in schedule:
            # print('creating minute log for date: ', date)
            schedule[date] = {
                "minutes": create_minute_log(),
                "guard_id": None
            }
    
        
        # update the current guard if beginning shift 
        if (log.action_type == BEGIN_SHIFT):
            current_guard = log.guard_id
            # print('new guard clocking in ' + str(current_guard))

        # else if guard falling asleep, set the time of falling asleep
        # guards can only fall asleep on their own day, so lets set guard id of the day the first time the guard falls asleep
        if (log.action_type == FALL_ASLEEP):
            min_asleep = log.minute
            if (schedule[date]['guard_id']is None):
                schedule[date]['guard_id']= current_guard
            # print ('Current Guard ' + str(current_guard) + ' falls asleep at ' + str(min_asleep))

        # if waking up, go fill in the hash table between the minute he fell asleep up to minute he woke up
        if (log.action_type == WAKE_UP):
            wake_up_minute = log.minute
            # print ('Current Guard ' + str(current_guard) + ' wakes up at ' + str(min_asleep))
            for minute in range(min_asleep, wake_up_minute):
                schedule[date]['minutes'][minute] = '#'
            min_asleep = None

    return schedule

    def handle_begin_shift(log):
        pass 

    def handle_fall_asleep(log):
        pass
    
    def handle_wake_up(log):
        pass


def analyze_guard_schedule(schedule):
    # go through each day in schedule
    guard_hash = {}

    secret_code = 0
    guard_most_asleep = ""
    guard_frequent_minute = ""

    for day in schedule:
        day_obj = schedule[day]
        guard = day_obj['guard_id']
        minutes = day_obj['minutes']
        if guard not in guard_hash:
            guard_hash[guard] = {
                "minutes_asleep": 0,
                "minute_hash": create_minute_hash(),
                "guard_id": guard
            }
        guard_stats = guard_hash[guard]
        for minute, is_asleep in enumerate(minutes):
            if is_asleep == '#':
                guard_stats['minutes_asleep'] += 1
                guard_stats['minute_hash'][minute] += 1
        # go over the minutes for the day 
            # if asleep add to minute
            # add to guard minute hash
    max_minutes_asleep = 0
    guard_most_asleep  = ""
    all_guard_stats = map( lambda guard_id: guard_hash[guard_id], guard_hash.keys() )
    for guard_stat in all_guard_stats:
        if (guard_stat['minutes_asleep'] > max_minutes_asleep):
            guard_most_asleep = guard_stat['guard_id']

    most_frequent_minute_total = -1
    most_frequent_minute = -1
    for minute in guard_hash[guard_most_asleep]['minute_hash'].keys():
        asleep_count = guard_hash[guard_most_asleep]['minute_hash'][minute]
        # print('minute: ', minute, ' asleep count', asleep_count)
        if asleep_count > most_frequent_minute_total:
            most_frequent_minute_total = asleep_count
            most_frequent_minute = minute
    secret_code = int(guard_most_asleep) * int(most_frequent_minute)
    return secret_code


class Log:

    log_pattern = re.compile('(\d{4})-(\d{2})-(\d{2})\s(\d{2}):(\d{2}).\s(.*)')
    guard_id_pattern = re.compile('Guard\s#(\d*)\s')
    # log_pattern = re.compile('Guard')

    def __init__(self, log):
        matches = Log.log_pattern.search(log)
        if matches is not None:
            date_pieces = matches.groups()[:5]
            # combine YYYY-MM-DD to set a date code used for hashing
            self.date_code = "-".join(matches.groups()[:3])
            # get pieces of date as int to create a date
            self.year, self.month, self.day, self.hour, self.minute = map(int, date_pieces)
            self.date = datetime(self.year, self.month, self.day, self.hour, self.minute)
            # string description of the guard action
            self.action = matches.groups()[-1]
            self.guard_id = None
            self.action_type = self.get_action_type()
        else:
            raise Exception('Could not parse data')

        if (self.action_type == BEGIN_SHIFT):
            self.guard_id = Log.guard_id_pattern.match(self.action).group(1)

    
    def get_action_type(self):
        # if matches Guard (#) begins shift 
        log_action = self.action;

        new_guard_match = re.search("Guard #(\d*) begins shift", log_action)
        if (new_guard_match):
            # assign guard id, assign type of 'BEGIN'
            return BEGIN_SHIFT

        asleep_match = re.search("falls asleep", log_action)
        if (asleep_match):
            return FALL_ASLEEP
        
        wake_match = re.search("wakes up", log_action)
        if (wake_match):
            return WAKE_UP

        raise Exception('Could not assign a type to log!', log_action)



def find_guard_and_minute():
    pass

def get_file_lines():
    file_name = os.path.join(os.getcwd(), 'input.txt')
    file = open(file_name, "r")
    lines = file.read().splitlines()
    return lines

def create_minute_log():
    minutes = []
    for i in range(0, 60):
        minutes.append('')
    return minutes

def create_minute_hash():
    minute_hash = {}
    for minute, val in enumerate(create_minute_log()):
        minute_hash[minute] = 0
    return minute_hash

if __name__ == "__main__":
    input = get_file_lines()
    test_input = test_input.split('\n')
    # input = test_input
    print ("making schedule")
    schedule = create_guard_schedule(input)
    print ('made schedule')
    print(analyze_guard_schedule(schedule))
    # pprint(schedule)