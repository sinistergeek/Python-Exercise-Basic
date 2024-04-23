import math
def euclidean(pixel:RGB,color:Color) -> float:
    return math.sqrt(
        sum(map(
            lambda x,y: (x-y)**2,
            pixel,
            color.rgb
        ))
    )

def manhattan(pixel:RBG,color:Color) -> float:
    return sum(map(
        lambda x,y: abs(x-y),
        pixel,
        color.rgb
    ))
