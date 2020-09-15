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
# pylint: skip-file
# flake8: noqa
from msrest.serialization import Model


class SecurityDomainOperationStatus(Model):

    _attribute_map = {
        'status': {'key': 'status', 'type': 'OperationStatus'},
        'status_details': {'key': 'status_details', 'type': 'str'}
    }

    def __init__(self, *, status=None, status_details=None, **kwargs) -> None:
        super(SecurityDomainOperationStatus, self).__init__(**kwargs)
        self.status = status
        self.status_details = status_details
