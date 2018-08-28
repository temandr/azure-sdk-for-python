# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from .resource_py3 import Resource


class HubVirtualNetworkConnection(Resource):
    """HubVirtualNetworkConnection Resource.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :param id: Resource ID.
    :type id: str
    :ivar name: Resource name.
    :vartype name: str
    :ivar type: Resource type.
    :vartype type: str
    :param location: Resource location.
    :type location: str
    :param tags: Resource tags.
    :type tags: dict[str, str]
    :param remote_virtual_network: Reference to the remote virtual network.
    :type remote_virtual_network:
     ~azure.mgmt.network.v2018_08_01.models.SubResource
    :param allow_hub_to_remote_vnet_transit: VirtualHub to RemoteVnet transit
     to enabled or not.
    :type allow_hub_to_remote_vnet_transit: bool
    :param allow_remote_vnet_to_use_hub_vnet_gateways: Allow RemoteVnet to use
     Virtual Hub's gateways.
    :type allow_remote_vnet_to_use_hub_vnet_gateways: bool
    :param provisioning_state: The provisioning state of the resource.
     Possible values include: 'Succeeded', 'Updating', 'Deleting', 'Failed'
    :type provisioning_state: str or
     ~azure.mgmt.network.v2018_08_01.models.ProvisioningState
    :ivar etag: Gets a unique read-only string that changes whenever the
     resource is updated.
    :vartype etag: str
    """

    _validation = {
        'name': {'readonly': True},
        'type': {'readonly': True},
        'etag': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'location': {'key': 'location', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'remote_virtual_network': {'key': 'properties.remoteVirtualNetwork', 'type': 'SubResource'},
        'allow_hub_to_remote_vnet_transit': {'key': 'properties.allowHubToRemoteVnetTransit', 'type': 'bool'},
        'allow_remote_vnet_to_use_hub_vnet_gateways': {'key': 'properties.allowRemoteVnetToUseHubVnetGateways', 'type': 'bool'},
        'provisioning_state': {'key': 'properties.provisioningState', 'type': 'str'},
        'etag': {'key': 'etag', 'type': 'str'},
    }

    def __init__(self, *, id: str=None, location: str=None, tags=None, remote_virtual_network=None, allow_hub_to_remote_vnet_transit: bool=None, allow_remote_vnet_to_use_hub_vnet_gateways: bool=None, provisioning_state=None, **kwargs) -> None:
        super(HubVirtualNetworkConnection, self).__init__(id=id, location=location, tags=tags, **kwargs)
        self.remote_virtual_network = remote_virtual_network
        self.allow_hub_to_remote_vnet_transit = allow_hub_to_remote_vnet_transit
        self.allow_remote_vnet_to_use_hub_vnet_gateways = allow_remote_vnet_to_use_hub_vnet_gateways
        self.provisioning_state = provisioning_state
        self.etag = None
