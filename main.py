from constants import *
from fractal.scale_maker import generate_twelve_outputs, generate_scale


if __name__ == "__main__":
    STARTING_NOTE = 'F'
    result = generate_twelve_outputs(UNDERLYING_STRUTURE, DYNAMIC_CIRCULAR, STARTING_NOTE)
    for i in range(len(DYNAMIC_CIRCULAR)):
        if DYNAMIC_CIRCULAR[i] == STARTING_NOTE:
            print(DYNAMIC_CIRCULAR[i:] + DYNAMIC_CIRCULAR[:i])
    [print(scale) for scale in result]

    # print(generate_scale(STAR_V,'C#'))
