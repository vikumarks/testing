# Copyright 2020 Amazon.com, Inc. or its affiliates. All Rights Reserved.
#
# generated using file ./gen/model/linux/network/bridge/bridge.yaml
#
# DONOT EDIT - generated by diligent bots

from dent_os_testbed.lib.test_lib_object import TestLibObject


class LinuxBridgeVlan(TestLibObject):
    """
        The corresponding commands display vlan filter entries, add new entries, and delete old ones.

    """

    def format_update(self, command, *argv, **kwarg):
        raise NotImplementedError

    def parse_update(self, command, output, *argv, **kwarg):
        raise NotImplementedError

    def format_show(self, command, *argv, **kwarg):
        raise NotImplementedError

    def parse_show(self, command, output, *argv, **kwarg):
        raise NotImplementedError

    def format_command(self, command, *argv, **kwarg):
        if command in ['add', 'delete']:
            return self.format_update(command, *argv, **kwarg)

        if command in ['show', 'tunnelshow']:
            return self.format_show(command, *argv, **kwarg)

        raise NameError('Cannot find command '+command)

    def parse_output(self, command, output, *argv, **kwarg):
        if command in ['add', 'delete']:
            return self.parse_update(command, output, *argv, **kwarg)

        if command in ['show', 'tunnelshow']:
            return self.parse_show(command, output, *argv, **kwarg)

        raise NameError('Cannot find command '+command)
