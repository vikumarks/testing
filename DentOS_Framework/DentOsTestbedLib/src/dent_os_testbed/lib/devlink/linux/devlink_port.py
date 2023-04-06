# Copyright 2020 Amazon.com, Inc. or its affiliates. All Rights Reserved.
#
# generated using file ./gen/model/linux/network/devlink/devlink.yaml
#
# DONOT EDIT - generated by diligent bots

from dent_os_testbed.lib.test_lib_object import TestLibObject
class DevlinkPort(TestLibObject):
    """
        devlink [ OPTIONS ] {dev|port|monitor|sb|resource|region|health|trap } {COMMAND | help }
        devlink [ -force ] -batch filename

    """
    def format_set(self, command, *argv, **kwarg):
        raise NotImplementedError

    def parse_set(self, command, output, *argv, **kwarg):
        raise NotImplementedError

    def format_show(self, command, *argv, **kwarg):
        raise NotImplementedError

    def parse_show(self, command, output, *argv, **kwarg):
        raise NotImplementedError

    def format_command(self, command, *argv, **kwarg):
        if command in ['set']:
            return self.format_set(command, *argv, **kwarg)

        if command in ['show']:
            return self.format_show(command, *argv, **kwarg)


        raise NameError("Cannot find command "+command)

    def parse_output(self, command, output, *argv, **kwarg):
        if command in ['set']:
            return self.parse_set(command, output, *argv, **kwarg)

        if command in ['show']:
            return self.parse_show(command, output, *argv, **kwarg)


        raise NameError("Cannot find command "+command)

