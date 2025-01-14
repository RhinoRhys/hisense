# -*- coding: utf-8 -*-
"""
Created on Tue Jan 14 09:18:37 2025

@author: rhysh
"""

import hisense

bridgefile = "/etc/mosquitto/conf.d/hisense.conf"

class Bridge(hisense.TVAuthenticator):
    def __init__(self):
        return super().__init__()

    def write_bridge_file(self):
        lines = ["connection TV",
                 "cleansession true",
                 f"clientid {self.client_id}",
                 "start_type automatic",
                 f"address {hisense.tv_ip}:36669",
                 f"remote_username {self.username}",
                 f"remote_passwd {self.password}"]
        
        with open(bridgefile, 'w') as file:
            file.write("\n".join(lines))
        
    
print("Initializing...")
hisense.logging.info(f"Initializing")

# Initialize the TVAuthenticator class
auth = Bridge()

# Load or generate credentials
auth.load_or_generate_creds()

# Show the credentials
auth.show_credentials()

# Define hashes and topic paths
auth.define_topic_paths()

# Refresh the token if needed
auth.check_and_refresh_token()

auth.write_bridge_file()
