from manim import *


class BasicScene(Scene):
    def construct(self):
        # Create a text object
        title = Text("Welcome to Measures of Success!", font_size=48)
        self.play(Write(title))
        self.wait(1)
        
        # Transform text
        subtitle = Text("Let's create animations!", font_size=36)
        self.play(Transform(title, subtitle))
        self.wait(2)


class MathScene(Scene):
    def construct(self):
        # Create a mathematical expression with LaTeX
        equation = MathTex(r"e^{i\pi} + 1 = 0")
        self.play(Write(equation))
        self.wait(1)
        
        # Scale the equation
        self.play(equation.animate.scale(1.5))
        self.wait(1)
        
        # Change color
        self.play(equation.animate.set_color(BLUE))
        self.wait(2)


class GeometryScene(Scene):
    def construct(self):
        # Create geometric shapes
        circle = Circle(radius=1, color=BLUE)
        square = Square(side_length=2, color=RED)
        triangle = Triangle(color=GREEN)
        
        # Arrange shapes
        shapes = VGroup(circle, square, triangle).arrange(RIGHT, buff=1)
        
        # Animate shapes
        self.play(Create(circle))
        self.play(Create(square))
        self.play(Create(triangle))
        self.wait(1)
        
        # Rotate all shapes
        self.play(shapes.animate.rotate(PI/4))
        self.wait(2)
