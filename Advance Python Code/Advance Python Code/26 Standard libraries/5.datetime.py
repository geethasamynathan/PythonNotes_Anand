from datetime import datetime

# # 1. datetime.datetime.now()
# # Get the current date and time
# now = datetime.datetime.now()
# print(f"Current date and time: {now}")

# # 2. datetime.datetime.today()
# #  Get today's date and time
# today=datetime.today()
# print("Today's Date & time",today)


# # 3. datetime.datetime.strptime()
# #  Convert a string to a datetime object
# date_str = "2024-01-31 14:30:00"
# date_obj = datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S")
# print("Converted DateTime:", date_obj)
# # Explanation:
# # Useful when parsing date/time from user input, logs, or external data sources.


# # 4. datetime.datetime.strftime()
# # Format a datetime object as a string

# from datetime import datetime

# now = datetime.now()
# formatted_date = now.strftime("%A, %d %B %Y %I:%M %p")
# print("Formatted Date:", formatted_date)
# # 📝 Explanation:
# # Used to display dates in a human-readable format.


# # 5. datetime.datetime.date()
# # 📌 Get only the date part of a datetime object
# now = datetime.now()
# print("Date Only:", now.date())

# # 📝 Explanation:
# # Extracts only the date (YYYY-MM-DD) from a datetime object


# # 6. datetime.datetime.time()
# # 📌 Get only the time part of a datetime object
# now = datetime.now()
# print("Time Only:", now.time())

# #📝 Extracts only the time (HH:MM:SS) from a datetime object.


# # 7. datetime.timedelta
# # 📌 Perform date/time arithmetic
# from datetime import datetime, timedelta
# now = datetime.now()
# future_date = now + timedelta(days=5)
# print("5 Days Later:", future_date)

# #📝 Used for adding/subtracting time periods.

# # 8. datetime.datetime.weekday()
# # 📌 Get the day of the week (Monday = 0, Sunday = 6)
# now = datetime.now()
# print("Weekday (0=Monday):", now.weekday())

# # 📝 Useful for scheduling tasks based on the day of the week.


# # 9. datetime.datetime.isoweekday()
# # 📌 Get the ISO weekday (Monday = 1, Sunday = 7)

# now = datetime.now()
# print("ISO Weekday (1=Monday):", now.isoweekday())
# 📝 Similar to weekday(), but follows ISO conventions.

# # 10. datetime.datetime.replace()
# # 📌 Modify a part of a datetime object
# now = datetime.now()
# modified_date = now.replace(year=2028)
# print("Modified Date:", modified_date)

# #📝Useful for setting specific date/time components.

# 11. datetime.datetime.timestamp()
# 📌 Convert datetime to a Unix timestamp

now = datetime.now()
timestamp = now.timestamp()
print("Unix Timestamp:", timestamp)

#📝Converts a datetime object into seconds since January 1, 1970.



# # Format the current date
# formatted_date = now.strftime("%Y-%m-%d %H:%M:%S")
# print(f"Formatted date: {formatted_date}")

# # Parse a string to create a datetime object
# date_str = "2025-01-30 12:00:00"
# parsed_date = datetime.datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S")
# print(f"Parsed date: {parsed_date}")


# da
