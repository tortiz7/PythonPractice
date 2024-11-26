KuraCafe={
    "Pastries":{"Croissant":{"Price":"$3.00","Ingredients":["Flour","Butter","Eggs"]}},
    "Entrees":{"BaconEgg&Cheese":{"price":"$7.50","Ingredients":["Bagel","Cheese","Eggs","Bacon"]}},
    "Desserts":{"Cheesecake":{"price":"$10.00","Ingredients":["Crust","Cream cheese","Eggs","Blueberries"]}},
    "Bevs":{"Drip COffee":{"Price":"$3.00","Ingredients":["Colombian Coffee Bean","Water"]}},
}
print(KuraCafe["Pastries"]["Croissant"]["Ingredients"])

server_config = {
    "hostname": "Kura-server",         
    "ip_address": ["192.168.1.10"],         
    "port": 8080,   
    "uptime": 99.98,              
    "ssh_enabled": True,                  
    "supported_protocols": ["HTTP", "HTTPS"]
}

print(server_config.values()) #here, server_config is an OBJECT, and the .values are METHODS since they are values relating to an Object

