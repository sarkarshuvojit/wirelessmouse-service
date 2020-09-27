import socket
import fcntl
import struct

def get_ip_address(ifname):
    """
    Implementation from https://stackoverflow.com/a/24196955/2976015
    """
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    return socket.inet_ntoa(fcntl.ioctl(
        s.fileno(),
        0x8915,  # SIOCGIFADDR
        struct.pack('256s', bytes(ifname[:15], 'utf-8'))
    )[20:24])
