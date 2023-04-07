# Copyright 2020 Amazon.com, Inc. or its affiliates. All Rights Reserved.
#
# generated using file ./gen/model/dent/platform/onlp/onlpdump.yaml
#
# DONOT EDIT - generated by diligent bots

from dent_os_testbed.discovery.Module import Module
from dent_os_testbed.lib.onlp.onlp_system_info import OnlpSystemInfo


class OnlpSystemInfoMod(Module):
    """
    """
    def set_onlp_system_info(self, src, dst):

        for i,onlp_system_info in enumerate([src]):
            if 'product_name' in onlp_system_info: dst.product_name = onlp_system_info.get('product_name')
            if 'serial_number' in onlp_system_info: dst.serial_number = onlp_system_info.get('serial_number')
            if 'mac' in onlp_system_info: dst.mac = onlp_system_info.get('mac')
            if 'mac_range' in onlp_system_info: dst.mac_range = onlp_system_info.get('mac_range')
            if 'manufacturer' in onlp_system_info: dst.manufacturer = onlp_system_info.get('manufacturer')
            if 'manufacturer_date' in onlp_system_info: dst.manufacturer_date = onlp_system_info.get('manufacturer_date')
            if 'vendor' in onlp_system_info: dst.vendor = onlp_system_info.get('vendor')
            if 'platform_name' in onlp_system_info: dst.platform_name = onlp_system_info.get('platform_name')
            if 'device_version' in onlp_system_info: dst.device_version = onlp_system_info.get('device_version')
            if 'label_revision' in onlp_system_info: dst.label_revision = onlp_system_info.get('label_revision')
            if 'country_code' in onlp_system_info: dst.country_code = onlp_system_info.get('country_code')
            if 'diag_version' in onlp_system_info: dst.diag_version = onlp_system_info.get('diag_version')
            if 'service_tag' in onlp_system_info: dst.service_tag = onlp_system_info.get('service_tag')
            if 'onie_version' in onlp_system_info: dst.onie_version = onlp_system_info.get('onie_version')

    async def discover(self):
        # need to get device instance to get the data from
        #
        for i, dut in enumerate(self.report.duts):
            if not dut.device_id: continue
            dev = self.ctx.devices_dict[dut.device_id]
            if dev.os == 'ixnetwork' or not await dev.is_connected():
                print('Device not connected skipping onlp_system_info discovery')
                continue
            print('Running onlp_system_info Discovery on ' + dev.host_name)
            out = await OnlpSystemInfo.show(
                input_data=[{dev.host_name: [{'dut_discovery':True}]}],
                device_obj={dev.host_name: dev},
                parse_output=True
            )
            if out[0][dev.host_name]['rc'] != 0:
                print(out)
                print('Failed to get onlp_system_info')
                continue
            if 'parsed_output' not in out[0][dev.host_name]:
                print('Failed to get parsed_output onlp_system_info')
                print (out)
                continue
            self.set_onlp_system_info(out[0][dev.host_name]['parsed_output'], self.report.duts[i].platform.onlp.system_information)
            print('Finished onlp_system_info Discovery on {} with {} entries'.format(dev.host_name, len(self.report.duts[i].platform.onlp.system_information)))
