# -*- coding: utf-8 -*-
# Copyright 2020 Red Hat
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

#############################################
#                WARNING                    #
#############################################
#
# This file is auto generated by the resource
#   module builder playbook.
#
# Do not edit this file manually.
#
# Changes to this file will be over written
#   by the resource module builder.
#
# Changes should be made in the model used to
#   generate this file or in the resource module
#   builder template.
#
#############################################

from __future__ import absolute_import, division, print_function

__metaclass__ = type

from ansible_collections.junipernetworks.junos.tests.unit.compat.mock import (
    patch,
)
from ansible_collections.junipernetworks.junos.plugins.modules import (
    junos_routing_instances,
)
from ansible_collections.junipernetworks.junos.tests.unit.modules.utils import (
    set_module_args,
)
from .junos_module import TestJunosModule, load_fixture


class TestJunosRouting_instancesModule(TestJunosModule):
    module = junos_routing_instances

    def setUp(self):
        super(TestJunosRouting_instancesModule, self).setUp()

        self.mock_lock_configuration = patch(
            "ansible_collections.junipernetworks.junos.plugins.module_utils.network.junos.junos.lock_configuration"
        )
        self.lock_configuration = self.mock_lock_configuration.start()

        self.mock_unlock_configuration = patch(
            "ansible_collections.junipernetworks.junos.plugins.module_utils.network.junos.junos.unlock_configuration"
        )
        self.unlock_configuration = self.mock_unlock_configuration.start()

        self.mock_load_config = patch(
            "ansible_collections.junipernetworks.junos.plugins.module_utils.network.junos.config.routing_instances.routing_instances.load_config"
        )
        self.load_config = self.mock_load_config.start()

        self.mock_commit_configuration = patch(
            "ansible_collections.junipernetworks.junos.plugins.module_utils.network.junos.config.routing_instances.routing_instances.commit_configuration"
        )
        self.mock_commit_configuration = self.mock_commit_configuration.start()

        self.mock_execute_show_command = patch(
            "ansible_collections.junipernetworks.junos.plugins.module_utils.network.junos.facts.routing_instances.routing_instances."
            "Routing_instancesFacts.get_device_data"
        )
        self.execute_show_command = self.mock_execute_show_command.start()

    def tearDown(self):
        super(TestJunosRouting_instancesModule, self).tearDown()
        self.mock_load_config.stop()
        self.mock_lock_configuration.stop()
        self.mock_unlock_configuration.stop()
        self.mock_commit_configuration.stop()
        self.mock_execute_show_command.stop()

    def load_fixtures(
        self, commands=None, format="text", changed=False, filename=None
    ):
        def load_from_file(*args, **kwargs):
            if filename:
                output = load_fixture(filename)
            else:
                output = load_fixture("junos_routing_instances_config.cfg")
            return output

        self.execute_show_command.side_effect = load_from_file

    def sort_routing_instances(self, entry_list):
        for entry in entry_list:
            if entry.get("instance"):
                entry["routing_instances"].sort(key=lambda i: i.get("name"))

    def test_junos_routing_instances_merged(self):
        set_module_args(
            dict(
                config=[
                    dict(
                        name="test",
                        type="vrf",
                        route_distinguisher="10.58.255.1:37",
                        vrf_imports=["test-policy"],
                        vrf_exports=["test-policy", "test-policy-1"],
                        interfaces=[
                            dict(name="sp-0/0/0.0"),
                            dict(name="gr-0/0/0.0"),
                        ],
                        connector_id_advertise=True,
                    )
                ],
                state="merged",
            )
        )
        commands = [
            '<nc:routing-instances xmlns:nc="urn:ietf:params:xml:ns:netconf:base:1.0">'
            "<nc:instance><nc:name>test</nc:name><nc:connector-id-advertise/>"
            "<nc:instance-type>vrf</nc:instance-type><nc:interface><nc:name>sp-0/0/0.0</nc:name>"
            "</nc:interface><nc:interface><nc:name>gr-0/0/0.0</nc:name>"
            "</nc:interface><nc:route-distinguisher><nc:rd-type>10.58.255.1:37</nc:rd-type>"
            "</nc:route-distinguisher><nc:vrf-import>test-policy</nc:vrf-import>"
            "<nc:vrf-export>test-policy</nc:vrf-export><nc:vrf-export>test-policy-1</nc:vrf-export>"
            "</nc:instance></nc:routing-instances>"
        ]
        result = self.execute_module(changed=True, commands=commands)
        self.assertEqual(sorted(result["commands"]), sorted(commands))

    def test_junos_routing_instances_merged_idempotent(self):
        set_module_args(
            dict(
                config=[
                    dict(
                        name="forwardinst",
                        type="forwarding",
                        description="Configured by Ansible Content Team",
                    )
                ],
                state="merged",
            )
        )
        result = self.execute_module(changed=True)
        self.assertEqual(result["before"], result["after"])

    def test_junos_routing_instances_replaced(self):
        """
        :return:
        """
        set_module_args(
            dict(
                config=[
                    dict(
                        name="test",
                        type="vrf",
                        route_distinguisher="10.58.255.1:37",
                        vrf_imports=["test-policy"],
                        vrf_exports=["test-policy", "test-policy-1"],
                        interfaces=[
                            dict(name="sp-0/0/0.0"),
                            dict(name="gr-0/0/0.0"),
                        ],
                        connector_id_advertise=True,
                    ),
                    dict(
                        name="forwardinst",
                        type="forwarding",
                        description="Replaced and Configured by Ansible Content Team",
                    ),
                ],
                state="replaced",
            )
        )

        commands = [
            '<nc:routing-instances xmlns:nc="urn:ietf:params:xml:ns:netconf:base:1.0">'
            '<nc:instance delete="delete"><nc:name>forwardinst</nc:name></nc:instance>'
            "<nc:instance><nc:name>test</nc:name><nc:connector-id-advertise/>"
            "<nc:instance-type>vrf</nc:instance-type><nc:interface><nc:name>sp-0/0/0.0</nc:name>"
            "</nc:interface><nc:interface><nc:name>gr-0/0/0.0</nc:name>"
            "</nc:interface><nc:route-distinguisher><nc:rd-type>10.58.255.1:37</nc:rd-type>"
            "</nc:route-distinguisher><nc:vrf-import>test-policy</nc:vrf-import>"
            "<nc:vrf-export>test-policy</nc:vrf-export><nc:vrf-export>test-policy-1</nc:vrf-export>"
            "</nc:instance><nc:instance><nc:name>forwardinst</nc:name>"
            "<nc:description>Replaced and Configured by Ansible Content Team</nc:description>"
            "<nc:instance-type>forwarding</nc:instance-type>"
            "</nc:instance></nc:routing-instances>"
        ]
        result = self.execute_module(changed=True, commands=commands)
        self.assertEqual(sorted(result["commands"]), sorted(commands))

    def test_junos_routing_instances_replaced_idempotent(self):
        set_module_args(
            dict(
                config=[
                    dict(
                        name="forwardinst",
                        type="forwarding",
                        description="Configured by Ansible Content Team",
                    )
                ],
                state="replaced",
            )
        )
        result = self.execute_module(changed=True)
        self.assertEqual(result["before"], result["after"])

    def test_junos_routing_instances_overridden(self):
        """
        :return:
        """
        set_module_args(
            dict(
                config=[
                    dict(
                        name="test1",
                        type="vrf",
                        route_distinguisher="10.58.255.1:37",
                        vrf_imports=["test-policy"],
                        vrf_exports=["test-policy", "test-policy-1"],
                        interfaces=[
                            dict(name="sp-0/0/0.0"),
                            dict(name="gr-0/0/0.0"),
                        ],
                        connector_id_advertise=True,
                    )
                ],
                state="overridden",
            )
        )

        commands = [
            '<nc:routing-instances xmlns:nc="urn:ietf:params:xml:ns:netconf:base:1.0">'
            '<nc:instance delete="delete"><nc:name>forwardinst</nc:name></nc:instance>'
            "<nc:instance><nc:name>test1</nc:name><nc:connector-id-advertise/>"
            "<nc:instance-type>vrf</nc:instance-type><nc:interface><nc:name>sp-0/0/0.0</nc:name>"
            "</nc:interface><nc:interface><nc:name>gr-0/0/0.0</nc:name></nc:interface>"
            "<nc:route-distinguisher><nc:rd-type>10.58.255.1:37</nc:rd-type></nc:route-distinguisher>"
            "<nc:vrf-import>test-policy</nc:vrf-import><nc:vrf-export>test-policy</nc:vrf-export>"
            "<nc:vrf-export>test-policy-1</nc:vrf-export></nc:instance></nc:routing-instances>"
        ]
        result = self.execute_module(changed=True, commands=commands)
        self.assertEqual(sorted(result["commands"]), sorted(commands))

    def test_junos_routing_instances_overridden_idempotent(self):
        set_module_args(
            dict(
                config=[
                    dict(
                        name="forwardinst",
                        type="forwarding",
                        description="Configured by Ansible Content Team",
                    )
                ],
                state="overridden",
            )
        )
        result = self.execute_module(changed=True)
        self.assertEqual(result["before"], result["after"])

    def test_junos_routing_instances_rendered(self):
        """
        :return:
        """
        set_module_args(
            dict(
                config=[
                    dict(
                        name="test",
                        type="vrf",
                        route_distinguisher="10.58.255.1:37",
                        vrf_imports=["test-policy"],
                        vrf_exports=["test-policy", "test-policy-1"],
                        interfaces=[
                            dict(name="sp-0/0/0.0"),
                            dict(name="gr-0/0/0.0"),
                        ],
                        connector_id_advertise=True,
                    )
                ],
                state="rendered",
            )
        )

        rendered = (
            '<nc:routing-instances xmlns:nc="urn:ietf:params:xml:ns:netconf:base:1.0">'
            "<nc:instance><nc:name>test</nc:name><nc:connector-id-advertise/>"
            "<nc:instance-type>vrf</nc:instance-type><nc:interface><nc:name>sp-0/0/0.0</nc:name>"
            "</nc:interface><nc:interface><nc:name>gr-0/0/0.0</nc:name>"
            "</nc:interface><nc:route-distinguisher><nc:rd-type>10.58.255.1:37</nc:rd-type>"
            "</nc:route-distinguisher><nc:vrf-import>test-policy</nc:vrf-import>"
            "<nc:vrf-export>test-policy</nc:vrf-export><nc:vrf-export>test-policy-1</nc:vrf-export>"
            "</nc:instance></nc:routing-instances>"
        )
        result = self.execute_module(changed=False)
        self.assertEqual(sorted(result["rendered"]), sorted(rendered))

    def test_junos_routing_instances_gathered(self):
        """
        :return:
        """
        set_module_args(dict(state="gathered"))
        result = self.execute_module(changed=False)
        gather_list = [
            {
                "name": "forwardinst",
                "type": "forwarding",
                "description": "Configured by Ansible Content Team",
            }
        ]
        self.assertEqual(sorted(gather_list), sorted(result["gathered"]))

    def test_junos_routing_instances_deleted(self):
        """
        :return:
        """
        set_module_args(dict(config=[], state="deleted"))

        commands = [
            '<nc:routing-instances xmlns:nc="urn:ietf:params:xml:ns:netconf:base:1.0">'
            '<nc:instance delete="delete"/></nc:routing-instances>'
        ]
        result = self.execute_module(changed=True)
        self.assertEqual(sorted(result["commands"]), sorted(commands))

    def test_junos_routing_instances_delted_single_entry(self):
        """
        :return:
        """
        set_module_args(
            dict(config=[dict(name="forwardinst")], state="deleted")
        )

        commands = [
            '<nc:routing-instances xmlns:nc="urn:ietf:params:xml:ns:netconf:base:1.0">'
            '<nc:instance delete="delete"><nc:name>forwardinst</nc:name></nc:instance></nc:routing-instances>'
        ]
        result = self.execute_module(changed=True)
        self.assertEqual(sorted(result["commands"]), sorted(commands))

    def test_junos_routing_instances_parsed(self):
        parsed_str = """
            <rpc-reply message-id="urn:uuid:0cadb4e8-5bba-47f4-986e-72906227007f">
                <configuration changed-seconds="1590139550" changed-localtime="2020-05-22 09:25:50 UTC">
                    <version>18.4R1-S2.4</version>
                     <routing-instances>
                        <instance>
                            <name>forwardinst</name>
                            <description>Configured by Ansible Content Team</description>
                            <instance-type>forwarding</instance-type>
                        </instance>
                        <instance>
                            <name>test</name>
                            <instance-type>vrf</instance-type>
                            <interface>
                                <name>gr-0/0/0.0</name>
                            </interface>
                            <interface>
                                <name>sp-0/0/0.0</name>
                            </interface>
                            <route-distinguisher>
                                <rd-type>10.58.255.1:37</rd-type>
                            </route-distinguisher>
                            <vrf-import>test-policy</vrf-import>
                            <vrf-export>test-policy</vrf-export>
                            <vrf-export>test-policy-1</vrf-export>
                            <no-local-switching/>
                            <no-vrf-advertise/>
                            <no-vrf-propagate-ttl/>
                            <qualified-bum-pruning-mode/>
                            <no-irb-layer2-copy/>
                            <connector-id-advertise/>
                        </instance>
                    </routing-instances>
                </configuration>
            </rpc-reply>
        """
        set_module_args(dict(running_config=parsed_str, state="parsed"))
        result = self.execute_module(changed=False)
        parsed_list = [
            {
                "description": "Configured by Ansible Content Team",
                "name": "forwardinst",
                "type": "forwarding",
            },
            {
                "connector_id_advertise": True,
                "interfaces": [{"name": "gr-0/0/0.0"}, {"name": "sp-0/0/0.0"}],
                "name": "test",
                "no_irb_layer_2_copy": True,
                "no_local_switching": True,
                "no_vrf_advertise": True,
                "no_vrf_propagate_ttl": True,
                "route_distinguisher": "10.58.255.1:37",
                "type": "vrf",
                "vrf_exports": ["test-policy", "test-policy-1"],
                "vrf_imports": ["test-policy"],
            },
        ]
        self.sort_routing_instances(result["parsed"])
        self.sort_routing_instances(parsed_list)
        self.assertEqual(result["parsed"], parsed_list)
