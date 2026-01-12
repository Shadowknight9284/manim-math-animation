"""
Euler's Formula Derivation: e^(ix) = cos(x) + i*sin(x)
Demonstrates the transformation from Taylor series to trigonometric form.

Visual Flow:
1. Show e^x expansion
2. Substitute ix to get e^(ix)
3. Evaluate powers of i (i^1=i, i^2=-1, i^3=-i, i^4=1)
4. Group even/odd terms
5. Recognize cos(x) and sin(x) series
6. Final Euler identity

Best Practices Applied:
- Helper functions to reduce code duplication
- Consistent styling via design system
- Modular scene structure for easier iteration
- Clear VGroup organization with submobject tracking
- Minimal string concatenation; f-strings where needed
"""

from manim import *

# ============================================================================
# HELPER FUNCTIONS - Extract repeated logic
# ============================================================================

def create_series_terms(n_terms=6, coefficient="1", exponent_var="x", evaluated=False):
    """
    Generate series terms with consistent formatting.
    
    Args:
        n_terms: Number of terms to generate (0 to n_terms-1)
        coefficient: Prefix for fraction (e.g., "1", "i", "ix")
        exponent_var: Variable in exponent (e.g., "x", "ix")
        evaluated: If True, evaluate i^n to actual values (i, -1, -i, 1)
    
    Returns:
        VGroup of formatted MathTex terms
    """
    terms = VGroup()
    
    for n in range(n_terms):
        if n == 0:
            # First term is always 1
            term = MathTex("1")
            terms.add(term)
        else:
            # Determine sign and coefficient based on position
            if evaluated:
                # Evaluate i^n cycle: i^1=i, i^2=-1, i^3=-i, i^4=1
                cycle_pos = n % 4
                if cycle_pos == 1:
                    sign, coeff = "+", "i"
                elif cycle_pos == 2:
                    sign, coeff = "-", ""
                elif cycle_pos == 3:
                    sign, coeff = "-", "i"
                else:  # cycle_pos == 0
                    sign, coeff = "+", ""
                
                numerator = f"{coeff} x^{{{n}}}" if coeff else f"x^{{{n}}}"
                term = MathTex(sign, f"\\frac{{{numerator}}}{{n!}}")
            else:
                # General form: show i^n or (ix)^n
                if exponent_var == "ix":
                    # Show (ix)^n expanded
                    term = MathTex("+", f"\\frac{{({exponent_var})^{{{n}}}}}{{n!}}")
                elif coefficient == "i^n":
                    # Show i^n factored out
                    term = MathTex("+", f"\\frac{{i^{{{n}}} x^{{{n}}}}}{{n!}}")
                else:
                    # Generic x^n form
                    term = MathTex("+", f"\\frac{{x^{{{n}}}}}{{n!}}")
            
            terms.add(term)
    
    # Arrange horizontally with consistent spacing
    terms.arrange(RIGHT, buff=0.15)
    return terms


def position_vgroup_below(target, reference, distance=0.5):
    """
    Position target group below reference with consistent spacing.
    
    Args:
        target: VGroup to reposition
        reference: Reference VGroup for alignment
        distance: Vertical distance below reference
    """
    target.next_to(reference, DOWN, buff=distance)
    return target


# ============================================================================
# SCENE 1: Step-by-step transformation from e^x to Euler's formula
# ============================================================================

class EulerTaylorToTrig(Scene):
    """
    Main scene: Visually derive e^(ix) = cos(x) + i*sin(x) via Taylor series.
    
    Flow:
    - Write e^x Taylor series
    - Substitute ix
    - Evaluate i^n powers
    - Group even/odd terms
    - Recognize trig series
    """
    
    def construct(self):
        self.show_exponential_series()
        self.substitute_imaginary()
        self.evaluate_powers_of_i()
        self.separate_and_group()
        self.reveal_trig_forms()

    def show_exponential_series(self):
        """Display e^x = sum(x^n / n!)"""
        # Header: e^x formula
        exp = MathTex("e^{x}")
        equals_and_sum = MathTex("=", r"\sum_{n=0}^{\infty}", r"\frac{x^{n}}{n!}")
        
        header = VGroup(exp, equals_and_sum).arrange(RIGHT, buff=0.3)
        header.move_to(ORIGIN)
        
        self.play(Write(header), run_time=1.5)
        self.wait(1)
        
        # Move header up to make room for expanded terms
        self.play(header.animate.to_edge(UP), run_time=1, rate_func=smooth)
        
        # Expanded series: 1 + x + x^2/2! + x^3/3! + ...
        expanded = create_series_terms(n_terms=6, exponent_var="x", evaluated=False)
        position_vgroup_below(expanded, header, distance=0.5)
        
        self.play(Write(expanded), run_time=1.5)
        self.wait(1)
        
        # Store for later transforms
        self.header = header
        self.expanded_x = expanded

    def substitute_imaginary(self):
        """Transform e^x → e^(ix) and substitute into series."""
        # Replace e^x with e^(ix)
        exp_ix = MathTex("e^{ix}")
        
        # Keep equals and sum the same, but update fraction
        equals_and_sum_ix = MathTex("=", r"\sum_{n=0}^{\infty}", r"\frac{(ix)^{n}}{n!}")
        
        new_header = VGroup(exp_ix, equals_and_sum_ix).arrange(RIGHT, buff=0.3)
        new_header.move_to(self.header)
        
        self.play(
            Transform(self.header, new_header),
            run_time=1.5,
            rate_func=smooth
        )
        self.wait(1)
        
        # Update series terms: 1 + ix + (ix)^2/2! + (ix)^3/3! + ...
        expanded_ix = create_series_terms(n_terms=6, exponent_var="ix", evaluated=False)
        expanded_ix.move_to(self.expanded_x)
        
        self.play(
            Transform(self.expanded_x, expanded_ix),
            run_time=1.5,
            rate_func=smooth
        )
        self.wait(1)

    def evaluate_powers_of_i(self):
        """
        Show the cycle of i^n:
        i^1 = i, i^2 = -1, i^3 = -i, i^4 = 1, i^5 = i, ...
        """
        # Stage 1: Factor out i^n → show (ix)^n = i^n * x^n
        factored = create_series_terms(n_terms=6, coefficient="i^n", evaluated=False)
        factored.move_to(self.expanded_x)
        
        self.play(
            Transform(self.expanded_x, factored),
            run_time=1.5,
            rate_func=smooth
        )
        self.wait(0.5)
        
        # Stage 2: Evaluate i^n cycle (i, -1, -i, 1)
        evaluated = create_series_terms(n_terms=6, evaluated=True)
        evaluated.move_to(self.expanded_x)
        
        self.play(
            Transform(self.expanded_x, evaluated),
            run_time=1.5,
            rate_func=smooth
        )
        self.wait(1)

    def separate_and_group(self):
        """
        Highlight even terms (YELLOW → cos) and odd terms (BLUE → sin).
        Shift odd terms downward for visual separation.
        """
        # Identify even and odd indices
        n_terms = len(self.expanded_x)
        even_indices = [i for i in range(n_terms) if i % 2 == 0]
        odd_indices = [i for i in range(n_terms) if i % 2 == 1]
        
        # Extract submobjects into new VGroups (Manim fix: can't slice with list)
        even_group = VGroup(*[self.expanded_x[i] for i in even_indices])
        odd_group = VGroup(*[self.expanded_x[i] for i in odd_indices])
        
        # Color and shift
        self.play(
            even_group.animate.set_color(YELLOW),
            odd_group.animate.set_color(BLUE),
            run_time=1
        )
        self.wait(0.5)
        
        self.play(
            odd_group.animate.shift(DOWN * 1.5),
            run_time=1,
            rate_func=smooth
        )
        self.wait(1)
        
        # Store for next step
        self.even_group = even_group
        self.odd_group = odd_group

    def reveal_trig_forms(self):
        """
        Transform grouped terms into clean cos(x) and sin(x) series,
        then equate to the actual functions.
        """
        # Build clean cos series: 1 - x^2/2! + x^4/4! - ...
        cos_series = VGroup(
            MathTex("1"),
            MathTex("-", r"\frac{x^{2}}{2!}"),
            MathTex("+", r"\frac{x^{4}}{4!}")
        ).arrange(RIGHT, buff=0.15)
        cos_series.set_color(YELLOW)
        cos_series.move_to(self.even_group)
        
        # Build clean sin series: i(x - x^3/3! + x^5/5! - ...)
        sin_series = VGroup(
            MathTex(r"i \left("),
            MathTex(r"\frac{x}{1!}"),
            MathTex("-", r"\frac{x^{3}}{3!}"),
            MathTex("+", r"\frac{x^{5}}{5!}"),
            MathTex(r"\right)")
        ).arrange(RIGHT, buff=0.1)
        sin_series.set_color(BLUE)
        sin_series.move_to(self.odd_group)
        
        self.play(
            Transform(self.even_group, cos_series),
            Transform(self.odd_group, sin_series),
            run_time=1.5,
            rate_func=smooth
        )
        self.wait(1)
        
        # Add equality labels
        cos_label = MathTex("= \\cos(x)").set_color(YELLOW)
        cos_label.next_to(cos_series, RIGHT, buff=0.2)
        
        sin_label = MathTex("= i \\sin(x)").set_color(BLUE)
        sin_label.next_to(sin_series, RIGHT, buff=0.2)
        
        self.play(
            Write(cos_label),
            Write(sin_label),
            run_time=1.5
        )
        self.wait(2)


# ============================================================================
# SCENE 2: Final Euler Identity - Clean derivation
# ============================================================================

class FinalEulerIdentity(Scene):
    """
    Clean, compact final derivation: e^(ix) = cos(x) + i*sin(x)
    
    Uses mathematical manipulation to show the progression concisely.
    """
    
    def construct(self):
        self.show_full_expansion()
        self.separate_even_odd()
        self.collapse_to_trig()
        self.finale()

    def show_full_expansion(self):
        """Start with e^(ix) = sum of (ix)^n / n!"""
        full_eq = VGroup(
            MathTex("e^{ix}"),
            MathTex("="),
            MathTex(r"\sum_{n=0}^{\infty}"),
            MathTex(r"\frac{(ix)^{n}}{n!}")
        ).arrange(RIGHT, buff=0.2)
        full_eq.move_to(ORIGIN)
        
        self.play(Write(full_eq), run_time=1.5)
        self.wait(1)
        
        self.full_eq = full_eq

    def separate_even_odd(self):
        """Split into even and odd summations."""
        split_eq = VGroup(
            MathTex("e^{ix}"),
            MathTex("="),
            MathTex(r"\sum_{k=0}^{\infty} \frac{(ix)^{2k}}{(2k)!}"),
            MathTex("+"),
            MathTex(r"\sum_{k=0}^{\infty} \frac{(ix)^{2k+1}}{(2k+1)!}")
        ).arrange(RIGHT, buff=0.15)
        split_eq.scale(0.9)  # Fit on screen
        split_eq.move_to(ORIGIN)
        
        self.play(Transform(self.full_eq, split_eq), run_time=1.5)
        self.wait(1)

    def collapse_to_trig(self):
        """Step-by-step: even sum → cos, odd sum → i*sin."""
        # Step 1: Replace even sum with cos(x)
        with_cos = VGroup(
            MathTex("e^{ix}"),
            MathTex("="),
            MathTex(r"\cos(x)").set_color(YELLOW),
            MathTex("+"),
            MathTex(r"\sum_{k=0}^{\infty} \frac{(ix)^{2k+1}}{(2k+1)!}")
        ).arrange(RIGHT, buff=0.15)
        with_cos.scale(0.9)
        with_cos.move_to(ORIGIN)
        
        self.play(Transform(self.full_eq, with_cos), run_time=1.5)
        self.wait(1)
        
        # Step 2: Replace odd sum with i*sin(x)
        final_form = VGroup(
            MathTex("e^{ix}"),
            MathTex("="),
            MathTex(r"\cos(x)").set_color(YELLOW),
            MathTex("+"),
            MathTex(r"i \sin(x)").set_color(BLUE)
        ).arrange(RIGHT, buff=0.2)
        final_form.move_to(ORIGIN)
        
        self.play(Transform(self.full_eq, final_form), run_time=1.5)
        self.wait(1)

    def finale(self):
        """Highlight the final identity with emphasis."""
        # Extract the core identity for emphasis
        identity = VGroup(
            MathTex("e^{ix}"),
            MathTex("="),
            MathTex(r"\cos(x) + i \sin(x)")
        ).arrange(RIGHT, buff=0.3)
        identity.scale(1.3)
        identity.move_to(ORIGIN + UP * 0.5)
        
        self.play(
            FadeOut(self.full_eq),
            Write(identity),
            run_time=1.5
        )
        self.wait(2)
        
        # Add label: Euler's Identity
        label = MathTex(r"\text{Euler's Identity}").scale(0.8)
        label.next_to(identity, DOWN, buff=0.5)
        label.set_color(GREEN)
        
        self.play(Write(label), run_time=1)
        self.wait(2)
