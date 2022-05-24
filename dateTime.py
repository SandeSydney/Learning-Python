#Parsing String into a datetime aware object
#Use a %z with a +HHMM or -HHMM offset

import datetime

dt = datetime.datetime.strptime("2022-05-07T18:06:28+0300", "%Y-%m-%dT%H:%M:%S%z")

#Display the datetime object created
print(dt)