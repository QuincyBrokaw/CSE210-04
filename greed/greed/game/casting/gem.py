import os
from game.casting.artifact import Artifact
from game.casting.actor import Actor
import random

class Gem(Artifact):
    def __init__(self):
        super().__init__()
        self.frame_counter= 0
        self.artifacts =[]
        
    def gem_drop(self):
        self.frame_counter = self.frame_counter + 1
        if self. frame_counter>= 120:
            #reset frame counter back to 0
            self.frame_counter = 0 
            new_artifact= Artifact()
            new_artifact.position= (random.randint(0,1024), 768)
            self.artifacts.apend(new_artifact)
            for artifact in list(self.artifacts):
                artifact.position= (artifact.position.x, artifact.position.y -2)
                if artifact.position.y < -100:
                    self.artifacts.remove(artifact)
                if artifact.bbox.intersects(self.player.bbox):
                    self.artifacts.remove(artifact)