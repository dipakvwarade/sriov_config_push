#!/usr/bin/python
# -*- coding: utf-8 -*-
# coding=utf-8
__author__ = "Dipak Warade <dipakvwarade@gmail.com>"
__copyright__ = "Dipak Warade <dipakvwarade@gmail.com>"

# import subprocess
# import os
# import sys
# import requests
# import time
# import datetime
import logging
from logging.handlers import TimedRotatingFileHandler
import pandas as pd
from jinja2 import Template


def xls_to_dict(underlay_data_dic,counter):
  data = {}
  #for i in range(len(underlay_data_dic["Logical_Network"])):
  data["network_name"] = underlay_data_dic["Logical_Network"][counter]
  data["vlan"] = underlay_data_dic["VLAN_ID"][counter]
  data["switch"] = underlay_data_dic["leaf"][counter]
  data["interface_display_name"] = underlay_data_dic["Leaf_port"][counter]
  data["interface"] = underlay_data_dic["interface"][counter]
  data["project_name"] = underlay_data_dic["Project_name"][counter]
  return data
 #print(data)

#     data = { "token": "961f31b218334698ab9e132d23bd0def",
#     "switch": "Leaf1",
#     "interface": "xe-0/0/9_3",
#     "vlan" : "999",
#     "interface_display_name" : "xe-0/0/9:3",
#     "network_name": "dipak_sriov",
#     "project_name": "vIMS_Project" }

f = open("demofile2.txt", "a")
f.write("Now the file has more content!")
f.close()


def main(): 
  
  file_name = "api_calls.txt"
  logHandler = TimedRotatingFileHandler(file_name,when="M",interval=10, backupCount=1000000)
  logger = logging.getLogger( 'MyLogger' )
  logger.addHandler( logHandler )
  logger.setLevel( logging.INFO )
  
  j2_template = Template(open('api_template.j2').read())
  underlay_data_dic = pd.read_excel('sriov_vlan_push_template.xlsx').to_dict()
  for i in range(len(underlay_data_dic["Logical_Network"])):
    counter = i
    f_data = xls_to_dict(underlay_data_dic,counter)
    api_call = j2_template.render(f_data)
    logger.info(api_call)
    
  

