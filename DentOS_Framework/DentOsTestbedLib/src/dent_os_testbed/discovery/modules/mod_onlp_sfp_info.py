# Copyright 2020 Amazon.com, Inc. or its affiliates. All Rights Reserved.
#
# generated using file ./gen/model/dent/platform/onlp/onlpdump.yaml
#
# DONOT EDIT - generated by diligent bots

from dent_os_testbed.discovery.Module import Module
from dent_os_testbed.lib.onlp.onlp_sfp_info import OnlpSfpInfo


class OnlpSfpInfoMod(Module):
    """
    """

    def set_onlp_sfp_info(self, src, dst):

        for i,onlp_sfp_info in enumerate(src):
            if 'port' in onlp_sfp_info: dst[i].port = onlp_sfp_info.get('port')
            if 'type' in onlp_sfp_info: dst[i].type = onlp_sfp_info.get('type')
            if 'media' in onlp_sfp_info: dst[i].media = onlp_sfp_info.get('media')
            if 'status' in onlp_sfp_info: dst[i].status = onlp_sfp_info.get('status')
            if 'len' in onlp_sfp_info: dst[i].len = onlp_sfp_info.get('len')
            if 'vendor' in onlp_sfp_info: dst[i].vendor = onlp_sfp_info.get('vendor')
            if 'model' in onlp_sfp_info: dst[i].model = onlp_sfp_info.get('model')
            if 'serial_number' in onlp_sfp_info: dst[i].serial_number = onlp_sfp_info.get('serial_number')

    async def discover(self):
        # need to get device instance to get the data from
        #
        for i, dut in enumerate(self.report.duts):
            if not dut.device_id: continue
            dev = self.ctx.devices_dict[dut.device_id]
            if dev.os == 'ixnetwork' or not await dev.is_connected():
                print('Device not connected skipping onlp_sfp_info discovery')
                continue
            print('Running onlp_sfp_info Discovery on ' + dev.host_name)
            out = await OnlpSfpInfo.show(
                input_data=[{dev.host_name: [{'dut_discovery':True}]}],
                device_obj={dev.host_name: dev},
                parse_output=True
            )
            if out[0][dev.host_name]['rc'] != 0:
                print(out)
                print('Failed to get onlp_sfp_info')
                continue
            if 'parsed_output' not in out[0][dev.host_name]:
                print('Failed to get parsed_output onlp_sfp_info')
                print (out)
                continue
            self.set_onlp_sfp_info(out[0][dev.host_name]['parsed_output'], self.report.duts[i].platform.onlp.sfps)
            print('Finished onlp_sfp_info Discovery on {} with {} entries'.format(dev.host_name, len(self.report.duts[i].platform.onlp.sfps)))
