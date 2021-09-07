# How it works 

Simple script to generate API calls to push your SRIOV config to Juniper fabric using Contrail.

The script uses pandas to process the xls and Jinja2 to render the API calls.


# Improvements
- Verify leaf port is in the range [1-3] for service vlans
- Introduce sleep between calls
