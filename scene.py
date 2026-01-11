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


class LogoStatic(Scene):
    def construct(self):
        # Separate symbols for individual control
        scale = 10
        mu = MathTex(r"M").scale(scale)      # Bigger M
        emptyset = MathTex(r"\emptyset").scale(scale)  # Bigger empty set
        integral = MathTex(r"\int").scale(scale)  # Bigger integral
        
        # Scale integral smaller
        integral.scale(0.5)  # 50% of default size
        
        # Group them horizontally with tight spacing
        group = VGroup(mu, emptyset, integral).arrange(RIGHT, buff=0.05)
        
        group.move_to(ORIGIN)
        
        self.play(Write(group))
        self.wait(1)

        # Render black background
        # manim -pqk --save_last_frame -r 2048,2048 scene.py LogoStatic -o MOS_logo.png



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
