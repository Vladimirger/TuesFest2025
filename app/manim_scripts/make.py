manim_code = r"""
from manim import *

class ExampleScene(Scene):
    def construct(self):
        # Simpler equation first
        simple_eq = MathTex(r"f(x) = x^2")
        self.play(Write(simple_eq))
        self.wait(1)
"""

with open("manim_script.py", "w") as f:
    f.write(manim_code)

import subprocess

subprocess.run([
    "manim",
    "-pql",
    "manim_script.py",
    "ExampleScene"
])