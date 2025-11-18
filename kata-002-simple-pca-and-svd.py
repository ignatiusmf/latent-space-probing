import torch
import numpy as np
from matplotlib import pyplot as plt


from manim import *


class Vectors(ThreeDScene):
  def construct(self):
    axes = ThreeDAxes()

    axes.x_axis.set_color(RED)
    axes.y_axis.set_color(GREEN)
    axes.z_axis.set_color(BLUE)

    self.add(axes)

    plane = NumberPlane().set_opacity(0.1)
    self.add(plane)

    # NOROMAL NUMPY
    np.random.seed(1)
    N = 10
    n = 3
    X = np.random.randn(N,n)
    Xc = X - X.mean(0, keepdims=True)

    vectors = []
    for i, v in enumerate(Xc):
      vectors.append(Vector(v))
    
    self.add(*vectors)

    self.wait(2)

    self.move_camera(phi=45 * DEGREES, run_time=1)
    self.move_camera(theta=270 * DEGREES, run_time=4)




