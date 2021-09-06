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

def main(): 
  underlay_data_dic = pd.read_excel('sriov_vlan_push_template.xlsx').to_dict()
  for i in range(len(underlay_data_dic["Logical_Network"])):
    counter = i
    f_data = xls_to_dict(underlay_data_dic,counter)
    
    
    
  

