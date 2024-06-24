from manim import *
from .ani_creature import * #Required to animate the creature within the load_script function

class FWC(FadeOut):
    """New class based on FadeOut. It now adds a beep sound when fading text. The idea is to simulate the sound when you press next in majority of RPG/ graphic adventure video games.

    """
    
    def __init__(self, *args, sound_to_play="sounds/beep.wav", **kwargs):
        super().__init__(*args, **kwargs)
        self.sound_to_play = sound_to_play
      

def load_script_tex(
    creature: VMobject, # Eats a creature, which is a mobject
    all_texts: list[VMobject], # Eats a script of text. This is a list with Text as entries
    all_actions: list,
    triangle_next_text: VMobject,
    animation_rc: float = there_and_back_with_pause,
    animation_rt: float = 4,                          
    fade_last=True, # fade out the last text
    **kwargs):
    r"""This function merges together a list of actions for the creature and a list of text to synchronise with the aforementioned actions. It has an inner counter called counter_script.  
    
    If the counter is at 0, this load_script_tex function will display the first entry of the text list inside the chosen box and the first animation for the creature in such list. It will also FadeIn a triangle simulating a "next text icon" in the chosen box. It will add +1 to the counter_script.
    
    If the counter_script is greater than 0, the function will erase the previous text and the triangle and write the next text at the same time it commands the creature the next action. 

    Args:
        - creature (VMobject): Creature to animation
        - all_texts (list[VMobject]): List of tex of what the creature will say.
        - triangle_next_text (VMobject): Triangle simulating next text in the box.
        - animation_rc: The desired rate_func for the animations. Defaults to there_and_back_with_pause.
        - animation_rt: The desired run_time for the creature animation. Defaults to 4 seconds. 
        
    """
    
    for iteration in range(len(all_texts) + bool(fade_last)): # counts number of entries + 1. I assume last one to erase final text.  
        if iteration < len(all_texts):
            type_de_script = [Create(all_texts[iteration], 
                            run_time = animation_rt), FadeIn(triangle_next_text, run_time = animation_rt), Animate_Creature(creature, all_actions[iteration], animation_rate_func= animation_rc, animation_run_time= animation_rt)]
        
        if iteration == 0:
            counter_script = type_de_script
            
        elif iteration < len(all_texts):
            counter_script= [FWC(all_texts[iteration-1], run_time = 0.08), FadeOut(triangle_next_text, run_time = 0.08), Create(all_texts[iteration], run_time = animation_rt), FadeIn(triangle_next_text, run_time = animation_rt), Animate_Creature(creature, all_actions[iteration], animation_rate_func= animation_rc, animation_run_time= animation_rt)]
            
        elif iteration == len(all_texts):
            counter_script = [FadeOut(triangle_next_text, run_time = 0.08), FWC(all_texts[iteration-1], run_time = 0.08)]
            
        else:
            counter_script = Wait(0.001)
            
        yield counter_script