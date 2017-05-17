"""
The datetime Library
A lot of times you want to keep track of when something happened. We can do so in Python using datetime.
Here we'll use datetime to print the date and time in a nice format.
"""
from datetime import datetime

"""
We can use a function called datetime.now() to retrieve the current date and time.

from datetime import datetime

print datetime.now()
The first line imports the datetime library so that we can use it.

The second line will print out the current date and time.
"""
from datetime import datetime

now=datetime.now()
print now

"""
Notice how the output looks like 2013-11-25 23:45:14.317454. What if you don't want the entire date and time?

from datetime import datetime
now = datetime.now()

current_year = now.year
current_month = now.month
current_day = now.day
You already have the first two lines.

In the third line, we take the year (and only the year) from the variable now and store it in current_year.

In the fourth and fifth lines, we store the month and day from now.
"""
from datetime import datetime

now=datetime.now()
current_year = now.year
current_month = now.month
current_day = now.day

print now.year
print now.month
print now.day


"""
Hot Date
What if we want to print today's date in the following format? mm/dd/yyyy. Let's use string substitution again!

from datetime import datetime
now = datetime.now()

print '%s-%s-%s' % (now.year, now.month, now.day)
# will print: 2014-02-19
Remember that the % operator will fill the %s placeholders in the string on the left with the strings in the parentheses on the right.

In the above example, we print 2014-02-19 (if today is February 19th, 2014), but you are going to print out 02/19/2014.

"""
from datetime import datetime
now = datetime.now()

print '%s/%s/%s' % (now.month, now.day, now.year)

#############################################
from datetime import datetime
now = datetime.now()

print '%s:%s:%s' % (now.hour, now.minute, now.second)


from datetime import datetime
now = datetime.now()

print '%s/%s/%s %s:%s:%s' % (now.month,now.day,now.year,now.hour, now.minute, now.second)
