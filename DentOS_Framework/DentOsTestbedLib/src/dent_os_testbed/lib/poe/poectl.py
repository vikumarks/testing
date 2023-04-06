# Copyright 2020 Amazon.com, Inc. or its affiliates. All Rights Reserved.
#
# generated using file ./gen/model/dent/platform/poe/peoctl.yaml
#
# DONOT EDIT - generated by diligent bots

import pytest
from dent_os_testbed.lib.test_lib_object import TestLibObject
from dent_os_testbed.lib.poe.linux.linux_poectl_impl import LinuxPoectlImpl
class Poectl(TestLibObject):
    """
        -h, --help                           Show this help message and exit
        -i, --port-info PORT_LIST            Return detailed information for the specified ports.
          eg: -i swp1-swp5,swp10
        -p, --priority PORT_LIST PRIORITY    Set priority for the specified ports:
          low, high, critical
        -d, --disable-ports PORT_LIST        Disable POE operation on the specified ports.
        -e, --enable-ports PORT_LIST         Enable POE operation on the specified ports.
        -r, --reset-ports PORT_LIST          Perform hardware reset on the specified ports.
        -u, --upgrade FILE_PATH              Upgrade firmware on controller
        -s, --system                         Return POE status for the entire switch
        -a, --all                            Return POE status for system and detailed information for ports.
        -j, --json                           Return output in json format
        -v, --version                        Display version info
        --save                               Save the current configuration. The saved configuration
                                             is automatically loaded on system boot.
        --load                               Load and apply the saved configuration.

    """
    async def _run_command(api, *argv, **kwarg):
        devices = kwarg['input_data']
        result = list()
        for device in devices:
            for device_name in device:
                device_result = {
                    device_name : dict()
                }
                # device lookup
                if 'device_obj' in kwarg:
                    device_obj = kwarg.get('device_obj', None)[device_name]
                else:
                    if device_name not in pytest.testbed.devices_dict:
                        device_result[device_name] =  "No matching device "+ device_name
                        result.append(device_result)
                        return result
                    device_obj = pytest.testbed.devices_dict[device_name]
                commands = ""
                if device_obj.os in ['dentos', 'cumulus']:
                    impl_obj = LinuxPoectlImpl()
                    for command in device[device_name]:
                        commands += impl_obj.format_command(command=api, params=command)
                        commands += '&& '
                    commands = commands[:-3]

                else:
                    device_result[device_name]['rc'] = -1
                    device_result[device_name]['result'] = "No matching device OS "+ device_obj.os
                    result.append(device_result)
                    return result
                device_result[device_name]['command'] = commands
                try:
                    rc, output = await device_obj.run_cmd(("sudo " if device_obj.ssh_conn_params.pssh else "") + commands)
                    device_result[device_name]['rc'] = rc
                    device_result[device_name]['result'] = output
                    if 'parse_output' in kwarg:
                        parse_output = impl_obj.parse_output(command=api, output=output, commands=commands)
                        device_result[device_name]['parsed_output'] = parse_output
                except Exception as e:
                    device_result[device_name]['rc'] = -1
                    device_result[device_name]['result'] = str(e)
                result.append(device_result)
        return result

    async def show(*argv, **kwarg):
        """
        Platforms: ['dentos', 'cumulus']
        Usage:
        Poectl.show(
            input_data = [{
                # device 1
                'dev1' : [{
                    # command 1
                        'port':'string',
                }],
            }],
        )
        Description:
        -i, --port-info PORT_LIST            Return detailed information for the specified ports.
          eg: -i swp1-swp5,swp10

        """
        return await Poectl._run_command("show", *argv, **kwarg)

    async def enable(*argv, **kwarg):
        """
        Platforms: ['dentos', 'cumulus']
        Usage:
        Poectl.enable(
            input_data = [{
                # device 1
                'dev1' : [{
                    # command 1
                        'port':'string',
                }],
            }],
        )
        Description:
        -d, --disable-ports PORT_LIST        Disable POE operation on the specified ports.
        -e, --enable-ports PORT_LIST         Enable POE operation on the specified ports.

        """
        return await Poectl._run_command("enable", *argv, **kwarg)

    async def disable(*argv, **kwarg):
        """
        Platforms: ['dentos', 'cumulus']
        Usage:
        Poectl.disable(
            input_data = [{
                # device 1
                'dev1' : [{
                    # command 1
                        'port':'string',
                }],
            }],
        )
        Description:
        -d, --disable-ports PORT_LIST        Disable POE operation on the specified ports.
        -e, --enable-ports PORT_LIST         Enable POE operation on the specified ports.

        """
        return await Poectl._run_command("disable", *argv, **kwarg)

    async def save(*argv, **kwarg):
        """
        Platforms: ['dentos', 'cumulus']
        Usage:
        Poectl.save(
            input_data = [{
                # device 1
                'dev1' : [{
                    # command 1
                        'port':'string',
                }],
            }],
        )
        Description:
        --save                               Save the current configuration. The saved configuration
                                             is automatically loaded on system boot.
        --load                               Load and apply the saved configuration.

        """
        return await Poectl._run_command("save", *argv, **kwarg)

    async def restore(*argv, **kwarg):
        """
        Platforms: ['dentos', 'cumulus']
        Usage:
        Poectl.restore(
            input_data = [{
                # device 1
                'dev1' : [{
                    # command 1
                        'port':'string',
                }],
            }],
        )
        Description:
        --save                               Save the current configuration. The saved configuration
                                             is automatically loaded on system boot.
        --load                               Load and apply the saved configuration.

        """
        return await Poectl._run_command("restore", *argv, **kwarg)

