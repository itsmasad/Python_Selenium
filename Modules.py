# A module is basically a file containing a set of functions to include in your application.
# There are core python modules, modules you can install using pip package manager (incuding Django) as well as custom modules

# Importing date time module
import datetime
today = datetime.date.today()
print(today)

# Another way of importing directly date from the datetime
from datetime import date
today1 = date.today()
print(today1)