from __future__ import annotations

import math
from dataclasses import dataclass


@dataclass
class Packet:
    version: int
    type_id: int
    value: int
    sub_packets: list[Packet]
    size: int

    def version_sum(self) -> int:
        return self.version + sum(packet.version_sum() for packet in self.sub_packets)

    def exp_result(self) -> int:
        if self.type_id == 0:
            return sum(packet.exp_result() for packet in self.sub_packets)
        elif self.type_id == 1:
            return math.prod(packet.exp_result() for packet in self.sub_packets)
        elif self.type_id == 2:
            return min(packet.exp_result() for packet in self.sub_packets)
        elif self.type_id == 3:
            return max(packet.exp_result() for packet in self.sub_packets)
        elif self.type_id == 4:
            return self.value
        elif self.type_id == 5:
            return int(
                self.sub_packets[0].exp_result() > self.sub_packets[1].exp_result()
            )
        elif self.type_id == 6:
            return int(
                self.sub_packets[0].exp_result() < self.sub_packets[1].exp_result()
            )
        elif self.type_id == 7:
            return int(
                self.sub_packets[0].exp_result() == self.sub_packets[1].exp_result()
            )
        return 0

    @classmethod
    def from_bits(cls, bits: str) -> Packet:
        version = cls.bin_to_int(bits[0:3])
        type_id = cls.bin_to_int(bits[3:6])

        index = 6
        value = 0
        sub_packets: list[Packet] = []

        if type_id == 4:  # literal packet
            last_group = False
            bin_val = ""
            while not last_group:
                bin_val += bits[index + 1 : index + 5]
                last_group = bits[index] == "0"
                index += 5
            value = cls.bin_to_int(bin_val)
        else:  # operator packet
            length_type = int(bits[index])
            if length_type == 0:  # total length operator
                sub_packets_len = cls.bin_to_int(bits[7:22])
                index = 22
                while sum(packet.size for packet in sub_packets) < sub_packets_len:
                    p = Packet.from_bits(bits[index:])
                    sub_packets.append(p)
                    index += p.size
            else:  # contained packets operator
                num_sub_packets = cls.bin_to_int(bits[7:18])
                index = 18
                while len(sub_packets) < num_sub_packets:
                    p = Packet.from_bits(bits[index:])
                    sub_packets.append(p)
                    index += p.size
        return cls(version, type_id, value, sub_packets, size=index)

    @staticmethod
    def bin_to_int(binary: str) -> int:
        return int(binary, 2)


with open("input.txt") as f:
    hex_line = f.read().split()
packet_bits = "".join(map(lambda x: format(int(x, 16), "04b"), hex_line))
p = Packet.from_bits(packet_bits)

# 16
print(p.version_sum())

# 16b
print(p.exp_result())
