# Copyright 2020 Amazon.com, Inc. or its affiliates. All Rights Reserved.
#
# generated using file ./gen/model/linux/system/os/system.yaml
#
# DONOT EDIT - generated by diligent bots

from dent_os_testbed.lib.test_lib_object import TestLibObject


class LinuxSystem(TestLibObject):
    """
        system information
    """
    def format_reboot(self, command, *argv, **kwarg):
        raise NotImplementedError

    def parse_reboot(self, command, output, *argv, **kwarg):
        raise NotImplementedError

    def format_shutdown(self, command, *argv, **kwarg):
        raise NotImplementedError

    def parse_shutdown(self, command, output, *argv, **kwarg):
        raise NotImplementedError

    def format_command(self, command, *argv, **kwarg):
        if command in ['reboot']:
            return self.format_reboot(command, *argv, **kwarg)

        if command in ['shutdown']:
            return self.format_shutdown(command, *argv, **kwarg)

        raise NameError('Cannot find command '+command)

    def parse_output(self, command, output, *argv, **kwarg):
        if command in ['reboot']:
            return self.parse_reboot(command, output, *argv, **kwarg)

        if command in ['shutdown']:
            return self.parse_shutdown(command, output, *argv, **kwarg)

        raise NameError('Cannot find command '+command)
