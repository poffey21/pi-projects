## Chromecast-like Hotspot ##

The intent is to recreate the Chromecast-like hotspot
which enables users connect to the Raspberry Pi when
it has not found a viable Wireless Connection in order
to add/edit connections.

Features
externalfile:gbheifiifcfekkamhepkeogobihicgmn:sftpfs:%2F%2F192%2E168%2E0%2E6:22%2Fpi:af65782add6e197fabccba3870129228318e7e7e/home/pi/pi-projects/wifi/ap/requirements_sys.txt
- Uses the iOS 'Login Required' functionality to auto-
popup window when connected to AP.
- Enables users to add/remove/edit Access Points.

### Installation ###

Install requirements_sys.txt via the OS Package Manager

```
virtualenv env
pip install -r requirements.txt
sudo env/bin/hostapd configure
```


### Applications used & Admin Commands ###

**dnsmasq**

```
# config file
/etc/dnsmasq.conf

# start service
service hostapd start

# restart service
/etc/init.d/dnsmasq restart

# log files
/var/log/dnsmasq.log

# reset config
zcat /usr/share/doc/hostapd/examples/hostapd.conf.gz | sudo tee -a /etc/hostapd/hostapd.conf

# Troubleshooting...
# - Validate that the following is in /etc/default/hostapd
DAEMON_CONF="/etc/hostapd/hostapd.conf"
```
