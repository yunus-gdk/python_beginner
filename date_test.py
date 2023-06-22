import dateparser
from datetime import datetime

print(dateparser.parse("Il y a un mois"))

now = datetime.now()
print(now.strftime("%d %B %Y"))