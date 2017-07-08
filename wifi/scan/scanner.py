from subprocess import call
from subprocess import Popen, PIPE, STDOUT

def scan(interface):
    output = ""
    p = Popen('iwlist {} scan'.format(interface), shell=True, stdout=PIPE, stderr=STDOUT)
    for line in p.stdout.readlines():
        output += line
    retval = p.wait()
    if retval == 0:
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
