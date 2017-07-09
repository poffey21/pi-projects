from subprocess import call
from subprocess import Popen, PIPE, STDOUT
from collections import OrderedDict

WPA_SUPPLICANT = """
ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev
update_config=1

network={
        ssid="%s"
        psk="%s"
        key_mgmt=WPA-PSK
}
"""

class Wireless(object):
    supplicant_file = '/etc/wpa_supplicant/wpa_supplicant.conf'
    
    def __init__(self, interface):
        self.interface = interface
    
    def connect(self, ssid, password):
        """ takes an ssid and password and saves it to wpa_supplicant """
        content = WPA_SUPPLICANT % (ssid,password,)
        # sudo chmod 666 /etc/wpa_supplicant/wpa_supplicant.conf
        with open(self.supplicant_file, 'w') as f:
            f.write(content)
        p = Popen('ifdown {}'.format(self.interface), shell=True, stdout=PIPE, stderr=STDOUT)
        for line in p.stdout.readlines():
            output += line
        retval = p.wait()
        p = Popen('ifup {}'.format(self.interface), shell=True, stdout=PIPE, stderr=STDOUT)
        for line in p.stdout.readlines():
            output += line
        retval = p.wait()

    def _eval_line(self, line):
        """ take an individual line and return the key/value pair(s) """
        valid_keys = ['Address', 'Group Cipher', 'ESSID', 'Quality', 'Encryption key', 'Frequency']
        for key in valid_keys:
            if line.strip().startswith(key):
                break
        else:
            return {}
    
        if ':' in line:
            x, y = line[:line.index(':')].strip().strip('"'), line[line.index(':')+1:].strip().strip('"')
            if not y:
                return {}
            return {x: y}
        
        if line.strip().startswith('Quality'):  # Quality=88/100  Signal level=42/100
            return {
                "Quality": line[line.index('=')+1:].split(' ')[0],
                'Signal Level': line[line.rindex('=')+1:],
            }
            
        return {}
           
    def _eval_output(self, output):
        """ takes the output from scan and returns a Python object  """
        first_line_output = None
    
        cells = []
    
        cell_name_sample = 'Cell 01 - '
        cell_prefix_sample = '          '
        
        temp_out = {}
        for line in output.split('\n'):
            if first_line_output is None:
                first_line_output = line
                continue
            if line.strip().startswith('Cell '):
                if temp_out:
                    cells.append(temp_out)
                line = line[line.index(' - ')+2:]
                temp_out = {}
            temp_out.update(**self._eval_line(line.strip()))
        
        if temp_out:
            cells.append(temp_out)
        
        return cells
        
    def scan(self):
        output = ""
        p = Popen('iwlist {} scan'.format(self.interface), shell=True, stdout=PIPE, stderr=STDOUT)
        first_line = True
        for line in p.stdout.readlines():
            output += line
        retval = p.wait()
        if retval == 0:
            output = self._eval_output(output)
            return output
        else:
            print('error returning: {}'.format(retval))
            return output

def main():
    """accepts one argument a network interface"""
    interface = 'wlan0'
    wifi = Wireless('wlan0')
    output = wifi.scan()
    wifi.connect('testing', '12345678')


if __name__ == '__main__':
    main()
