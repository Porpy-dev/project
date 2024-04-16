from manim import *
from math import *
global_scale = 3
config.frame_height = 14.222222222222221
config.frame_width = 8.0
config.frame_size = (1080,1920)

class Trig_Circle(Scene):
    def construct(self):
        trig_circle = Circle(color=WHITE,
         fill_opacity= 0,
          radius= 1
        ).scale(global_scale)

        axe = Axes(
            color= WHITE,
            fill_opacity = 0,
            x_length= 2.6,
            y_length= 2.6,
            x_range=[-1.3, 1.3, 1],
            y_range=[-1.3, 1.3, 1],
            tips=True,

            axis_config={"stroke_width":4, "tip_width": 0.1, "tip_height": 0.1, "include_ticks":False}
        ).scale(global_scale)

        label_1_x = Tex("1", font_size= 34).move_to([global_scale+0.30, 0.35, 0.])
        label_neg1_x = Tex("-1", font_size= 34).move_to([-global_scale-0.35, 0.35, 0.])
        label_1_y = Tex("1", font_size= 34).move_to([-0.35, global_scale+0.30, 0.])
        label_neg1_y = Tex("-1", font_size= 34).move_to([-0.35,-global_scale-0.35, 0.])
        label_orgn = Tex("0", font_size= 34).move_to([-0.30, -0.30, 0.])
        first_dot = Dot(
            point = [1*global_scale/2, (sqrt(3)*global_scale/2), 0.],
            radius = 0.03,
            color= BLUE,
            ).scale(global_scale)
        
        sine_line = always_redraw(
            lambda: DashedLine(
        start=[0., first_dot.get_y(), 0.], 
        end=first_dot.get_center()).set_z_index(first_dot.z_index - 3))

        sine_text = Tex(r"sin($\alpha$)", font_size= 30).rotate(PI/2).add_updater(lambda x: x.move_to([-0.30, (first_dot.get_y())/2, 0.]))

        cosine_line = always_redraw(
            lambda: DashedLine(
        start=[first_dot.get_x(), 0., 0.], 
        end= first_dot.get_center()
        ).set_z_index(first_dot.z_index - 2))

        x_line = Line(start= [0., 0., 0.], end= [1., 0., 0.])
        y_line = Line(start= ORIGIN, end= [0., 1., 0.])

        cosine_text = always_redraw(
            lambda: Tex (r"cos($\alpha$)", font_size= 30).move_to([(first_dot.get_x())/2, -0.30, 0.])
        )
        cosine_text_2 = Tex (r"cos($\alpha$)", font_size= 30, color = WHITE).move_to([(sqrt(3)*global_scale)/4, -0.30, 0.])

        blue_sine = always_redraw(
            lambda: Line(start= ORIGIN, end= [0., first_dot.get_y(), 0.], color= BLUE))

        blue_cosine = always_redraw(
            lambda: Line(start= ORIGIN, end= [first_dot.get_x(), 0., 0.], color= BLUE))
            
        cos_proj = Line(start= ORIGIN, end= [sqrt(3)*global_scale/2, 0., 0.], color = BLUE)

        white_line = always_redraw(
            lambda: Line(start= ORIGIN, end= first_dot.get_center()).set_z_index(first_dot.z_index - 1)
        )
        alpha_angle = always_redraw(
            lambda: Angle(x_line, white_line, radius= 0.6, quadrant= (1, 1))
        )
        alpha_values = ValueTracker(PI/3)
        alpha_label = Tex(r"$\alpha$", font_size= 30).add_updater( lambda x: x.move_to([1.*cos(alpha_values.get_value()/2), 1.*sin(alpha_values.get_value()/2), 0.])
            )
        title = Tex(r"The Unit Circle", font_size = 42).move_to([0., 1.55*global_scale, 0.])
        pythagoras_explanation = Tex(r"Using Pythagoras' Theorem: ", font_size = 40).move_to([0.,-1.55*global_scale, 0.])
        py_formula = MathTex(r"sin^2(\alpha) + cos^2(\alpha) = 1", font_size = 40).next_to(pythagoras_explanation, DOWN)

        radius_indic = Tex("r = 1", font_size= 29).rotate(alpha_values.get_value()).add_updater(lambda x: x.move_to([(first_dot.get_x()/2)-0.15, (first_dot.get_y()/2)+0.15, 0]))
        radius_indic_1 = Tex("1", font_size= 29).rotate(PI/4).move_to([(sqrt(2)*global_scale/4)-0.15, (sqrt(2)*global_scale/4)+0.15, 0])

        value_display1 = MathTex(r"\alpha" + r"=" + r"\frac{\pi}{3}", font_size= 40).move_to([-global_scale-0.1, 0.85*global_scale, 0.])
        value_display2 = MathTex(r"\alpha" + r"=" + r"\frac{\pi}{4}", font_size= 40).move_to([-global_scale-0.1, 0.85*global_scale, 0.])
        value_display3 = MathTex(r"\alpha" + r"=" + r"\frac{3\pi}{4}", font_size= 40).move_to([-global_scale-0.1, 0.85*global_scale, 0.])
        value_display4 = MathTex(r"\alpha" + r"=" + r"\frac{\pi}{6}", font_size= 40).move_to([-global_scale-0.1, 0.85*global_scale, 0.])
        cadre = Rectangle(height= 0.35*global_scale, width= 0.50*global_scale).move_to([-global_scale-0.1, 0.85*global_scale, 0.])

        right_angle = RightAngle(sine_line, y_line, quadrant = (1, -1), length= 0.2, color= RED).set_z_index(axe.z_index - 1)
        right_angle.add_updater(lambda x: x.move_to([0.1, first_dot.get_y()-0.1, 0.]))

        

        self.play(Create(trig_circle), run_time= 1.2)
        self.wait(0.5)
        self.play(Create(axe), run_time= 1.2)
        self.play(Create(label_1_x), Create(label_1_y), Create (label_neg1_x), Create(label_neg1_y), Create(label_orgn), Create (title), run_time= 1.2)
        self.wait(0.3)
        self.play(Create(first_dot))
        self.wait(0.5)
        self.play(Create(white_line), Create(radius_indic))
        self.wait(0.5)
        self.play(Create(alpha_angle), FadeIn(alpha_label), Create(value_display1), Create(cadre, run_time= 1.2))
        self.wait(0.7)
        self.play(Create(sine_line))
        self.wait(0.4)
        self.play(Create(sine_text), Create(blue_sine))
        self.wait(0.7)
        self.play(Create(cosine_line))
        self.wait(0.4)
        self.play(Create(cosine_text), Create(blue_cosine))
        self.wait(0.7)
        self.play(Rotate(first_dot, about_point= ORIGIN, angle= -1*PI/12), alpha_values.animate.set_value(PI/4), Rotate(radius_indic, about_point= ORIGIN, angle= -PI/12), ReplacementTransform(radius_indic, radius_indic_1), ReplacementTransform(value_display1, value_display2))
        self.wait(0.8)
        self.play(Rotate(first_dot, about_point= ORIGIN, angle= PI/2, run_time = 1.3), alpha_values.animate.set_value(3*PI/4), Rotate(radius_indic_1, about_point= ORIGIN, angle= PI/2, run_time= 1.3), ReplacementTransform(value_display2, value_display3))
        self.wait(0.6)
        self.play(Rotate(first_dot, about_point= ORIGIN, angle= (PI+PI/4+PI/6), run_time = 1.5), alpha_values.animate.set_value(PI/6), ReplacementTransform(value_display3, value_display4), Rotate(radius_indic_1, about_point= ORIGIN, angle= PI+PI/4+PI/6, run_time= 1.5))
        self.wait(1.3)
        self.add(cos_proj)
        self.play(cos_proj.animate.put_start_and_end_on([0., global_scale/2, 0.], [sqrt(3)*global_scale/2, global_scale/2, 0.]))
        self.wait(0.7)
        self.play(Create(right_angle))
        self.play(cosine_text_2.animate.shift((0., (global_scale/2)+0.65, 0.)).set_color(BLUE), Create(pythagoras_explanation, run_time= 1.8))
        self.wait(0.2)
        self.play(Create(py_formula), run_time= 2.4)
        self.wait(1.)
        self.play(*[FadeOut(mob)for mob in self.mobjects])
        self.wait()
        