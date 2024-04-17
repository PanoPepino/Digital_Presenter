from manim import *
from blob_creature import *
import csv
from ani_type import *
from tl import *


class Demo(Scene):
        def construct(self):
                actions = []
                dialogue = []
                with open('script.csv') as f:  #Careful adding empty lines of script at the end of the .csv file.
                    script = csv.reader(f, delimiter='/')
                    for row in script:
                        new_row = row[0].replace('mobj_', '').replace('dir_','')
                        if new_row == row[0]:
                                actions.append(new_row)
                        else:
                                actions.append(eval(new_row))
                                print(new_row)
                        row[1]= row[1].replace(r"\n", "\n")
                        dialogue.append(row[1])
                            
                texts = VGroup(*[Text(line) for line in dialogue]).scale_to_fit_width(config["frame_width"]-0.8).to_corner(DOWN)
                bc = Blob_Creature(pupillary_vector = [1.3,0,0], eye_color = GREEN_E).scale(2)

                bc_script = load_script(bc, texts, actions)
                self.play(FadeIn(bc))
                for action in actions:
                    self.play(next(bc_script))
                    self.wait(3)
                self.play(FadeOut(bc))
                
                
 
                

                
                