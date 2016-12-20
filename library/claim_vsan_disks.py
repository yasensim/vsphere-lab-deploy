#!/usr/bin/python

import requests
import ssl
from pyVim import connect
from pyVim.connect import SmartConnect
from pyVmomi import vim, vmodl

def connect_to_api(vchost, vc_user, vc_pwd):
    global service_instance
    try:
        service_instance = SmartConnect(host=vchost, user=vc_user, pwd=vc_pwd)
    except (requests.ConnectionError, ssl.SSLError):
        try:
            context = ssl.SSLContext(ssl.PROTOCOL_SSLv23)
            context.verify_mode = ssl.CERT_NONE
            service_instance = SmartConnect(host=vchost, user=vc_user, pwd=vc_pwd, sslContext=context)
        except Exception as e:
            raise Exception(e)
    return service_instance.RetrieveContent()

def get_obj(content, vimtype, name):
    obj = None
    container = content.viewManager.CreateContainerView( content.rootFolder, vimtype, True)
    for c in container.view:
        if name:
            if c.name == name:
                obj = c
                break
        else:
            obj = c
            break
    return obj

def main():

    module = AnsibleModule(
        argument_spec=dict(
            vcenter=dict(required=True, type='str'),
            user=dict(required=True, type='str'),
            passwd=dict(required=True, type='str', no_log=True),
	    cluster=dict(required=True, type='str'),
        ),
        supports_check_mode=False,
    )

    try:
        content = connect_to_api(module.params['vcenter'], module.params['user'],
                                 module.params['passwd'])
    except vim.fault.InvalidLogin:
        module.fail_json(msg='exception while connecting to vCenter, login failure, check username and password')
    except requests.exceptions.ConnectionError:
        module.fail_json(msg='exception while connecting to vCenter, check hostname, FQDN or IP')

    content = service_instance.RetrieveContent()
    cluster = get_obj(content, [vim.ClusterComputeResource], module.params['cluster'])
#    print cluster.name +", id: "+str(cluster)  
    for host in cluster.host:
#        print host.name +", id: "+str(host) 
        disk_list = []
        disks = host.configManager.vsanSystem.QueryDisksForVsan()
        for diskResult in disks:
            if diskResult.state == "eligible":
#                print ( diskResult.disk.displayName + ", SSD: " + str(diskResult.disk.ssd))
                disk_list.append(diskResult.disk)
        host.configManager.vsanSystem.AddDisks(disk=disk_list)
#        print str(host.config.vsanHostConfig.storageInfo.diskMapping) 

    return 0

from ansible.module_utils.basic import *

# Start program
if __name__ == "__main__":
    main()

