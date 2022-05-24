## When we want to test an object if it has nothing and assigning a value if it's none
import datetime

aDate = None
if aDate is None:
    aDate = datetime.date.today()
    
    print(aDate)
