#import wget
#wget.download("https://raw.githubusercontent.com/pesikj/python-012021/master/zadani/5/twlo.csv")

import matplotlib.pyplot as plt
import pandas
twilio = pandas.read_csv("twlo.csv")

#twilio.plot("Date", "Close")
#plt.show()

twilio["Date"] = pandas.to_datetime(twilio["Date"])
twilio.plot(kind="Date", ax="Close")
plt.show()