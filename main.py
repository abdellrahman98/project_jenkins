import yaml
from jinja2 import Environment, FileSystemLoader
from netmiko import ConnectHandler
env = Environment(loader=FileSystemLoader("."))

print("\n Welcome to my First Project \n")

hi = input("Do you want bgp or ospf or static protocol : ")

if hi == "bgp" :
    with open("bgp.yaml") as file1:
        data1 =yaml.load(file1, Loader=yaml.FullLoader)
    temp = env.get_template("bgp.j2")
    P1= temp.render(a=data1)
    vxr = ConnectHandler(host="192.168.1.21", username="abdo", password="abdo", device_type="cisco_ios")
    vxr.enable()
    vxr.config_mode()
    vxr.send_command_timing(P1)
    output = vxr.send_command_timing("do show bgp summary")
    print(output)
elif hi == "ospf" :
    with open("ospf.yaml") as file2:
        data2 = yaml.load(file2, Loader=yaml.FullLoader)
    temp = env.get_template("ospf.j2")
    P2 = temp.render(a=data2)
    vxr = ConnectHandler(host="192.168.1.21", username="abdo", password="abdo", device_type="cisco_ios")
    vxr.enable()
    vxr.config_mode()
    vxr.send_command_timing(P2)
    output = vxr.send_command_timing("do show run")
    print(output)
elif hi == "static" :
    with open("static.yaml") as file3:
        data3 = yaml.load(file3, Loader=yaml.FullLoader)
    temp = env.get_template("static.j2")
    P3 = temp.render(a=data3)
    vxr = ConnectHandler(host="192.168.1.21", username="abdo", password="abdo", device_type="cisco_ios")
    vxr.enable()
    vxr.config_mode()
    vxr.send_command_timing(P3)
    output = vxr.send_command_timing("do show run")
    print(output)
else:
    print(" please write only protocols :  bpg or ospf or staic only !!!")


