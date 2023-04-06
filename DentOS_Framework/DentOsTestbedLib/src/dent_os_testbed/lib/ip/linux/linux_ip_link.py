# Copyright 2020 Amazon.com, Inc. or its affiliates. All Rights Reserved.
#
# generated using file ./gen/model/linux/network/ip/link.yaml
#
# DONOT EDIT - generated by diligent bots

from dent_os_testbed.lib.test_lib_object import TestLibObject
class LinuxIpLink(TestLibObject):
    """
        ip-link - network device configuration
        - ip link { COMMAND | help }
        - ip link add [ link DEVICE ] [ name ] NAME [ txqueuelen PACKETS ] [ address LLADDR ] [ broadcast LLADDR ]
          [ mtu MTU ] [ index IDX ] [ numtxqueues QUEUE_COUNT ] [ numrxqueues QUEUE_COUNT ] [ gso_max_size BYTES ]
          [ gso_max_segs SEGMENTS ] type TYPE [ ARGS ]
        - ip link delete { DEVICE | group GROUP } type TYPE [ ARGS ]
        - ip link set { DEVICE | group GROUP } [ { up | down } ] [ type ETYPE TYPE_ARGS ] [ arp { on | off } ]
          [ dynamic { on | off } ] [ multicast { on | off } ] [ allmulticast { on | off } ] [ promisc { on | off } ]
          [ protodown { on | off } ] [ trailers { on | off } ] [ txqueuelen PACKETS ] [ name NEWNAME ] [ address LLADDR ]
          [ broadcast LLADDR ] [ mtu MTU ] [ netns { PID | NETNSNAME } ] [ link-netnsid ID ] [ alias NAME ] [ vf NUM [ mac LLADDR ]
          [ VFVLAN-LIST ] [ rate TXRATE ] [ max_tx_rate TXRATE ] [ min_tx_rate TXRATE ] [ spoofchk { on | off } ]
          [ query_rss { on | off } ] [ state { auto | enable | disable } ] [ trust { on | off } ] [ node_guid eui64 ]
          [ port_guid eui64 ] ] [ { xdp | xdpgeneric | xdpdrv | xdpoffload } { off | object FILE [ section NAME ] [ verbose ] |
          pinned FILE } ] [ master DEVICE ] [ nomaster ] [ vrf NAME ] [ addrgenmode { eui64 | none | stable_secret | random } ]
          [ macaddr { flush | { add | del } MACADDR | set [ MACADDR [ MACADDR [ ... ] ] ] } ]
        = ip link show [ DEVICE | group GROUP ] [ up ] [ master DEVICE ] [ type ETYPE ] [ vrf NAME ]
        - ip link xstats type TYPE [ ARGS ]
        - ip link afstats [ dev DEVICE ]
        - ip link help [ TYPE ]
        TYPE := [ bridge | bond | can | dummy | hsr | ifb | ipoib | macvlan | macvtap | vcan | vxcan | veth | vlan | vxlan
          | ip6tnl | ipip | sit | gre | gretap | erspan | ip6gre | ip6gretap | ip6erspan | vti | nlmon | ipvlan | ipvtap
          | lowpan | geneve | vrf | macsec | netdevsim | rmnet ]
        ETYPE := [ TYPE | bridge_slave | bond_slave ]
        VFVLAN-LIST := [ VFVLAN-LIST ] VFVLAN
        VFVLAN := [ vlan VLANID [ qos VLAN-QOS ] [ proto VLAN-PROTO ] ]

    """
    def format_add(self, command, *argv, **kwarg):
        raise NotImplementedError

    def parse_add(self, command, output, *argv, **kwarg):
        raise NotImplementedError

    def format_delete(self, command, *argv, **kwarg):
        raise NotImplementedError

    def parse_delete(self, command, output, *argv, **kwarg):
        raise NotImplementedError

    def format_set(self, command, *argv, **kwarg):
        raise NotImplementedError

    def parse_set(self, command, output, *argv, **kwarg):
        raise NotImplementedError

    def format_show(self, command, *argv, **kwarg):
        raise NotImplementedError

    def parse_show(self, command, output, *argv, **kwarg):
        raise NotImplementedError

    def format_command(self, command, *argv, **kwarg):
        if command in ['add']:
            return self.format_add(command, *argv, **kwarg)

        if command in ['delete']:
            return self.format_delete(command, *argv, **kwarg)

        if command in ['set']:
            return self.format_set(command, *argv, **kwarg)

        if command in ['show', 'xstats', 'afstats']:
            return self.format_show(command, *argv, **kwarg)


        raise NameError("Cannot find command "+command)

    def parse_output(self, command, output, *argv, **kwarg):
        if command in ['add']:
            return self.parse_add(command, output, *argv, **kwarg)

        if command in ['delete']:
            return self.parse_delete(command, output, *argv, **kwarg)

        if command in ['set']:
            return self.parse_set(command, output, *argv, **kwarg)

        if command in ['show', 'xstats', 'afstats']:
            return self.parse_show(command, output, *argv, **kwarg)


        raise NameError("Cannot find command "+command)

