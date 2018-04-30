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

from msrest.serialization import Model


class CreateJobProperties(Model):
    """The common Data Lake Analytics job properties for job submission.

    You probably want to use the sub-classes and not this class directly. Known
    sub-classes are: CreateUSqlJobProperties, CreateScopeJobProperties

    All required parameters must be populated in order to send to Azure.

    :param runtime_version: The runtime version of the Data Lake Analytics
     engine to use for the specific type of job being run.
    :type runtime_version: str
    :param script: Required. The script to run. Please note that the maximum
     script size is 3 MB.
    :type script: str
    :param type: Required. Constant filled by server.
    :type type: str
    """

    _validation = {
        'script': {'required': True},
        'type': {'required': True},
    }

    _attribute_map = {
        'runtime_version': {'key': 'runtimeVersion', 'type': 'str'},
        'script': {'key': 'script', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
    }

    _subtype_map = {
        'type': {'USql': 'CreateUSqlJobProperties', 'Scope': 'CreateScopeJobProperties'}
    }

    def __init__(self, *, script: str, runtime_version: str=None, **kwargs) -> None:
        super(CreateJobProperties, self).__init__(**kwargs)
        self.runtime_version = runtime_version
        self.script = script
        self.type = None