def parse_rgb(red: int, green: int, blue: int, alpha: float) -> tuple:
    red: float = red / 255
    green: float = green / 255
    blue: float = blue / 255
    alpha: float = alpha
    return red, green, blue, alpha
