from manim import *
from .obj_eyes import *

class Creature(Eyes, VMobject):
    r""" This class creates a creature. It inherites properties from VMobject and Eyes. To place the eyes, there is an anchor point called frown. To place the arms, there are anchor points called shoulders. The creature main features are: The eyes and two hands used to point to things. The hands and the body are svg objects. 
    
    It also eats parameters from the Eyes class. These are:
    
    Parameters (Attributes)
    ----------
     
    - eyelid_color_input = The color of the eye_lid. Defaults to BLACK. Observe that the body and hands will also default to this color.
    - eyeball_color = Defaults to WHITE.
    - pupil_color = Defaults to BLACK.
    - pupillary_vector = A vector that indicates the distance between the pupils of the eyes. Defaults to [1,0,0]. If 0, you get a Cyclop!
    - eye_size: Size of the eyes after separation with pupillary_vector. Defaults to 0.25.
    
    It has two main functions:
    
    Methods
    -------
    
    - pulse: Function to animate the glow (the opacity) of a piece of the body. It has a trigonometric time-dependence.
    - go_live: Similar to the blink function in the eyes class. It accounts for a time differential which increments.
    
    """
    
    # Do not forget to change the position of the .svg files. I cannot manage to place the .svg files inside the body folder. It seems they have to be place inside a folder at the level of the example file.
    
    # Note that if you change the shape of the different parts of the creature, you will have to change the position of each of them so that the creature has a sensible anatomy.
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Dot().set_default(color = WHITE, fill_opacity = 0) # Set fill opacity to see the joints of the creature.
         
        # Core (Note that the body color is a different tone, so the motion of the hands and eyes can be seen)
        self.body = SVGMobject("body_pieces/blob_body.svg").set_color(BLUE).scale(0.4).set_z_index(-5)
        self.glow = self.body.copy().scale(0.3).set(fill_opacity = 0.2, color = self.eyelid_color_input).next_to(self.body, DOWN, buff =0.1).set_z_index(2)
        
        # Shoulders and hands (set Dot(fill_opacity) to 1 to see the position of the shoulders)
        self.l_shoulder = Dot().move_to(self.body.get_left()+0.15*LEFT).set_z_index(-5)
        self.r_shoulder = Dot().move_to(self.body.get_right()+0.15*RIGHT).set_z_index(-5)
        self.l_hand = SVGMobject("body_pieces/blob_hand.svg").set_color(self.eyelid_color_input).scale(0.2).next_to(self.l_shoulder.get_center(), DOWN, buff =0).set_z_index(-8)
        self.r_hand = self.l_hand.copy().flip().next_to(self.r_shoulder.get_center(), DOWN, buff =0).set_z_index(-8)
        
        # Eyes and frown (set fill_opacity to 1 to see the position of the frown, i.e. where the eyes attach)
        self.frown = Dot().next_to(self.body.get_center(), UP, buff = 0.3).set_z_index(10)
        self.oculii.move_to(self.frown.get_center()) # The eyes. Place the body behind the eyes with z_index. Do not modify the oculii.z_index here. Do it in obj_eyes 

        self.add(self.oculii, self.body, self.l_shoulder,  self.r_shoulder, self.l_hand, self.r_hand, self.frown, self.glow)
        self.go_live() # self function to make the glowing part pulsate (i.e. change opacity with time-dependenceå)
        
    def go_live(self):
        r""" This function makes the creature alive. It uses its own timer to make the blinking and the pulsating light of the bandana independent of the duration of the animation. Its main feature is the counter "time" that increments independently and it is used in the following functions.
        """
        
        time = 0
        dummy_element = VMobject()
        def living(mob, dt):
            nonlocal time
            time += dt
            self.pulse(time)
        dummy_element.add_updater(living)
        self.add(dummy_element)

    def pulse(self, time):
        r""" To animate the glowing part of the creature. It just changes its opacity.
        """
        
        self.glow.set_opacity(1-0.6*np.cos(time)**2)
        # This can perhaps be improved to make the whole creature levitate (oscillate around a point depending on a time parameter or any other time dependence)
        
    
        
    



