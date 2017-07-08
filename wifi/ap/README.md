## Chromecast-like Hotspot ##

The intent is to recreate the Chromecast-like hotspot
which enables users connect to the Raspberry Pi when
it has not found a viable Wireless Connection in order
to add/edit connections.

Planned Features

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
sudo systemctl start dnsmasq

# restart service
sudo systemctl restart dnsmasq

# log files
/var/log/dnsmasq.log

# reset config
zcat /usr/share/doc/hostapd/examples/hostapd.conf.gz | sudo tee -a /etc/hostapd/hostapd.conf

# Troubleshooting...
# - Validate that the following is in /etc/default/hostapd
DAEMON_CONF="/etc/hostapd/hostapd.conf"

```

**hostapd**

```
# config file
/etc/dnsmasq.conf

# set it as a service

# start service
sudo systemctl start hostapd

# restart service
sudo systemctl restart hostapd

# Troubleshooting...
# - getting the edimax usb driver to work.
[tutorial](https://www.daveconroy.com/turn-your-raspberry-pi-into-a-wifi-hotspot-with-edimax-nano-usb-ew-7811un-rtl8188cus-chipset/)
```

**network interfaces**

```

# restart particular interface
sudo ifdown wlan0

# restart all interfaces
/etc/init.d/networking restart
```


## Sources

[Restarting Network Interfaces](http://ccm.net/faq/1141-restart-network-interface-using-command-lines-in-linux)

[Getting Edimax to work](https://www.daveconroy.com/turn-your-raspberry-pi-into-a-wifi-hotspot-with-edimax-nano-usb-ew-7811un-rtl8188cus-chipset/)

http://www.pihomeserver.fr/en/2014/05/22/raspberry-pi-home-server-creer-hot-spot-wifi-captive-portal/

https://learn.adafruit.com/setting-up-a-raspberry-pi-as-a-wifi-access-point/install-software

https://www.the-hawkes.de/dnsmasq-a-local-dnsdhcp-server-on-raspberry-pi.html

http://www.elinux.org/RPI-Wireless-Hotspot

https://seravo.fi/2014/create-wireless-access-point-hostapd

