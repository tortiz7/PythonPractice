# var/log/syslog
# print last 10 to terimnal
# every minute

log = /var/log/syslog

while true
do
    tail -n 10 /var/log/syslog
done
