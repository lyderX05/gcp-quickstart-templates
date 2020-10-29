def GenerateConfig(context):
    resources = [
        {
            'name': context.properties['vm_id'] + '-vm',
            'type': 'compute.v1.instance',
            'properties': {
                'description': 'A Vm Properties Description',
                'tags': {
                    'items': [
                        "demo", "cloud-manager"
                    ]
                },
                'zone': context.properties['zone'],
                'machineType': 'zones/{}/machineTypes/n1-standard-1'.format(context.properties['zone']),
                'disks': [
                    {
                        'type': 'PERSISTENT',
                        'mode': 'READ_WRITE',
                        'deviceName': 'main-drive',
                        'boot': True,
                        'initializeParams': {
                            'diskName': context.properties['vm_id'] + '-vm-disk',
                            'sourceImage': context.properties['image_id'],
                            'diskSizeGb': '30',
                            'diskType': 'zones/{}/diskTypes/pd-standard'.format(context.properties['zone']),
                            'autoDelete': True
                        }
                    }
                ],
                'labels': {
                    'name': 'vm-instance',
                    'count': 1
                },
                'networkInterfaces': [ 
                    {
                        'network': 'global/networks/default',
                        'accessConfigs': [
                            {
                                'name': 'External NAT',
                                'type': 'ONE_TO_ONE_NAT'
                            }
                        ]
                    }
                ]
            }
        }
    ]
    return {"resources": resources}