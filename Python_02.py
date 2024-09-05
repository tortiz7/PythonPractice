import psutil, time

def seconds_elapsed():
    return time.time() - psutil.boot_time()


print(f"{seconds_elapsed():0.2f}")

# Define a function for service uptime, taking total hours up and down hours as parameters
# do math! Uptim epercent is the total hours - down hours, divided by total hours, multplie by 100 (for percentage)
def service_uptime(total_hours, down_hours):
    uptime_percent = ((total_hours - down_hours) / total_hours) * 100
    return(round(uptime_percent, 2))

total_hours=float(input("How long was your service up for?: "))
down_hours=float(input("How long was your service down for?: "))

print(service_uptime(total_hours, down_hours))
