This script is intended to help perform automated tagging on NSX-T for VMs. 

Pre-requisites:
1) Deploy NSX-T manager
2) upload certificate to NSX-T manager
3) pip install requests

This python script use has 3 main functionalities 
- Add additional tag to VM
- remove select tag to VM 
- removes all tags from VM

This script is intended for engineers to easily use Python to perform tagging/untagging operations on NSX-T. 

Steps

1) First go to NSX-T manager and upload a self-signed certificate


