# How it works 

Simple script to generate API calls to push your SRIOV config to Juniper fabric using Contrail.

The script uses pandas to process the xls and Jinja2 to render the API calls.


# Planed Improvements
- Verify leaf port is in the range [1-3] for service vlans
- Introduce a function to verify the pushed config on fabric
