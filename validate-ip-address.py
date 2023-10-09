class Solution:
    def validIPAddress(self, queryIP: str) -> str:
        
        def ip4(n):
            try:
               
                return  0 <= int(n) <= 255 and str(int(n)) == n
            except:
                return False

        def ip6(n):
            if len(n) > 4:
                return False
            if re.match('\W',n):
                return False
            
            try:
                int(n,16)
                return True
            except:
                return False


        ipv4 = queryIP.split('.')
        ipv6 = queryIP.split(':')

        if len(ipv4) == 4 and all(ip4(n) for n in ipv4):
            return 'IPv4'
        
        if len(ipv6) == 8 and all(ip6(n) for n in ipv6):
            return "IPv6"
        return "Neither"