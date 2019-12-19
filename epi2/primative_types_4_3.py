import math

class ReverseBits(object):
    def __init__(self):
        self.r_sections = {}
        self.sec_size = 16

    def swap(self, i, j, bits):
        swapped = bits

        if ((bits >> i) & 1) != ((bits >> j) & 1):
            mask = 1 << i | 1 << j
            swapped = bits ^ mask

        return swapped

    def reverse_section(self, bits, section_idx):
        section_mask = int('ffff', 16)
        section = (bits >> (section_idx * self.sec_size)) & section_mask # parens not needed - only for understanding
        r_sec = self.r_sections.get(section)
        if r_sec is None:
            r_sec = section
            for i in range(8):
                r_sec = self.swap(i, self.sec_size - 1 - i, r_sec)
            self.r_sections[section] = r_sec

        return r_sec

    def reverse(self, bits):
        degree = int(math.log(bits, 2))
        s1 = self.reverse_section(bits, 3)
        s2 = self.reverse_section(bits, 2) << self.sec_size
        s3 = self.reverse_section(bits, 1) << 2 * self.sec_size
        s4 = self.reverse_section(bits, 0) << 3 * self.sec_size

        return (s4 | s3 | s2 | s1) >> (63 - degree)



if __name__ == "__main__":
    x = ['0'] * 32
    y =  ['0'] * 32
    y[:3] = ['1'] * 3
    y[31] = '1'
    a = ''.join(x + y)
    print(a)
    reverse_bits =  ReverseBits()
    rev = reverse_bits.reverse(int(a, 2))
    print(bin(rev)[2:])
      