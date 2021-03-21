#import wget
#wget.download("https://raw.githubusercontent.com/pesikj/python-012021/master/zadani/5/twlo.csv")


import pandas
twilio = pandas.read_csv('twlo.csv')

print(twilio.shape)
print(twilio.iloc[:5])
print(twilio.tail())