import fileinput
from typing import List, final


def hex_to_binary(c: str) -> str:
    if c == '0':
        return "0000"
    if c == '1':
        return "0001"
    if c == '2':
        return "0010"
    if c == '3':
        return "0011"
    if c == '4':
        return "0100"
    if c == '5':
        return "0101"
    if c == '6':
        return "0110"
    if c == '7':
        return "0111"
    if c == '8':
        return "1000"
    if c == '9':
        return "1001"
    if c == 'A':
        return "1010"
    if c == 'B':
        return "1011"
    if c == 'C':
        return "1100"
    if c == 'D':
        return "1101"
    if c == 'E':
        return "1110"
    if c == 'F':
        return "1111"


class Packet:
    def __init__(self, version: int) -> None:
        self.version = version


@final
class LiteralPacket(Packet):
    def __init__(self, version: int, value: int) -> None:
        Packet.__init__(self, version)
        self.value = value

    def __int__(self):
        return self.value


@final
class OperatorPacket(Packet):
    def __init__(self, version: int, typeid: int, subpackets: List[Packet]) -> None:
        Packet.__init__(self, version)
        self.subpackets = subpackets
        self.typeid = typeid
        pass


def to_binary(s: str) -> int:
    value = 0
    for i in range(len(s)):
        if s[i] == "1":
            value += 2 ** (len(s) - 1 - i)

    return value


def parse_packet(s: str, pos: int):
    version = to_binary(s[pos: (pos + 3)])
    typeid = to_binary(s[(pos + 3): (pos + 6)])
    if typeid == 4:
        local_pos = pos + 6
        bits = ""
        while True:
            bits += s[(local_pos + 1): (local_pos + 5)]
            if s[local_pos] == "0":
                break
            local_pos += 5

        return LiteralPacket(version, to_binary(bits)), local_pos + 5
    else:
        subpackets = []
        # length_typeid
        if s[pos + 6] == "0":
            bit_length = to_binary(s[(pos + 7): (pos + 22)])
            pos += 22
            end = pos + bit_length
            while pos != end:
                subpacket, pos = parse_packet(s, pos)
                subpackets.append(subpacket)
        else:
            num_subpackets = to_binary(s[(pos + 7): (pos + 18)])
            pos += 18
            for _ in range(num_subpackets):
                subpacket, pos = parse_packet(s, pos)
                subpackets.append(subpacket)

        return OperatorPacket(version, typeid, subpackets), pos


def sum_versions(p: Packet):
    if type(p) is LiteralPacket:
        return p.version
    elif type(p) is OperatorPacket:
        return p.version + sum([sum_versions(sp) for sp in p.subpackets])


input = map(str.rstrip, fileinput.input())

line = next(input)

binary_str = "".join([hex_to_binary(c) for c in line])

packet, pos = parse_packet(binary_str, 0)

print(sum_versions(packet))
