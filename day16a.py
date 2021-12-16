import fileinput
from typing import List, final


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
    def __init__(self, version: int, subpackets: List[Packet]) -> None:
        Packet.__init__(self, version)
        self.subpackets = subpackets
        pass


def to_binary(s: str) -> int:
    value = 0
    for i in range(len(s)):
        if s[i] == "1":
            value += 2 ** (len(s) - 1 - i)

    return value


def parse_packet(s: str):
    version = to_binary(s[0:3])
    typeid = to_binary(s[3:6])
    if typeid == 4:
        pos = 6
        bits = ""
        while True:
            bits += s[(pos + 1):(pos + 5)]
            if s[pos] == "0":
                break
            pos += 5

        return LiteralPacket(version, to_binary(bits)), pos + 5
    else:
        subpackets = []
        # length_typeid
        if s[6] == "0":
            bit_length = to_binary(s[7:22])
            pos = 0
            while pos != bit_length:
                subpacket, new_pos = parse_packet(s[(22 + pos):])
                subpackets.append(subpacket)
                pos += new_pos
            return OperatorPacket(version, subpackets)
        else:
            return None


input = map(str.rstrip, fileinput.input())

line = next(input)

packet, pos = parse_packet(line)

print(int(packet))
print(pos)
