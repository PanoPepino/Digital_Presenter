from manim import *

class Animate_Creature(AnimationGroup):
    """
    This is an animation class to animate the creature to present results. It eats the creature "object" and the input_action. The input_action can be a direction (array) or an object (Mobject). If it is a direction, it will look in that direction. If it is an Mobject, it will look and point to the Mobject, based on the position of the Mobject w.r.t. the creature.

    Parameters:
        - input_action: direction, object or expression, among:
            - none: pass
            - look_left(right): Move the eyes in that direction.
            - look_uleft(uright): Move the eyes to UL or UR.
            - point_left(right): Move the eyes and arm to LEFT or RIGHT.
            - point_uleft(uright): Move the eyes and arm to UL or UR.
            - suspicion: like Fry in futurama meme.
            - boredom: like Tony Stark meme.
            - susprise: both hands to mouth, and small eyes. 
            - explanation: both hand shoulder height.
            - thinking: eyes up and hand to mouth.
            - anger: suspicion eyes  color changes.

    """
    def __init__(self, object, input_action = None, **kwargs):
        self.input_action = input_action
        self.object = object
        tbp = there_and_back_with_pause
        rt = 4

        # ############## Useless piece ################
        # Due to the nature of the script for the videos, this is not possible. (Objects that classes beyond strings cannot be read from csv in an easy way. Hence all commands are strings.)
        if isinstance(self.input_action, np.ndarray) is True: # To look in a given direction
            super().__init__(
                    AnimationGroup(
                    object.sight.animate(rate_func= tbp).shift(0.05*self.input_action), suspend_updating= True), run_time =rt,
                    **kwargs)
            
        if isinstance(self.input_action, Mobject) is True: # Look at a given Mobject and point to it.
            if self.input_action.get_x() > object.get_x():
                if hasattr(object, 'r_shoulder') is True:
                    super().__init__(
                    LaggedStart(
                    object.sight.animate(rate_func= tbp).shift(0.05*UR),
                    object.r_hand.animate(rate_func= tbp).rotate(PI/3, about_point= object.r_shoulder.get_center(), axis = [0,0,1]),
                    lag_ratio=0.2), run_time= rt,
                    **kwargs)
                elif hasattr(object, 'r_shoulder') is False:
                    object.sight.animate(rate_func= tbp, run_time = rt).shift(0.05*UR)
                
            elif self.input_action.get_x() < object.get_x():
                super().__init__(
                LaggedStart(
                    object.sight.animate(rate_func= tbp).shift(0.05*UL),
                    object.l_hand.animate(rate_func= tbp).rotate(-2*PI/3, about_point= object.l_shoulder.get_center(), axis = [0,0,1]),
                    lag_ratio=0.2), run_time = rt,
                    **kwargs) 
        ############################### useful piece ########################################
        if isinstance(self.input_action,str) is True:
            if self.input_action == "none":
                super().__init__(
                    Wait(),
                    **kwargs)
            if self.input_action == "look_left":
                super().__init__(
                    AnimationGroup(
                    object.sight.animate(rate_func= tbp).shift(0.05*LEFT), suspend_updating= True), run_time =rt,
                    **kwargs)
            if self.input_action == "look_right":
                super().__init__(
                    AnimationGroup(
                    object.sight.animate(rate_func= tbp).shift(0.05*RIGHT), suspend_updating= True), run_time =rt,
                    **kwargs)
            if self.input_action == "look_uleft":
                super().__init__(
                    AnimationGroup(
                    object.sight.animate(rate_func= tbp).shift(0.05*UL), suspend_updating= True), run_time =rt,
                    **kwargs)
            if self.input_action == "look_uright":
                super().__init__(
                    AnimationGroup(
                    object.sight.animate(rate_func= tbp).shift(0.05*UR), suspend_updating= True), run_time =rt,
                    **kwargs)
            if self.input_action == "point_left":
                super().__init__(
                    LaggedStart(
                    object.sight.animate(rate_func= tbp).shift(0.05*LEFT),
                    object.l_hand.animate(rate_func= tbp).rotate(-PI/4, about_point= object.l_shoulder.get_center(), axis = [0,0,1]),
                    lag_ratio=0.2), run_time= rt,
                    **kwargs)
            if self.input_action == "point_right":
                super().__init__(
                    LaggedStart(
                    object.sight.animate(rate_func= tbp).shift(0.05*RIGHT),
                    object.r_hand.animate(rate_func= tbp).rotate(PI/4, about_point= object.r_shoulder.get_center(), axis = [0,0,1]),
                    lag_ratio=0.2), run_time= rt,
                    **kwargs)
            if self.input_action == "point_uleft":
                super().__init__(
                    LaggedStart(
                    object.sight.animate(rate_func= tbp).shift(0.05*UL),
                    object.l_hand.animate(rate_func= tbp).rotate(-PI/3, about_point= object.l_shoulder.get_center(), axis = [0,0,1]),
                    lag_ratio=0.2), run_time= rt,
                    **kwargs)
            if self.input_action == "point_uright":
                super().__init__(
                    LaggedStart(
                    object.sight.animate(rate_func= tbp).shift(0.05*UR),
                    object.r_hand.animate(rate_func= tbp).rotate(PI/3, about_point= object.r_shoulder.get_center(), axis = [0,0,1]),
                    lag_ratio=0.2), run_time= rt,
                    **kwargs)
            if self.input_action == "salute":
                super().__init__(
                    object.r_hand.animate(rate_func= tbp).rotate(PI/2, about_point= object.r_shoulder.get_center(), axis = [0,0,1]), run_time = rt, **kwargs)
            if self.input_action == "suspicion":
                super().__init__(
                    AnimationGroup(object.oculii[0][3:5].animate(rate_func= tbp).set_opacity(1),
                    object.oculii[1][3:5].animate(rate_func= tbp).set_opacity(1)), run_time = rt,
                    **kwargs)
            if self.input_action == "boredom":
                super().__init__(
                    AnimationGroup(object.oculii[0][3:4].animate(rate_func= tbp).set_opacity(1),
                    object.oculii[1][3:4].animate(rate_func= tbp).set_opacity(1),
                    object.sight.animate(rate_func= tbp).shift(0.07*UP)), run_time = rt,
                    **kwargs)
            if self.input_action == "surprise":
                super().__init__(
                    AnimationGroup(object.sight[0].animate(rate_func= tbp).scale(0.5),
                    object.sight[-1].animate(rate_func= tbp).scale(0.5),
                    object.r_hand.animate(rate_func= tbp).rotate(-2*PI/3, about_point= object.r_shoulder.get_center(), axis = [0,0,1]),
                    object.l_hand.animate(rate_func= tbp).rotate(2*PI/3, about_point= object.l_shoulder.get_center(), axis = [0,0,1])), run_time = rt,
                    **kwargs)
            if self.input_action == "explanation":
                super().__init__(
                    AnimationGroup(
                    object.r_hand.animate(rate_func= tbp).rotate(PI/3, about_point= object.r_shoulder.get_center(), axis = [0,0,1]),
                    object.l_hand.animate(rate_func= tbp).rotate(-PI/3, about_point= object.l_shoulder.get_center(), axis = [0,0,1])), run_time = rt,
                    **kwargs)
            if self.input_action == "thinking":
                super().__init__(
                AnimationGroup(
                    object.sight.animate(rate_func= tbp).shift(0.12*UP),
                    object.l_hand.animate(rate_func= tbp).rotate(2*PI/3, about_point= object.l_shoulder.get_center(), axis = [0,0,1])), run_time = rt,
                    **kwargs)
                
            if self.input_action == "anger":
                super().__init__(
                    LaggedStart(AnimationGroup(object.oculii[0][3:5].animate(rate_func= tbp, run_time = rt).set_opacity(1),
                    object.oculii[1][3:5].animate(rate_func= tbp, run_time = rt).set_opacity(1),
                    object.l_hand.animate(rate_func= tbp, run_time = rt).rotate(-PI/3, about_point= object.l_shoulder.get_center(), axis = [0,0,1]),
                    object.r_hand.animate(rate_func= tbp, run_time = rt).rotate(PI/3, about_point= object.r_shoulder.get_center(), axis = [0,0,1]),
                    self.object.body.animate(rate_func= tbp, run_time = rt).set_color(RED_E),
                    self.object.l_hand.animate(rate_func= tbp, run_time = rt).set_color(RED_E),
                    self.object.r_hand.animate(rate_func= tbp, run_time = rt).set_color(RED_E)),lag_ratio=0.2
                    ),
                    **kwargs)
            