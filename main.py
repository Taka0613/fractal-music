from constants import PATTERN_RED
from fractal.scale_maker import generate_scale


if __name__ == "__main__":
    a_scale_pattern_red = generate_scale(PATTERN_RED, "A")
    print(a_scale_pattern_red) # ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'A']

    d_scale_pattern_red = generate_scale(PATTERN_RED, "D")
    print(d_scale_pattern_red) # ['D', 'E', 'F', 'G', 'A', 'Bb', 'C', 'D']
