# Helpful Wifi Commands

See a list of available networks to connect to:

- `sudo iwlist wlan0 scan | more`

Refresh your wireless settings

`sudo ap_cli reconfigure`

File: `/etc/wpa_supplicant/wpa_supplicant.conf`

```
ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev
update_config=1

network={
	ssid="xxNAMExOFxSSIDxx"
	psk="xxUNENCRYPTEDxPASSWORDxx"
	key_mgmt=WPA-PSK
}

network={
	ssid="linksys"
	key_mgmt=NONE
}
```

Use `wpa_passphrase` to generate a new SSID & Password
```
console> wpa_passphrase "xxNAMExOFxSSIDxx" "xxUNENCRYPTEDxPASSWORDxx"

network={
	ssid="xxNAMExOFxSSIDxx"
	#psk="xxUNENCRYPTEDxPASSWORDxx"
	psk=98a0fcd2f6eee495826821d36a9401689b934e99647a61f64777d53
}
```

If you are running as root:
`wpa_passphrase "xxNAMExOFxSSIDxx" "xxUNENCRYPTEDxPASSWORDxx" >> /etc/wpa_supplicant/wpa_supplicant.conf

If you are not running as root but have access to sudo:
`wpa_passphrase "xxNAMExOFxSSIDxX" "xxUNECRYPTEDxPASSWORDxx" | sudo tee -a /etc/wpa_supplicant/wpa_supplicant.conf > /dev/null

The above command uses `tee` with `-a` to append and then the `/dev/null` prevents the screen from showing anything.

Adding the `priority` setting within a network will allow you to set 
