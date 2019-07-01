
import requests
import json
import sys
import getopt

def fun_get_node_id(controller_ip):
	r = requests.get('http://' + controller_ip + ':8181/restconf/config/opendaylight-inventory:nodes', auth=('admin', 'admin'))
	#print(r.text)
	json_data = json.loads(r.text)
	for i in json_data['nodes']['node']:
		print(i['id'])

def fun_put_flow(controller_ip, flow_json_file, node_id):
	#r = requests.delete('http://' + controller_ip + ':8181/restconf/config/opendaylight-inventory:nodes/node/' + node_id + '/table/0', auth=('admin', 'admin'))
	f = file(flow_json_file, "ro")
	json_data = json.loads(f.read())
	#print(flow)
	for flow in json_data['flows']:
		flow_id = flow['flow'][0]['id']
		headers = {"Content-Type" : "application/json"}
		requests.put("http://" + controller_ip + ":8181/restconf/config/opendaylight-inventory:nodes/node/" + node_id + "/table/0/flow/" + flow_id, auth=('admin', 'admin'), data=json.dumps(flow), headers=headers)
		
def fun_delete_all_flow(controller_ip, node_id):
	r = requests.delete('http://' + controller_ip + ':8181/restconf/config/opendaylight-inventory:nodes/node/' + node_id + '/table/0', auth=('admin', 'admin'))

		

def main(argv):
	node_id = ""
	controller_ip = ""
	flow_json_file = ""
	get_node_id = False
	delete_all_flow = False
	
	try:
		opts, args = getopt.getopt(argv,"h",["controller_ip=","flow_json_file=","node_id=","get_node_id", "delete_all_flow"])
	except getopt.GetoptError:
		print 'Input Invalid! odl_simple_control.py --controller_ip=<Controller IP> [--flow_json_file=<file path> --node_id=<Switch_ID>] [--get_node_id]'
		sys.exit(2)
	for opt, arg in opts:
		if opt == "--node_id":
			node_id = arg
		elif opt == '-h':
			print 'odl_simple_control.py --controller_ip=<Controller IP> [--flow_json_file=<file path> --node_id=<Switch_ID>] [--get_node_id]'
		elif opt == "--controller_ip":
			controller_ip = arg
		elif opt == "--flow_json_file":
			flow_json_file = arg
		elif opt == "--get_node_id":
			get_node_id = True
		elif opt == "--delete_all_flow":
			get_node_id = True
		#print(opt + ":" + arg)
		
	if get_node_id == True:
		fun_get_node_id(controller_ip)
	elif delete_all_flow == True and node_id != "":
		fun_delete_all_flow(controller_ip, node_id)
	elif flow_json_file != "" and node_id != "":
		fun_put_flow(controller_ip, flow_json_file, node_id)


if __name__ == "__main__":
	main(sys.argv[1:])




