# import numpy as np
# from manim import *
# from manim.mobject.three_d.three_dimensions import Arrow3D

# class Vectors(ThreeDScene):
#   def construct(self):
#     axes = ThreeDAxes()
#     axes.x_axis.set_color(RED)
#     axes.y_axis.set_color(GREEN)
#     axes.z_axis.set_color(BLUE)
#     self.add(axes)

#     plane = NumberPlane().set_opacity(0.1)
#     self.add(plane)

#     np.random.seed(1)
#     N, n = 10, 3
#     X = np.random.randn(N, n)
#     Xc = X - X.mean(0, keepdims=True)

#     vectors = []
#     for v in Xc:
#       vec = Arrow3D(
#         start=ORIGIN,
#         end=v,
#         color=BLUE,
#         thickness=0.01,
#         base_radius=0.05,
#         resolution=8,
#       )
#       vectors.append(vec)

#     self.add(*vectors)

#     self.wait(2)
#     self.move_camera(phi=45 * DEGREES, run_time=1)
#     self.move_camera(theta=270 * DEGREES, run_time=4)

from manim import *
import numpy as np
from manim.mobject.three_d.three_dimensions import Arrow3D

class Vectors(ThreeDScene):
  def construct(self):
    # Stel eers ide axes klere 
    axes = ThreeDAxes()
    axes.x_axis.set_color(RED)
    axes.y_axis.set_color(BLUE)
    axes.z_axis.set_color(GREEN)
    self.add(axes)

    plane = NumberPlane().set_opacity(0.2)
    self.add(plane)

    np.random.seed(1)
    N, n = 10, 3
    X = np.random.randn(N, n)
    Xc = X - X.mean(0, keepdims=True)
    


    vectors = []
    for v in Xc:
      vec = Arrow3D(start=ORIGIN, end=v, color=BLUE, thickness=0.01, base_radius=0.05, resolution=4)
      # vec = Vector(v, color=BLUE)
      vectors.append(vec)
    self.add(*vectors)
  

    A, B, C = np.linalg.svd(Xc, full_matrices=False)
    k = 2

    Xp = Xc @ C # N,n
    Xr = Xp[:, :k] @ C[:, :k].T # Reconstructed with k factors 

    p1 = C[0]
    p2 = C[1]
    self.add(Vector(p1, color=PURPLE))
    self.add(Vector(p2, color=PURPLE))

    plane = Surface(
        lambda u, v: u * p1 + v * p2,
        u_range=(-5, 5),
        v_range=(-5, 5),
        resolution=(5, 5),
        fill_opacity=0.1,
        # fill_color=BLUE_D,
        stroke_color=LIGHT_GREY,
    )
    self.add(plane)


    normal = np.cross(p1, p2)
    normal = normal / np.linalg.norm(normal)

    nx, ny, nz = normal
    theta = np.arctan2(ny, nx)           # rotation around z-axis
    phi   = np.arccos(nz)   


    self.move_camera(phi=phi, theta=theta, run_time=2)
    self.wait(2)




















