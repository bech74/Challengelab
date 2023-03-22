from netmiko import ConnectHandler
sshCli = ConnectHandler(
    device_type="cisco_ios",
    host="192.168.56.104",
    port="22",
    username="cisco",
    password="cisco123!",
)
# Goes directly into
command = []

command.append("do show ip interface brief")

command.append("interface loopback 7")

command.append("ip address 14.15.16.17 255.255.255.0")

command.append("exit")

command.append("do sh run interface lo7")

output = sshCli.send_config_set(command)

print(output)
