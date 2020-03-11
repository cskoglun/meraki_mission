"""The provided sample code in this repository will reference this file to get the
information needed to connect to your lab backend.  You provide this info here
once and the scripts in this repository will access it as needed by the lab.
Copyright (c) 2019 Cisco and/or its affiliates.
Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:
The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

# Libraries
from pprint import pprint
import requests
import os, sys, json
from webexteamssdk import WebexTeamsAPI


# Get the absolute path for the directory where this file is located "here"
here = os.path.abspath(os.path.dirname(__file__))

# Get the absolute path for the project / repository root
project_root = os.path.abspath(os.path.join(here, ".."))

# Extend the system path to include the project root and import the env files
sys.path.insert(0, project_root)

# Import env_user.py as a module
import env_user

# WEBEX TEAMS LIBRARY
teamsapi = WebexTeamsAPI(access_token=env_user.WT_ACCESS_TOKEN)

# Function that returns data from the Meraki Dashboard. Argument variable is a URL.
def get_data(url):
    
    headers = {
    'Content-Type' : 'application/json',
    'X-Cisco-Meraki-API-Key' : env_user.MERAKI_API_KEY,
    }

    response = requests.get(url,headers=headers)
    json_data = response.text
    data = json.loads(json_data)
    return data

# Function that returns an ID for a specific item of the data set. Argument variables are the data set and a name 
def get_id(data,name):
    for i in range(0,len(data)):
        if data[i]['name'] == name:
            id_nr = data[i]['id']
            return id_nr
    return 0


######## MISSION TODO : finish the Meraki base url 
base_url = "https://CHANGEME/api/v0"

######## MISSION TODO : modify the url so that you can retrieve all organizations you have access to
url_org = base_url + "/CHANGE_ME"

# Utilizing the get_data() function in order to retrieve a data set of all organizations you have access to
data_organizations = get_data(url_org)

# Name of organization we are going to be working with
org_name = "DeLab"

######## MISSION TODO : What argument variable do you need input into the get_id function in order to retrieve the org ID?
org_ID = get_id(data_organizations,CHANGEME)

######## MISSION TODO : modify the url so that you can retrieve all networks for a specific organization
url_network = url_org + '/CHANGEME'

######## MISSION TODO : state the correct function you need in order to retrieve network data
data_networks = CHANGEME(url_network)

######## MISSION TODO : create a variable. Datatype = string. Value = name of network
network_name = 'CHANGEME'

######## MISSION TODO : state the correct function you need in order to retrieve the network ID
network_ID = CHANGEME(data_networks,network_name)

######## MISSION TODO : modify the url so that you can retrieve all devices for a specific network
url_devices = url_network + '/CHANGEME'

######## MISSION TODO : state the correct function you need in order to retrieve device data
data_devices = CHANGEME(url_devices)

# Creating a list of device platform information with the help of a for loop
devices = []
for item in range(0,len(data_devices)):
    devices.append(data_devices[item]['model'])

######## MISSION TODO : print the device list


######## MISSION TODO : modify the url so that you can retrieve failed connections for a specific network
url_fail_conn = base_url + '/networks/' + CHANGEME + '/failedConnections?t0=1583148210&t1=1583753010'

# Utilizing the get_data() function in order to retrieve failed connections within a given time stamp
fail_conn = get_data(url_fail_conn)

######## MISSION TODO (LAST MISSION) : print all failed connections for a specific network within a given time stamp



if not fail_conn or len(devices)==0:
    print("You have not yet fulfilled the mission")
else:
    print("Congratulations! Check your WT space ;) ")
    teamsapi.messages.create(
                        env_user.WT_ROOM_ID,
                        text="I finished the beginner level mission! YEY!",
                    )
