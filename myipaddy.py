import ipaddress

class IPAddy:
    def __init__(self, network, mask, start=10):
        self.network = ipaddress.ip_network(f"{network}/{mask}", strict=False)
        self.start = start
        self.hosts = {}
        self.current_ip = self.network.network_address+start

    def __call__(self, hostname):
        if hostname not in self.hosts:
            if self.current_ip in self.network:
                self.hosts[hostname] = str(self.current_ip)
                self.current_ip += 1
                return self.hosts[hostname]
            else:
                raise ValueError("network full")
        return self.hosts[hostname]

    def list(self):
        return [dict(host=host, ip=ip) for host, ip in self.hosts.items()]



myip = IPAddy("1.2.3.0", "255.255.255.0")

print(myip("foobar"))

print(myip.list())
