from constants import *
from fractal.scale_maker import generate_twelve_outputs


if __name__ == "__main__":
    result = generate_twelve_outputs(UNDERLYING_STRUTURE, DYNAMIC_CIRCULAR, "A")
    [print(scale) for scale in result]