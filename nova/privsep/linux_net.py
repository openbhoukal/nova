# Copyright 2016 Red Hat, Inc
# Copyright 2017 Rackspace Australia
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

"""
Linux network specific helpers.
"""

from oslo_concurrency import processutils

import nova.privsep


@nova.privsep.sys_admin_pctxt.entrypoint
def delete_bridge(interface):
    """Delete a bridge.

    :param interface: the name of the bridge
    """
    processutils.execute('brctl', 'delbr', interface)
