# Display Good Morning if hour is less than 12.

import time
hour = int(time.strftime("%H"))
if hour > 12:
    print(" Good Morning ")
