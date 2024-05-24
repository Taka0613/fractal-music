from constants import PATTERN_RED
from fractal.scale_maker import generate_scale



if __name__ == "__main__":
    result = generate_scale(PATTERN_RED, "A")
    print(result)