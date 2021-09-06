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

underlay_data_dic = pd.read_excel('sriov_vlan_push_template.xlsx').to_dict()

def xls_to_dict(underlay_data_dic):
  for i in range(len(my_dic["Logical_Network"])):
     data["virtual_network"] = my_dic["Logical_Network"][i]
     data["vlan"] = my_dic["VLAN_ID"][i]
     data["switch"] = my_dic["leaf"][i]
     data["interface_display_name"] = my_dic["Leaf_port"][i]
     data["interface"] = my_dic["interface"][i]
     return data
  
      
      
