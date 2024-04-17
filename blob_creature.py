from manim import *
from obj_eyes import *


class Blob_Creature(Eyes, VMobject):
    # DO NOT FORGET TO CHANGE LOCATION OF SVG'S TO ANIMATE!
    """
    This class creates a creature. It inherites properties from VMobject and Eyes. To place the eyes, there is an anchor point called frown. The creature main features are: The eyes and two hands used to point to things. The hands and the body are svg objects.
    It also eats arguments from the Eyes class: These are:
    
    - eye_color = The color of the eye_lid. By default, BLACK.
    - pupillary_vector = A vector that indicates the distance between the pupils of the eyes.
    - eye_size: Size of the eyes after separation with pupillary_vector. By default is 0.25.
    """
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
         
        #body (BE AWARE OF CHANGING POSITIIONS AND SCALINGS!)
        self.body = SVGMobject("blob_pieces/blob_body.svg").scale(0.5).set_z_index(-5)
        self.l_shoulder = Dot(color = WHITE, fill_opacity  = 0).move_to(self.body.get_left()+0.1*LEFT).set_z_index(-5) # Set fill_opacity to 1 to see location.
        self.r_shoulder = Dot(color = WHITE, fill_opacity  = 0).move_to(self.body.get_right()+0.1*RIGHT).set_z_index(-5)
        self.frown = Dot(color = BLACK, fill_opacity= 0).move_to(self.body.get_center()+0.5*UP).set_z_index(-10)
        self.l_hand = SVGMobject("blob_pieces/blob_hand.svg").scale(0.2).next_to(self.l_shoulder.get_center(), LEFT, buff =0.1).set_z_index(-8)
        self.r_hand = self.l_hand.copy().flip().next_to(self.r_shoulder.get_center(), RIGHT, buff =0.1).set_z_index(-8)
        self.oculii.move_to(self.frown.get_center()) # The eyes. Place the body behind the eyes with z_index. Do not modify the oculii.z_index here. Do it in obj_eyes 

        self.add(self.oculii, self.body, self.l_shoulder,  self.r_shoulder, self.l_hand, self.r_hand, self.frown)
        self.go_live() # self function to make dark energy pulsating bandana go on. Eyes are alive by default.
        
    def go_live(self):
        """
        This function makes the creature alive. It uses its own timer to make the blinking and the pulsating light of the bandana independent of the duration of the animation. Its main feature is the counter "time" that increments independently and it is used in the following functions.
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
        """
        To animate the pulsating light of the body. Issue with the basic actions, to be solved.
        """
        #self.l_hand.set_opacity(1-0.6*np.cos(time)**2)
        #self.r_hand.set_opacity(1-0.6*np.cos(time)**2)
        #self.body.set_opacity(1-0.6*np.cos(time)**2)
    
        
    



