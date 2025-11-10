def demo_arithmetic(a: int, b: int) -> dict:
    return {
        "a+b": a + b,
        "a-b": a - b,
        "a*b": a * b,
        "a/b": a / b,
        "a//b": a // b,
        "a%b": a % b,
        "a**b": a ** b,
    }

def demo_comparisons(a: int, b: int) -> dict:
    return {
        "a==b": a == b,
        "a!=b": a != b,
        "a>b": a > b,
        "a>=b": a >= b,
        "a<b": a < b,
        "a<=b": a <= b,
    }

def demo_logic(x: bool, y: bool) -> dict:
    return {
        "x and y": x and y,
        "x or y": x or y,
        "not x": not x,
    }

