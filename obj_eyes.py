from manim import *
import random 



class Eyes(VMobject):
    """
    This class generates a pair of eyes that has a blinking animation. The attributes it has:
    
    - eye_color = The color of the eye_lid. By default, black.
    - pupillary_vector = A vector that indicates the distance between the pupils of the eyes. If 0, you get a Cyclop!
    -eye_size: Size of the eyes after separation with pupillary_vector. By default is 0.25.
    """
    def __init__(self, eye_color = None, pupillary_vector = None, eye_size = None, **kwargs):
        super().__init__(**kwargs)
        
        self.opa = ValueTracker(1)
        self.eye_color = eye_color
        self.pupillary_vector = pupillary_vector 
        self.eye_size = eye_size
        
        if eye_color is None:
            eye_color = BLACK
        
        if pupillary_vector is None:
            pupillary_vector = [1,0,0]
        
        if eye_size is None:
            eye_size = 0.25

        #eyes
        eye= Circle(color = WHITE, fill_opacity = 1, stroke_color = eye_color, radius= 1)
        rimel= Circle(color = WHITE, fill_opacity = 0, stroke_color = eye_color, radius= 1).set_z_index(3)
        pupil = Circle(color = BLACK, fill_opacity = 1, radius = 0.4).move_to(eye.get_center())
        reflection = Circle(color = WHITE, stroke_color = WHITE,fill_opacity = 1, radius = 0.1).move_to(pupil.get_center()+ [0.1,0.1,0])
        half_eyelid_up = Arc(angle= PI, color = eye_color, fill_opacity = 0, stroke_color = eye_color, fill_color = eye_color).stretch_to_fit_height(0.7).move_to(eye.get_center()+0.6*UP).set(z_index = 4)
        half_eyelid_down = Arc(angle= -PI, color = eye_color, fill_opacity = 0, stroke_color = eye_color, fill_color = eye_color).stretch_to_fit_height(0.7).move_to(eye.get_center()-0.6*UP).set(z_index = 4)
        eyelid = Circle(color = eye_color, fill_opacity = 0, stroke_color = eye_color, radius = 1).move_to(eye.get_center()).set(z_index = 2) # for creature to blink!
        

        sight = VGroup(pupil, reflection) # for creature to look at things!
        whole_eye = VGroup(eye, rimel, eyelid, half_eyelid_up, half_eyelid_down, sight).scale(0.5)
        whole_eye_2 = whole_eye.copy().move_to(whole_eye.get_center()+pupillary_vector)

        
        self.oculii = always_redraw(lambda:
                 VGroup(whole_eye, whole_eye_2)).scale(eye_size)
        self.sight = always_redraw(lambda: VGroup(self.oculii[0][-1], self.oculii[1][-1]))
        self.add(self.oculii)
        self.to_blink() # self function to start the blinking of the eyes.

    def to_blink(self):
        """
        This function makes the eyes to blink. It uses its own timer to make the blinking. Its main feature is the counter "time" that increments independently and it is used in the following functions.
        """
        time = 0
        self.blinking = False
        dummy_element = VMobject()
        def living(mob, dt):
            nonlocal time
            time += dt
            self.blink(time)
        dummy_element.add_updater(living)
        self.add(dummy_element)
        
    def blink(self, time):
        """
        Conditional function. If a random number gets greater than some value, the creature will move its eyelid (i.e. will set opacity to them) Observe that has to be done to both eyelids separatly. Some issues with animation interaction.
        """
        if time < 0.2: # No blinking at the beginning of the scene
            return 
        window = time % 1
        if window < 0.2:
            if not self.blinking:
                if random.random() < 0.15:
                    self.oculii[0][2].set_opacity(1)
                    self.oculii[1][2].set_opacity(1)
                    self.blinking = True
        else:
            if self.blinking:
                self.oculii[0][2].set_opacity(0)
                self.oculii[1][2].set_opacity(0)
                self.blinking = False