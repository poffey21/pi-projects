```
ping 4.2.2.2
# if no connection
sudo ifdown wlan0
sudo systemctl start dnsmasq
sudo hostapd -d /etc/hostapd/hostapd.conf

iwlist wlan0 scan

# Current SSID
iwgetid -r

```

