from netmiko import ConnectHandler
try:
    server_ip = "10.48.229.9"
    node_ports = ["5020", "5022"]
    print('******Getting Configs******')
    save_file = open("358configs.txt","w")
    for node in node_ports:
        device = ConnectHandler (device_type="cisco_ios_telnet", ip=server_ip, port=node, username="admin", password="P@ssw0rd!")
        device.enable(node)
        output1 = device.send_command("show running-config")
        save_file = open("358configs.txt","a")
        save_file.write(output1)
        print('******Config added for node ',(node),'!!!******')
        
    print('Closing Config File.  Saved', len(node_ports),'configuration files')
    save_file.close()
except:
    print("Save may have failed on at least one item!  Have you set up usernames and passwords?")
