#show all switch connected to controller
python odl_simple_control.py --controller_ip=192.168.11.142 --get_node_id
#output: openflow:93094397149973

#insert flow on switch from json file
python odl_simple_control.py --controller_ip=192.168.11.142 --flow_json_file=flow_entry2.json --node_id=openflow:93094397149973

#delete all flow on selected switch
python odl_simple_control.py --controller_ip=192.168.11.142  --node_id=openflow:93094397149973 --delete_all_flow



