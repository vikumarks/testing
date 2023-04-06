# Copyright 2020 Amazon.com, Inc. or its affiliates. All Rights Reserved.
#
# generated using file ./gen/model/dent/network/ip/route.yaml
#
# DONOT EDIT - generated by diligent bots

import pytest
from dent_os_testbed.lib.test_lib_object import TestLibObject
from dent_os_testbed.lib.ip.linux.linux_ip_route_impl import LinuxIpRouteImpl
class IpRoute(TestLibObject):
    """
        - ip [ ip-OPTIONS ] route { COMMAND | help }
        - ip route { show | flush } SELECTOR
        - ip route save SELECTOR
        - ip route restore
        - ip route get ROUTE_GET_FLAGS ADDRESS [ from ADDRESS iif STRING ] [ oif STRING ] [ mark MARK ]
          [ tos TOS ] [ vrf NAME ] [ ipproto PROTOCOL ] [ sport NUMBER ] [ dport NUMBER ]
        - ip route { add | del | change | append | replace } ROUTE

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
                    impl_obj = LinuxIpRouteImpl()
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

    async def add(*argv, **kwarg):
        """
        Platforms: ['dentos', 'cumulus']
        Usage:
        IpRoute.add(
            input_data = [{
                # device 1
                'dev1' : [{
                    # command 1
                        'dst':'ip_addr_t',
                        'tos':'int',
                        'table':'int',
                        'protocol':'string',
                        'scope':'string',
                        'metric':'int',
                        'nexthop':'undefined',
                        'via':'ip_addr_t',
                        'dev':'string',
                        'weight':'int',
                        'nhflags':'int',
                        'mtu':'int',
                        'advmss':'int',
                        'rtt':'int',
                        'rttvar':'int',
                        'reordering':'int',
                        'window':'int',
                        'cwnd':'int',
                        'ssthresh':'int',
                        'realms':'int',
                        'rto_min':'time_t',
                        'initcwnd':'int',
                        'initrwnd':'int',
                        'qickack':'undefined',
                        'congctl':'undefined',
                        'features':'undefined',
                        'src':'ip_addr_t',
                        'hoplimit':'undefined',
                        'pref':'undefined',
                        'expires':'undefined',
                        'options':'string',
                }],
            }],
        )
        Description:
        Add/Delete/Change/Append/Replace route using the below command
        - ip route { add | del | change | append | replace } ROUTE
        ROUTE := NODE_SPEC [ INFO_SPEC ]
        NODE_SPEC := [ TYPE ] PREFIX [ tos TOS ] [ table TABLE_ID ] [ proto RTPROTO ] [ scope SCOPE ]
          [ metric METRIC ] [ ttl-propagate { enabled | disabled } ]
        INFO_SPEC := NH OPTIONS FLAGS [ nexthop NH ] ...
        NH := [ encap ENCAP ] [ via [ FAMILY ] ADDRESS ] [ dev STRING ] [ weight NUMBER ] NHFLAGS
        FAMILY := [ inet | inet6 | ipx | dnet | mpls | bridge | link ]
        OPTIONS := FLAGS [ mtu NUMBER ] [ advmss NUMBER ] [ as [ to ] ADDRESS ] rtt TIME ] [ rttvar TIME ]
          [ reordering NUMBER ] [ window NUMBER ] [ cwnd NUMBER ] [ ssthresh NUMBER ] [ realms REALM ]
          [ rto_min TIME ] [ initcwnd NUMBER ] [ initrwnd NUMBER ] [ features FEATURES ] [ quickack BOOL ]
          [ congctl NAME ] [ pref PREF ] [ expires TIME ] [ fastopen_no_cookie BOOL ]
        TYPE := [ unicast | local | broadcast | multicast | throw | unreachable | prohibit | blackhole | nat ]
        TABLE_ID := [ local| main | default | all | NUMBER ]
        SCOPE := [ host | link | global | NUMBER ]
        NHFLAGS := [ onlink | pervasive ]
        RTPROTO := [ kernel | boot | static | NUMBER ]
        FEATURES := [ ecn | ]
        PREF := [ low | medium | high ]
        ENCAP := [ ENCAP_MPLS | ENCAP_IP | ENCAP_BPF | ENCAP_SEG6 | ENCAP_SEG6LOCAL ]
        ENCAP_MPLS := mpls [ LABEL ] [ ttl TTL ]
        ENCAP_IP := ip id TUNNEL_ID dst REMOTE_IP [ tos TOS ] [ ttl TTL ]
        ENCAP_BPF := bpf [ in PROG ] [ out PROG ] [ xmit PROG ] [ headroom SIZE ]
        ENCAP_SEG6 := seg6 mode [ encap | inline | l2encap ] segs SEGMENTS [ hmac KEYID ]
        ENCAP_SEG6LOCAL := seg6local action SEG6_ACTION [ SEG6_ACTION_PARAM ]

        """
        return await IpRoute._run_command("add", *argv, **kwarg)

    async def delete(*argv, **kwarg):
        """
        Platforms: ['dentos', 'cumulus']
        Usage:
        IpRoute.delete(
            input_data = [{
                # device 1
                'dev1' : [{
                    # command 1
                        'dst':'ip_addr_t',
                        'tos':'int',
                        'table':'int',
                        'protocol':'string',
                        'scope':'string',
                        'metric':'int',
                        'nexthop':'undefined',
                        'via':'ip_addr_t',
                        'dev':'string',
                        'weight':'int',
                        'nhflags':'int',
                        'mtu':'int',
                        'advmss':'int',
                        'rtt':'int',
                        'rttvar':'int',
                        'reordering':'int',
                        'window':'int',
                        'cwnd':'int',
                        'ssthresh':'int',
                        'realms':'int',
                        'rto_min':'time_t',
                        'initcwnd':'int',
                        'initrwnd':'int',
                        'qickack':'undefined',
                        'congctl':'undefined',
                        'features':'undefined',
                        'src':'ip_addr_t',
                        'hoplimit':'undefined',
                        'pref':'undefined',
                        'expires':'undefined',
                        'options':'string',
                }],
            }],
        )
        Description:
        Add/Delete/Change/Append/Replace route using the below command
        - ip route { add | del | change | append | replace } ROUTE
        ROUTE := NODE_SPEC [ INFO_SPEC ]
        NODE_SPEC := [ TYPE ] PREFIX [ tos TOS ] [ table TABLE_ID ] [ proto RTPROTO ] [ scope SCOPE ]
          [ metric METRIC ] [ ttl-propagate { enabled | disabled } ]
        INFO_SPEC := NH OPTIONS FLAGS [ nexthop NH ] ...
        NH := [ encap ENCAP ] [ via [ FAMILY ] ADDRESS ] [ dev STRING ] [ weight NUMBER ] NHFLAGS
        FAMILY := [ inet | inet6 | ipx | dnet | mpls | bridge | link ]
        OPTIONS := FLAGS [ mtu NUMBER ] [ advmss NUMBER ] [ as [ to ] ADDRESS ] rtt TIME ] [ rttvar TIME ]
          [ reordering NUMBER ] [ window NUMBER ] [ cwnd NUMBER ] [ ssthresh NUMBER ] [ realms REALM ]
          [ rto_min TIME ] [ initcwnd NUMBER ] [ initrwnd NUMBER ] [ features FEATURES ] [ quickack BOOL ]
          [ congctl NAME ] [ pref PREF ] [ expires TIME ] [ fastopen_no_cookie BOOL ]
        TYPE := [ unicast | local | broadcast | multicast | throw | unreachable | prohibit | blackhole | nat ]
        TABLE_ID := [ local| main | default | all | NUMBER ]
        SCOPE := [ host | link | global | NUMBER ]
        NHFLAGS := [ onlink | pervasive ]
        RTPROTO := [ kernel | boot | static | NUMBER ]
        FEATURES := [ ecn | ]
        PREF := [ low | medium | high ]
        ENCAP := [ ENCAP_MPLS | ENCAP_IP | ENCAP_BPF | ENCAP_SEG6 | ENCAP_SEG6LOCAL ]
        ENCAP_MPLS := mpls [ LABEL ] [ ttl TTL ]
        ENCAP_IP := ip id TUNNEL_ID dst REMOTE_IP [ tos TOS ] [ ttl TTL ]
        ENCAP_BPF := bpf [ in PROG ] [ out PROG ] [ xmit PROG ] [ headroom SIZE ]
        ENCAP_SEG6 := seg6 mode [ encap | inline | l2encap ] segs SEGMENTS [ hmac KEYID ]
        ENCAP_SEG6LOCAL := seg6local action SEG6_ACTION [ SEG6_ACTION_PARAM ]

        """
        return await IpRoute._run_command("delete", *argv, **kwarg)

    async def change(*argv, **kwarg):
        """
        Platforms: ['dentos', 'cumulus']
        Usage:
        IpRoute.change(
            input_data = [{
                # device 1
                'dev1' : [{
                    # command 1
                        'dst':'ip_addr_t',
                        'tos':'int',
                        'table':'int',
                        'protocol':'string',
                        'scope':'string',
                        'metric':'int',
                        'nexthop':'undefined',
                        'via':'ip_addr_t',
                        'dev':'string',
                        'weight':'int',
                        'nhflags':'int',
                        'mtu':'int',
                        'advmss':'int',
                        'rtt':'int',
                        'rttvar':'int',
                        'reordering':'int',
                        'window':'int',
                        'cwnd':'int',
                        'ssthresh':'int',
                        'realms':'int',
                        'rto_min':'time_t',
                        'initcwnd':'int',
                        'initrwnd':'int',
                        'qickack':'undefined',
                        'congctl':'undefined',
                        'features':'undefined',
                        'src':'ip_addr_t',
                        'hoplimit':'undefined',
                        'pref':'undefined',
                        'expires':'undefined',
                        'options':'string',
                }],
            }],
        )
        Description:
        Add/Delete/Change/Append/Replace route using the below command
        - ip route { add | del | change | append | replace } ROUTE
        ROUTE := NODE_SPEC [ INFO_SPEC ]
        NODE_SPEC := [ TYPE ] PREFIX [ tos TOS ] [ table TABLE_ID ] [ proto RTPROTO ] [ scope SCOPE ]
          [ metric METRIC ] [ ttl-propagate { enabled | disabled } ]
        INFO_SPEC := NH OPTIONS FLAGS [ nexthop NH ] ...
        NH := [ encap ENCAP ] [ via [ FAMILY ] ADDRESS ] [ dev STRING ] [ weight NUMBER ] NHFLAGS
        FAMILY := [ inet | inet6 | ipx | dnet | mpls | bridge | link ]
        OPTIONS := FLAGS [ mtu NUMBER ] [ advmss NUMBER ] [ as [ to ] ADDRESS ] rtt TIME ] [ rttvar TIME ]
          [ reordering NUMBER ] [ window NUMBER ] [ cwnd NUMBER ] [ ssthresh NUMBER ] [ realms REALM ]
          [ rto_min TIME ] [ initcwnd NUMBER ] [ initrwnd NUMBER ] [ features FEATURES ] [ quickack BOOL ]
          [ congctl NAME ] [ pref PREF ] [ expires TIME ] [ fastopen_no_cookie BOOL ]
        TYPE := [ unicast | local | broadcast | multicast | throw | unreachable | prohibit | blackhole | nat ]
        TABLE_ID := [ local| main | default | all | NUMBER ]
        SCOPE := [ host | link | global | NUMBER ]
        NHFLAGS := [ onlink | pervasive ]
        RTPROTO := [ kernel | boot | static | NUMBER ]
        FEATURES := [ ecn | ]
        PREF := [ low | medium | high ]
        ENCAP := [ ENCAP_MPLS | ENCAP_IP | ENCAP_BPF | ENCAP_SEG6 | ENCAP_SEG6LOCAL ]
        ENCAP_MPLS := mpls [ LABEL ] [ ttl TTL ]
        ENCAP_IP := ip id TUNNEL_ID dst REMOTE_IP [ tos TOS ] [ ttl TTL ]
        ENCAP_BPF := bpf [ in PROG ] [ out PROG ] [ xmit PROG ] [ headroom SIZE ]
        ENCAP_SEG6 := seg6 mode [ encap | inline | l2encap ] segs SEGMENTS [ hmac KEYID ]
        ENCAP_SEG6LOCAL := seg6local action SEG6_ACTION [ SEG6_ACTION_PARAM ]

        """
        return await IpRoute._run_command("change", *argv, **kwarg)

    async def append(*argv, **kwarg):
        """
        Platforms: ['dentos', 'cumulus']
        Usage:
        IpRoute.append(
            input_data = [{
                # device 1
                'dev1' : [{
                    # command 1
                        'dst':'ip_addr_t',
                        'tos':'int',
                        'table':'int',
                        'protocol':'string',
                        'scope':'string',
                        'metric':'int',
                        'nexthop':'undefined',
                        'via':'ip_addr_t',
                        'dev':'string',
                        'weight':'int',
                        'nhflags':'int',
                        'mtu':'int',
                        'advmss':'int',
                        'rtt':'int',
                        'rttvar':'int',
                        'reordering':'int',
                        'window':'int',
                        'cwnd':'int',
                        'ssthresh':'int',
                        'realms':'int',
                        'rto_min':'time_t',
                        'initcwnd':'int',
                        'initrwnd':'int',
                        'qickack':'undefined',
                        'congctl':'undefined',
                        'features':'undefined',
                        'src':'ip_addr_t',
                        'hoplimit':'undefined',
                        'pref':'undefined',
                        'expires':'undefined',
                        'options':'string',
                }],
            }],
        )
        Description:
        Add/Delete/Change/Append/Replace route using the below command
        - ip route { add | del | change | append | replace } ROUTE
        ROUTE := NODE_SPEC [ INFO_SPEC ]
        NODE_SPEC := [ TYPE ] PREFIX [ tos TOS ] [ table TABLE_ID ] [ proto RTPROTO ] [ scope SCOPE ]
          [ metric METRIC ] [ ttl-propagate { enabled | disabled } ]
        INFO_SPEC := NH OPTIONS FLAGS [ nexthop NH ] ...
        NH := [ encap ENCAP ] [ via [ FAMILY ] ADDRESS ] [ dev STRING ] [ weight NUMBER ] NHFLAGS
        FAMILY := [ inet | inet6 | ipx | dnet | mpls | bridge | link ]
        OPTIONS := FLAGS [ mtu NUMBER ] [ advmss NUMBER ] [ as [ to ] ADDRESS ] rtt TIME ] [ rttvar TIME ]
          [ reordering NUMBER ] [ window NUMBER ] [ cwnd NUMBER ] [ ssthresh NUMBER ] [ realms REALM ]
          [ rto_min TIME ] [ initcwnd NUMBER ] [ initrwnd NUMBER ] [ features FEATURES ] [ quickack BOOL ]
          [ congctl NAME ] [ pref PREF ] [ expires TIME ] [ fastopen_no_cookie BOOL ]
        TYPE := [ unicast | local | broadcast | multicast | throw | unreachable | prohibit | blackhole | nat ]
        TABLE_ID := [ local| main | default | all | NUMBER ]
        SCOPE := [ host | link | global | NUMBER ]
        NHFLAGS := [ onlink | pervasive ]
        RTPROTO := [ kernel | boot | static | NUMBER ]
        FEATURES := [ ecn | ]
        PREF := [ low | medium | high ]
        ENCAP := [ ENCAP_MPLS | ENCAP_IP | ENCAP_BPF | ENCAP_SEG6 | ENCAP_SEG6LOCAL ]
        ENCAP_MPLS := mpls [ LABEL ] [ ttl TTL ]
        ENCAP_IP := ip id TUNNEL_ID dst REMOTE_IP [ tos TOS ] [ ttl TTL ]
        ENCAP_BPF := bpf [ in PROG ] [ out PROG ] [ xmit PROG ] [ headroom SIZE ]
        ENCAP_SEG6 := seg6 mode [ encap | inline | l2encap ] segs SEGMENTS [ hmac KEYID ]
        ENCAP_SEG6LOCAL := seg6local action SEG6_ACTION [ SEG6_ACTION_PARAM ]

        """
        return await IpRoute._run_command("append", *argv, **kwarg)

    async def replace(*argv, **kwarg):
        """
        Platforms: ['dentos', 'cumulus']
        Usage:
        IpRoute.replace(
            input_data = [{
                # device 1
                'dev1' : [{
                    # command 1
                        'dst':'ip_addr_t',
                        'tos':'int',
                        'table':'int',
                        'protocol':'string',
                        'scope':'string',
                        'metric':'int',
                        'nexthop':'undefined',
                        'via':'ip_addr_t',
                        'dev':'string',
                        'weight':'int',
                        'nhflags':'int',
                        'mtu':'int',
                        'advmss':'int',
                        'rtt':'int',
                        'rttvar':'int',
                        'reordering':'int',
                        'window':'int',
                        'cwnd':'int',
                        'ssthresh':'int',
                        'realms':'int',
                        'rto_min':'time_t',
                        'initcwnd':'int',
                        'initrwnd':'int',
                        'qickack':'undefined',
                        'congctl':'undefined',
                        'features':'undefined',
                        'src':'ip_addr_t',
                        'hoplimit':'undefined',
                        'pref':'undefined',
                        'expires':'undefined',
                        'options':'string',
                }],
            }],
        )
        Description:
        Add/Delete/Change/Append/Replace route using the below command
        - ip route { add | del | change | append | replace } ROUTE
        ROUTE := NODE_SPEC [ INFO_SPEC ]
        NODE_SPEC := [ TYPE ] PREFIX [ tos TOS ] [ table TABLE_ID ] [ proto RTPROTO ] [ scope SCOPE ]
          [ metric METRIC ] [ ttl-propagate { enabled | disabled } ]
        INFO_SPEC := NH OPTIONS FLAGS [ nexthop NH ] ...
        NH := [ encap ENCAP ] [ via [ FAMILY ] ADDRESS ] [ dev STRING ] [ weight NUMBER ] NHFLAGS
        FAMILY := [ inet | inet6 | ipx | dnet | mpls | bridge | link ]
        OPTIONS := FLAGS [ mtu NUMBER ] [ advmss NUMBER ] [ as [ to ] ADDRESS ] rtt TIME ] [ rttvar TIME ]
          [ reordering NUMBER ] [ window NUMBER ] [ cwnd NUMBER ] [ ssthresh NUMBER ] [ realms REALM ]
          [ rto_min TIME ] [ initcwnd NUMBER ] [ initrwnd NUMBER ] [ features FEATURES ] [ quickack BOOL ]
          [ congctl NAME ] [ pref PREF ] [ expires TIME ] [ fastopen_no_cookie BOOL ]
        TYPE := [ unicast | local | broadcast | multicast | throw | unreachable | prohibit | blackhole | nat ]
        TABLE_ID := [ local| main | default | all | NUMBER ]
        SCOPE := [ host | link | global | NUMBER ]
        NHFLAGS := [ onlink | pervasive ]
        RTPROTO := [ kernel | boot | static | NUMBER ]
        FEATURES := [ ecn | ]
        PREF := [ low | medium | high ]
        ENCAP := [ ENCAP_MPLS | ENCAP_IP | ENCAP_BPF | ENCAP_SEG6 | ENCAP_SEG6LOCAL ]
        ENCAP_MPLS := mpls [ LABEL ] [ ttl TTL ]
        ENCAP_IP := ip id TUNNEL_ID dst REMOTE_IP [ tos TOS ] [ ttl TTL ]
        ENCAP_BPF := bpf [ in PROG ] [ out PROG ] [ xmit PROG ] [ headroom SIZE ]
        ENCAP_SEG6 := seg6 mode [ encap | inline | l2encap ] segs SEGMENTS [ hmac KEYID ]
        ENCAP_SEG6LOCAL := seg6local action SEG6_ACTION [ SEG6_ACTION_PARAM ]

        """
        return await IpRoute._run_command("replace", *argv, **kwarg)

    async def get(*argv, **kwarg):
        """
        Platforms: ['dentos', 'cumulus']
        Usage:
        IpRoute.get(
            input_data = [{
                # device 1
                'dev1' : [{
                    # command 1
                        'dst':'ip_addr_t',
                        'from':'undefined',
                        'iif':'undefined',
                        'oif':'undefined',
                        'tos':'int',
                        'mark':'undefined',
                        'vrf':'undefined',
                        'ipproto':'undefined',
                        'sport':'undefined',
                        'dport':'undefined',
                        'options':'string',
                }],
            }],
        )
        Description:
        Get the details of the route
        - ip route get ROUTE_GET_FLAGS ADDRESS [ from ADDRESS iif STRING ] [ oif STRING ] [ mark MARK ]
          [ tos TOS ] [ vrf NAME ] [ ipproto PROTOCOL ] [ sport NUMBER ] [ dport NUMBER ]
        ROUTE_GET_FLAGS := [ fibmatch ]

        """
        return await IpRoute._run_command("get", *argv, **kwarg)

    async def show(*argv, **kwarg):
        """
        Platforms: ['dentos', 'cumulus']
        Usage:
        IpRoute.show(
            input_data = [{
                # device 1
                'dev1' : [{
                    # command 1
                        'dst':'ip_addr_t',
                        'root':'undefined',
                        'match':'undefined',
                        'exact':'undefined',
                        'table':'int',
                        'protocol':'string',
                        'type':'string',
                        'scope':'string',
                        'options':'string',
                }],
            }],
        )
        Description:
        Show/Flush the route
        ip route { list | flush } SELECTOR
        SELECTOR := [ root PREFIX ] [ match PREFIX ] [ exact PREFIX ]
                [ table TABLE_ID ] [ vrf NAME ] [ proto RTPROTO ]
                [ type TYPE ] [ scope SCOPE ]
        TYPE := [ unicast | local | broadcast | multicast | throw | unreachable | prohibit | blackhole | nat ]
        TABLE_ID := [ local| main | default | all | NUMBER ]
        SCOPE := [ host | link | global | NUMBER ]
        RTPROTO := [ kernel | boot | static | NUMBER ]

        """
        return await IpRoute._run_command("show", *argv, **kwarg)

    async def flush(*argv, **kwarg):
        """
        Platforms: ['dentos', 'cumulus']
        Usage:
        IpRoute.flush(
            input_data = [{
                # device 1
                'dev1' : [{
                    # command 1
                        'dst':'ip_addr_t',
                        'root':'undefined',
                        'match':'undefined',
                        'exact':'undefined',
                        'table':'int',
                        'protocol':'string',
                        'type':'string',
                        'scope':'string',
                        'options':'string',
                }],
            }],
        )
        Description:
        Show/Flush the route
        ip route { list | flush } SELECTOR
        SELECTOR := [ root PREFIX ] [ match PREFIX ] [ exact PREFIX ]
                [ table TABLE_ID ] [ vrf NAME ] [ proto RTPROTO ]
                [ type TYPE ] [ scope SCOPE ]
        TYPE := [ unicast | local | broadcast | multicast | throw | unreachable | prohibit | blackhole | nat ]
        TABLE_ID := [ local| main | default | all | NUMBER ]
        SCOPE := [ host | link | global | NUMBER ]
        RTPROTO := [ kernel | boot | static | NUMBER ]

        """
        return await IpRoute._run_command("flush", *argv, **kwarg)

    async def save(*argv, **kwarg):
        """
        Platforms: ['dentos', 'cumulus']
        Usage:
        IpRoute.save(
            input_data = [{
                # device 1
                'dev1' : [{
                    # command 1
                        'root':'undefined',
                        'match':'undefined',
                        'exact':'undefined',
                        'table':'int',
                        'protocol':'string',
                        'type':'string',
                        'scope':'string',
                        'options':'string',
                }],
            }],
        )
        Description:
        Save the route config
        ip route save SELECTOR
        SELECTOR := [ root PREFIX ] [ match PREFIX ] [ exact PREFIX ]
                [ table TABLE_ID ] [ vrf NAME ] [ proto RTPROTO ]
                [ type TYPE ] [ scope SCOPE ]
        TYPE := [ unicast | local | broadcast | multicast | throw | unreachable | prohibit | blackhole | nat ]
        TABLE_ID := [ local| main | default | all | NUMBER ]
        SCOPE := [ host | link | global | NUMBER ]
        RTPROTO := [ kernel | boot | static | NUMBER ]

        """
        return await IpRoute._run_command("save", *argv, **kwarg)

    async def restore(*argv, **kwarg):
        """
        Platforms: ['dentos', 'cumulus']
        Usage:
        IpRoute.restore(
            input_data = [{
                # device 1
                'dev1' : [{
                    # command 1

                }],
            }],
        )
        Description:
        Restore the route ip route restore

        """
        return await IpRoute._run_command("restore", *argv, **kwarg)

