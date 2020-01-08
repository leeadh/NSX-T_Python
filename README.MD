This script is intended to help perform automated tagging on NSX-T for VMs. 

Pre-requisites:
1) Deploy NSX-T manager
2) upload certificate to NSX-T manager
3) pip install requests

This python script use has 3 main functionalities 
- Add a tag to VM [```addnewtag_VMs(json_data,new_tag)```]
- remove select tag to VM  [```removespecifictag_VMs(json_data,scopetoberemoved,tagtoberemoved)```]
- removes all tags from VM [```removealltags_VMs(json_data)```]

This script is intended for engineers to easily use Python to perform tagging/untagging operations on NSX-T with the use of the certificates instead of using passwords and usernames. 

## Add a tag to VM [```addnewtag_VMs(json_data,new_tag)```]

In this example, I am going to add a new tag to my VMs with the function ```addnewtag_VMs(json_data,new_tag)```.  

1) First go to NSX-T manager and upload a self-signed certificate (in this case I am using pi-nsx-t-superuser). For generation of a self-signed cert, please refer to this link: https://docs.vmware.com/en/VMware-Validated-Design/5.0.1/com.vmware.vvd.sddc-nsxt-domain-deploy.doc/GUID-3F545B7F-97DA-4527-AB45-9B01FDABC653.html

![NSX-Tmanager](https://github.com/leeadh/NSX-T_Python/blob/master/screenshots/nsx-t%20manager.png)

2) Now that its ready, we can run our simple python script to perform the tagging operations on NSX-T. This script is relying on the requests libray in Python. Hence, it is necessary to do a `pip install requests`. (I am running `Python 3.8` in my environment)

3) Scroll to the NSX-T manager and you can see there are no tags assigned to the VMs

![VMsbeforetagging](https://github.com/leeadh/NSX-T_Python/blob/master/screenshots/VMsbeforetagging.png)

4) We will now add a new tag to all VMs in scope with the tag "allow access" and scope "yes".  To do so 

```new_tag= {"scope": "yes", "tag": "allow_access"}```

5) We can see now that NSX-T has been tagged with the approriate tag and scope

![VMsaftertagging](https://github.com/leeadh/NSX-T_Python/blob/master/screenshots/VMsaftertagging.png)

## Remove a selected tag to VM [```removespecifictag_VMs(json_data,scopetoberemoved,tagtoberemoved)```]

1) We now have 2 tags tagged to the VMS

![dualtags](https://github.com/leeadh/NSX-T_Python/blob/master/screenshots/dualtags.png)

2) We are going to remove a selected tag "windows_version" and scope "10" from the VM. Run the method ```removespecifictag_VMs(json_data,scopetoberemoved,tagtoberemoved)``` with values ```removespecifictag_VMs(json_data,"10","windows_version")```

3) Tag has been removed 

![taggedremoved](https://github.com/leeadh/NSX-T_Python/blob/master/screenshots/VMsaftertagging.png)

## Remove all tags to VM [```removespecifictag_VMs(json_data,scope,tag)```]

1) Execute the function ```removespecifictag_VMs(json_data,scope,tag)```

2) All tags has been removed
