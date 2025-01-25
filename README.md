# Scheduler and Conference Manager Readme

## Overview
This document describes the implementation of a Conference Scheduler written in Python. The scheduler organizes events into morning and evening sessions based on their durations and predefined time constraints.

## 1. Core Components
### Classes
#### 1.1 Event
The `Event` class represents an individual talk or session.

**Attributes:**
- `name`: The title of the event.
- `duration`: The duration of the event in minutes.
- `scheduled`: A boolean indicating whether the event has been scheduled.

**Methods:**
- `__repr__`: Returns the name of the event for easy readability.

#### 1.2 Slot
The `Slot` class defines a time slot for scheduling events.

**Attributes:**
- `max`: Maximum duration allowed for the slot.
- `min`: Minimum duration required for the slot (default is 0).

**Methods:**
- `isValidEvent(event, totaltime)`: Checks if an event can fit in the slot given the current total time.
- `isValidSession(totaltime)`: Checks if the total time for the session is valid based on the slot's constraints.

#### 1.3 ConferenceManager
The `ConferenceManager` class handles reading events, scheduling them into sessions, and printing the final schedule.

**Attributes:**
- `talk_list`: A list of `Event` objects created from the input file.
- `morning`: Scheduled events for the morning sessions.
- `evening`: Scheduled events for the evening sessions.
- `perday`: Total available time per day in minutes (7 hours).

**Methods:**
- `__init__(file)`: Reads the input file and initializes the `talk_list`.
- `readInput(file)`: Parses the input file and creates `Event` objects.
- `totaltime(talk_list)`: Calculates the total time required for the list of events.
- `clear(slot_list)`: Removes scheduled events from the `talk_list`.
- `schedule(talk_list)`: Schedules events into morning and evening sessions.
- `combinations(event_list, possibledays, slot)`: Finds valid combinations of events for a given slot.
- `print_output()`: Prints the final schedule in a readable format.

## 2. Usage
### Input Format
The input file should contain a list of events, each with a title and duration in minutes (e.g., `60min`). If the event duration is not specified, it is assumed to be a lightning talk of 5 minutes.

### Example Input
```
Writing Fast Tests Against Enterprise Rails 60min
Overdoing it in Python 45min
Lua for the Masses 30min
Ruby Errors from Mismatched Gem Versions 45min
Rails for Python Developers lightning
```

### Example Output
```
Track 1:
09:00 AM Writing Fast Tests Against Enterprise Rails
10:00 AM Overdoing it in Python
10:45 AM Lua for the Masses
11:15 AM Ruby Errors from Mismatched Gem Versions
12:00 PM Lunch
01:00 PM Rails for Python Developers
04:00 PM Network
```

### Running the Scheduler
1. Create an input file (e.g., `input.txt`) with the event list.
2. Initialize the `ConferenceManager` with the file path:
   ```python
   from schedule import ConferenceManager

   c = ConferenceManager('input.txt')
   c.schedule(c.talk_list)
   c.print_output()
   ```

## 3. Key Features
1. Automatically schedules events into morning and evening sessions.
2. Handles varying event durations and ensures they fit within session constraints.
3. Includes networking and lunch breaks in the schedule.
4. Flexible design to handle unscheduled events in subsequent days.

## 4. Dependencies
- Python 3.x

## 5. Future Improvements
1. Add support for customizing session durations.
2. Optimize the scheduling algorithm for efficiency with larger datasets.
3. Improve error handling for invalid input formats.

