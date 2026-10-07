def describe_day(day):
    match day:
        case "Saturday" | "saturday" | "Sunday" | "sunday":
            return "Weekend"
        case "Friday" | "friday":
            return "Almost there"
        case _:
            return "Working day"


print(describe_day("Sunday"))
print(describe_day("Friday"))
print(describe_day("Tuesday"))
print(describe_day("sunday"))
