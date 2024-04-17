from manim import *
from ani_creature import *
from math import floor


class Type(Animation): # Abulafia Type animation. Thanks for creating this, boss!
        def __init__(self, textmo: Text, **kwargs) -> None:
                super().__init__(textmo, **kwargs)
                self.cursor = Text("|", font_size=textmo.font_size, font=textmo.font)
                self.mobject.add(self.cursor)
                self.mobject.set_opacity(0)
                     
                
        def interpolate_mobject(self, alpha: float) -> None:
                if alpha==0 or alpha==1: return
                self.blink = rate_functions.ease_out_circ(abs((alpha * self.run_time % 1.06)/0.53-1))
                char = floor(alpha * (len(self.mobject)-1))
                self.mobject[:char+1].set_opacity(1)
                self.cursor.set_opacity(self.blink).next_to(
                    self.mobject[char], RIGHT, buff=0)
                
        def clean_up_from_scene(self, scene: "Scene") -> None:
                self.cursor.set_opacity(0)
                super().clean_up_from_scene(scene) 
        
        



        
def load_script(creature: VMobject,     # Eats a creature, which is a mobject
           all_texts: list[VMobject],   # Eats a script of text. This is a list with Text as entries
           all_actions: list,          # List of actions. 
           cps=15,                      # characters to write per second
           lag_ratio=0.1,               # lag between fade and Type animations
           shift=0,                     # shifting the FadeOut
           fade_last=True,              # fade out the last text
           **kwargs):
    for iteration in range(len(all_texts) + bool(fade_last)): # counts number of entries + 1. I assume last one to erase final text.  
        if iteration < len(all_texts):
            type_de_script = AnimationGroup(Type(all_texts[iteration], 
                            run_time=len(all_texts[iteration])/cps), Animate_Creature(creature, all_actions[iteration]), lag_ratio= 0.1)
        fade_out_de_script = FadeOut(all_texts[iteration-1], run_time =0.08)
        if iteration == 0:
            counter_script = type_de_script
        elif iteration < len(all_texts):
            counter_script= LaggedStart(fade_out_de_script, type_de_script, 
                                lag_ratio=lag_ratio)
        elif iteration == len(all_texts):
            counter_script = fade_out_de_script
        else:
            counter_script = Wait(0.001)
        yield counter_script

