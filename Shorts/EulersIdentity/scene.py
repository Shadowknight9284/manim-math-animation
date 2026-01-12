from manim import *

class EulerTaylorToTrig(Scene):
    def construct(self):
        # 1. e^x expansion
        exp_group = VGroup()
        exp = MathTex("e^{x}")
        equals = MathTex("=", r"\sum_{n=0}^{\infty}", r"\frac{x^{n}}{n!}")
        exp_group.add(exp, equals)
        exp_group.arrange(RIGHT)
        exp_group.move_to(ORIGIN)
        self.play(Write(exp_group))
        self.wait(2)
        self.play(exp_group.animate.to_edge(UP), run_time=1, rate_func=smooth)
        
        # 2. Show expansion terms
        terms = VGroup()
        term = MathTex(r"1")
        terms.add(term)
        for n in range(6):
            if n > 0:
                term = MathTex("+", r"\frac{x^{" + str(n) + r"}}{" + str((n)) + r"!}")
            terms.add(term)
        terms.arrange(RIGHT)
        terms.next_to(exp_group, DOWN, buff=0.5)
        self.play(Write(terms))
        self.wait(1)

        # display e^(ix) by editing original e^x 
        exp_ix = MathTex("e^{ix}")
        equals_ix = MathTex("=", r"\sum_{n=0}^{\infty}", r"\frac{(ix)^{n}}{n!}")
        exp_ix_group = VGroup(exp_ix, equals_ix).arrange(RIGHT).move_to(exp_group)
        self.play(Transform(exp, exp_ix), Transform(equals, equals_ix))
        self.wait(2)
        
        # edit the term wise expansion to ix^n
        terms_ix = VGroup()
        term = MathTex(r"1")
        terms_ix.add(term)
        for n in range(6):
            if n > 0:
                term = MathTex("+", r"\frac{(ix)^{" + str(n) + r"}}{" + str((n)) + r"!}")
            terms_ix.add(term)
        terms_ix.arrange(RIGHT)
        terms_ix.move_to(terms)
        self.play(Transform(terms, terms_ix))
        self.wait(.25)
        
        # Simplify terms to show i^n
        simplified_terms = VGroup()
        for n in range(6):
            if n == 0:
                term = MathTex(r"1")
                simplified_terms.add(term)
            else:
                power_of_i = "i^{" + str(n) + "}"
                term = MathTex("+", r"\frac{" + power_of_i + r"x^{" + str(n) + r"}}{" + str((n)) + r"!}")
            simplified_terms.add(term)
        simplified_terms.arrange(RIGHT)
        simplified_terms.move_to(terms)
        self.play(Transform(terms, simplified_terms))
        self.wait(.25)
        
        # Evaulate i^n to i, -1, -i, 1
        evaluated_terms = VGroup()
        for n in range(6):
            if n == 0:
                term = MathTex(r"1")
                evaluated_terms.add(term)
            else:
                if n % 4 == 1:
                    term = MathTex("+", r"\frac{i x^{" + str(n) + r"}}{" + str((n)) + r"!}")
                elif n % 4 == 2:
                    term = MathTex("-", r"\frac{1 x^{" + str(n) + r"}}{" + str((n)) + r"!}")
                elif n % 4 == 3:
                    term = MathTex("-", r"\frac{i x^{" + str(n) + r"}}{" + str((n)) + r"!}")
                else:
                    term = MathTex("+", r"\frac{1 x^{" + str(n) + r"}}{" + str((n)) + r"!}")
            evaluated_terms.add(term)
        evaluated_terms.arrange(RIGHT)
        evaluated_terms.move_to(terms)
        self.play(Transform(terms, evaluated_terms))
        self.wait(.25)
        
        # highlight even and odd terms
        even_terms = VGroup()
        odd_terms = VGroup()
        for i, term in enumerate(terms):
            if i % 2 == 0:
                even_terms.add(term)
            else:
                odd_terms.add(term)
        self.play(
            even_terms.animate.set_color(YELLOW),
            odd_terms.animate.set_color(BLUE)
        )
        self.wait(2)
        
        # Move the odd terms down 
        self.play(odd_terms.animate.shift(DOWN * 1.5))
        self.wait(1)
        
        # Transform to clean cosine and sine series
        cos_series = MathTex(r"1", r"-", r"\frac{x^{2}}{2!}", r"+", r"\frac{x^{4}}{4!}")
        cos_series.arrange(RIGHT, buff=0.15)
        cos_series.set_color(YELLOW)
        cos_series.move_to(even_terms)
        
        sin_series = MathTex(r"i \left( \frac{x^{1}}{1!}", r"-", r"\frac{x^{3}}{3!}", r"+", r"\frac{x^{5}}{5!}\right)")
        sin_series.arrange(RIGHT, buff=0.15)
        sin_series.set_color(BLUE)
        sin_series.move_to(odd_terms)
        
        self.play(
            Transform(even_terms, cos_series),
            Transform(odd_terms, sin_series)
        )
        self.wait(2)
        
        # Equate to cosine and sine respectively
        cos_with_eq = VGroup(
            MathTex(r"1", r"-", r"\frac{x^{2}}{2!}", r"+", r"\frac{x^{4}}{4!}").set_color(YELLOW),
            MathTex(r"= \cos{x}").set_color(YELLOW)
        ).arrange(RIGHT, buff=0.2)
        
        sin_with_eq = VGroup(
            MathTex(r"i \left( \frac{x^{1}}{1!}", r"-", r"\frac{x^{3}}{3!}", r"+", r"\frac{x^{5}}{5!}\right)").set_color(BLUE),
            MathTex(r"= i \sin{x}").set_color(BLUE)
        ).arrange(RIGHT, buff=0.2)
        
        # Align right edges
        sin_with_eq.align_to(cos_with_eq, RIGHT)
        
        # Position both near center
        both_eqs = VGroup(cos_with_eq, sin_with_eq)
        both_eqs.move_to(ORIGIN + DOWN * 0.5)
        cos_with_eq.shift(UP * 1.5)
        
        self.play(
            Transform(even_terms, cos_with_eq),
            Transform(odd_terms, sin_with_eq)
        )
        self.wait(2)

class FinalEulerIdentity(Scene):
    def construct(self):
        # write e^(ix) = summation
        full_eq = MathTex(r"e^{ix}", r"=", r"\sum_{n=0}^{\infty}", r"\frac{(ix)^{n}}{n!}")
        full_eq.move_to(ORIGIN)
        self.play(Write(full_eq))
        self.wait(1)
        
        # transform summation into split even and odd (on same line)
        split_form = MathTex(r"e^{ix}", r"=", r"\sum_{k=0}^{\infty}", r"\frac{(ix)^{2k}}{(2k)!}", r"+", r"\sum_{k=0}^{\infty}", r"\frac{(ix)^{2k+1}}{(2k+1)!}")
        split_form.move_to(ORIGIN)
        
        self.play(Transform(full_eq, split_form))
        self.wait(1)
        
        # transform even summation to cos
        with_cos = MathTex(r"e^{ix}", r"=", r"\cos{x}", r"+", r"\sum_{k=0}^{\infty}", r"\frac{(ix)^{2k+1}}{(2k+1)!}")
        with_cos.move_to(ORIGIN)
        
        self.play(Transform(full_eq, with_cos))
        self.wait(1)
        
        # transform odd summation to sin
        final_form = MathTex(r"e^{ix}", r"=", r"\cos{x}", r"+", r"i \sin{x}")
        final_form.move_to(ORIGIN)
        
        self.play(Transform(full_eq, final_form))
        self.wait(2)
        