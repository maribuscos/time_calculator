def add_time(start, duration, starting_day=None):
  # Separate the start time into time and AM/PM
  [st_time, ampm] = start.split()
  time = st_time.split(":")

  # Convert to 24-hour format if PM
  if ampm == "PM":
    hour = int(time[0]) + 12
    time[0] = str(hour)

  # Separate the duration into hours and minutes
  time_dur = duration.split(":")

  # Add hours and minutes from start time and duration
  new_hour = int(time[0]) + int(time_dur[0])
  new_minutes = int(time[1]) + int(time_dur[1])

  # Adjust for carrying over minutes to hours
  if new_minutes >= 60:
    hours_add = new_minutes // 60
    new_minutes -= hours_add * 60
    new_hour += hours_add

  # Adjust for carrying over hours to days
  days_add = 0
  if new_hour > 24:
    days_add = new_hour // 24
    new_hour -= days_add * 24

  # Convert to 12-hour format and set AM/PM
  if new_hour > 0 and new_hour < 12:
    ampm = "AM"
  elif new_hour == 12:
    ampm = "PM"
  elif new_hour > 12:
    ampm = "PM"
    new_hour -= 12
  else:  # new_hour == 0
    ampm = "AM"
    new_hour += 12

  # Add number of days later, if applicable
  if days_add > 0:
    if days_add == 1:
      days_later = " (next day)"
    else:
      days_later = " (" + str(days_add) + " days later)"
  else:
    days_later = ""

  # Determine the day of the week, if applicable
  week_days = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday",
               "Saturday", "Sunday")

  if starting_day:
    weeks = days_add // 7
    i = week_days.index(
      starting_day.lower().capitalize()) + (days_add - 7 * weeks)
    if i > 6:
      i -= 7
    day = ", " + week_days[i]
  else:
    day = ""

  # Combine all information and return result
  new_time = str(new_hour) + ":" + str(new_minutes).zfill(
    2) + " " + ampm + day + days_later

  return new_time


# print(add_time("3:00 PM", "3:10"))
# print(add_time("11:30 AM", "2:32", "Monday"))
# print(add_time("11:43 AM", "00:20"))
# print(add_time("10:10 PM", "3:30"))
# print(add_time("11:43 PM", "24:20", "tueSday"))
# print(add_time("6:30 PM", "205:12"))
# print(add_time("5:01 AM", "0:00"))
# print(add_time("8:16 PM", "466:02", "tuesday"))
