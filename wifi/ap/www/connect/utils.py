from subprocess import call
from subprocess import Popen, PIPE, STDOUT

def _eval_line(line):
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
            "Quality": line[line.index('='):].split(' ')[0],
            'Signal Level': line[line.rindex('='):],
        }
        
    return {}
       

def _eval_output(output):
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
        temp_out.update(**_eval_line(line.strip()))
    
    if temp_out:
        cells.append(temp_out)
    
    return cells
    

def scan(interface):
    output = ""
    p = Popen('iwlist {} scan'.format(interface), shell=True, stdout=PIPE, stderr=STDOUT)
    first_line = True
    for line in p.stdout.readlines():
        output += line
    retval = p.wait()
    if retval == 0:
        output = _eval_output(output)
        return output
    else:
        print('error returning: {}'.format(retval))
        return output

def main():
    """accepts one argument a network interface"""
    interface = 'wlan0'
    #return_code = call(["iwlist", interface, "scan"], shell=True)
    output = scan(interface)
    print(output)


if __name__ == '__main__':
    main()
