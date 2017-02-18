"""Get and print atomic time using NTP. Requires NTPLIB."""


import ntplib
from time import ctime
respone = ntplib.NTPClient().request('0.pool.ntp.org', version=3)
print ctime(respone.tx_time)
