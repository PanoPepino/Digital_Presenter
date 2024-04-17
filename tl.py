from manim import *
from collections.abc import Iterable
def play_timeline(scene, timeline):
    previous_t = 0
    ending_time = 0
    for t, anims in sorted(timeline.items()):
        to_wait = t - previous_t
        if to_wait > 0:
            scene.wait(to_wait)
        previous_t = t
        if not isinstance(anims, Iterable):
            anims = [anims]
        for anim in anims:
            turn_animation_into_updater(anim)
            scene.add(anim.mobject)
            ending_time = max(ending_time, t + anim.run_time)
    if ending_time > t:
        scene.wait(ending_time - t)