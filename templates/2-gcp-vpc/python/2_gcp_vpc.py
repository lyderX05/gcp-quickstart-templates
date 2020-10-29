def GenerateConfig(context):
    resources = [
        {
            "name": context.properties['vpc_id'] + '-vpc',
            "type": "compute.v1.network",

            "properties": {
                "autoCreateSubnetworks": False,
                "description": "A GCP VPC Network generated from templates",
                "subnetworks": [
                    "regions/{}/subnetworks/{}".format(context.properties['region'], context.properties['vpc_id'] + '-subnetwork-1'),
                    "regions/{}/subnetworks/{}".format(context.properties['region'], context.properties['vpc_id'] + '-subnetwork-2')
                ],
                "routingConfig": {
                    "routingMode": "REGIONAL"
                }
            }
        },
        {
            "name": context.properties['vpc_id'] + '-subnetwork-1',
            "type": "compute.v1.subnetwork",
            "properties": {
                "description": "A GCP VPC Subnetwork generated from templates",
                "region": context.properties['region'],
                "network": "global/networks/{}".format(context.properties['vpc_id'] + '-vpc'),
                "ipCidrRange": "10.10.0.0/20",
                "privateIpGoogleAccess": True
            },
            "metadata": {
                "dependsOn": [
                    context.properties['vpc_id'] + '-vpc',
                ]
            }
        },
        {
            "name": context.properties['vpc_id'] + '-subnetwork-2',
            "type": "compute.v1.subnetwork",
            "properties": {
                "description": "A GCP VPC Subnetwork generated from templates",
                "region": context.properties['region'],
                "network": "global/networks/{}".format(context.properties['vpc_id'] + '-vpc'),
                "ipCidrRange": "10.30.0.0/20",
                "privateIpGoogleAccess": True
            },
            "metadata": {
                "dependsOn": [
                    context.properties['vpc_id'] + '-vpc',
                ]
            }
        }
    ]

    return {'resources': resources}
