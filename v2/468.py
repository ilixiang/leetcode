#!/usr/bin/python3

def validIPAddress(queryIP):
    if '.' in queryIP:
        ipParts = queryIP.split('.')
        if len(ipParts) != 4:
            return 'Neither'
        for ipPart in ipParts:
            if not ipPart.isnumeric():
                return 'Neither'
            ipPartNum = int(ipPart)
            if (ipPartNum == 0 and len(ipPart) != 1) or (ipPartNum != 0 and ipPart[0] == '0'):
                return 'Neither'
            if ipPartNum < 0 or ipPartNum > 255:
                return 'Neither'
        return 'IPv4'
    else:
        ipParts = queryIP.split(':')
        if len(ipParts) != 8:
            return 'Neither'
        for ipPart in ipParts:
            if len(ipPart) > 4 or len(ipPart) < 1:
                return 'Neither'
            for c in ipPart:
                b = c.encode()[0]
                if not ((b <= 70 and b >= 65) or (b <= 102 and b >= 97) or (b <= 57 and b >= 48)):
                    return 'Neither' 
        return 'IPv6'
