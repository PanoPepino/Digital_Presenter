from manim import *
import random 



class Eyes(VMobject):
    r"""This class generates a pair of eyes that has a blinking animation and associated Animation ani_creature to make gesture. It has several parameters (that can be input) and two methods.
    
    Parameters (Attributes)
    ----------
     
    - eyelid_color_input = The color of the eye_lid. Defaults to BLACK.
    - eyeball_color = Defaults to WHITE.
    - pupil_color = Defaults to BLACK.
    - pupillary_vector = A vector that indicates the distance between the pupils of the eyes. Defaults to [1,0,0]. If 0, you get a Cyclop!
    - eye_size: Size of the eyes after separation with pupillary_vector. Defaults to 0.25.
    
    Methods
    -------
    
    - to_blink, which make the eyes blink given a timmer.
    - blink, which describes how the blink takes places (increasing or decreasing the opacity of the eyelid)
    """
    
    def __init__(self, 
                 eyelid_color_input: ParsableManimColor = BLACK,
                 eyeball_color_input: ParsableManimColor = WHITE,
                 pupil_color_input: ParsableManimColor = BLACK,
                 pupillary_vector: str = LEFT, # Eyes touching
                 eye_size: float = 0.2, 
                 **kwargs):
        super().__init__(**kwargs)
        
        self.eyelid_color_input = eyelid_color_input
        self.eyeball_color_input = eyeball_color_input
        self.pupil_color_input = pupil_color_input
        self.pupillary_vector = pupillary_vector 
        self.eye_size = eye_size
        
        #eyes
        eye= Circle(color = self.eyeball_color_input, fill_opacity = 1, stroke_color = self.eyelid_color_input, radius= 1)
        rimel= Circle(color = self.eyeball_color_input, fill_opacity = 0, stroke_color = self.eyelid_color_input, radius= 1).set_z_index(3)
        pupil = Circle(color = self.pupil_color_input, fill_opacity = 1, radius = 0.4).move_to(eye.get_center())
        reflection = Circle(color = WHITE, stroke_color = WHITE,fill_opacity = 1, radius = 0.1).move_to(pupil.get_center()+ [0.1,0.1,0])
        eyelid = Circle(color = self.eyelid_color_input, fill_opacity = 0, stroke_color = self.eyelid_color_input, radius = 1).move_to(eye.get_center()).set(z_index = 2) # for creature to blink!
        
        # This is extra, to make the creature close the eyes, but not completely, so it manages a suspicion or boredom look
        half_eyelid_up = Arc(angle= PI, color = self.eyelid_color_input, fill_opacity = 0, stroke_color = self.eyelid_color_input, fill_color = self.eyelid_color_input).stretch_to_fit_height(0.7).move_to(eye.get_center()+0.6*UP).set(z_index = 4)
        half_eyelid_down = Arc(angle= -PI, color = self.eyelid_color_input, fill_opacity = 0, stroke_color = self.eyelid_color_input, fill_color = self.eyelid_color_input).stretch_to_fit_height(0.7).move_to(eye.get_center()-0.6*UP).set(z_index = 4)
    
        sight = VGroup(pupil, reflection) # The composite VGroup for creature to look at things!
        whole_eye = VGroup(eye, rimel, eyelid, half_eyelid_up, half_eyelid_down, sight).scale(0.5)
        whole_eye_2 = whole_eye.copy().move_to(whole_eye.get_center()+pupillary_vector)

        self.oculii = always_redraw(lambda:
                 VGroup(whole_eye, whole_eye_2)).scale(eye_size)
        self.sight = always_redraw(lambda: VGroup(self.oculii[0][-1], self.oculii[1][-1]))
        self.add(self.oculii)
        self.to_blink() # self function to start the blinking of the eyes.

    def to_blink(self):
        r"""This function makes the eyes to blink. It uses its own timer to make the blinking. Its main feature is the counter "time" that increments independently and it is used in the following functions.
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
        """Conditional function. If a random number gets greater than some value, the creature will move its eyelid (i.e. will set opacity to them) Observe that has to be done to both eyelids separatly. Some issues with animation interaction.
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