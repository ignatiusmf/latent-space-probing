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



########################################################################################################################################
###################################################### ROUND 2 #########################################################################
########################################################################################################################################
# from manim import *
# import numpy as np
# from manim.mobject.three_d.three_dimensions import Arrow3D

# class Vectors(ThreeDScene):
#   def construct(self):
#     # Stel eers ide axes klere 
#     axes = ThreeDAxes()
#     axes.x_axis.set_color(RED)
#     axes.y_axis.set_color(BLUE)
#     axes.z_axis.set_color(GREEN)
#     self.add(axes)

#     plane = NumberPlane().set_opacity(0.2)
#     self.add(plane)

#     np.random.seed(1)
#     N, n = 10, 3
#     X = np.random.randn(N, n)
#     Xc = X - X.mean(0, keepdims=True)
    


#     vectors = []
#     for v in Xc:
#       # vec = Arrow3D(start=ORIGIN, end=v, color=BLUE, thickness=0.01, base_radius=0.05, resolution=4)
#       vec = Vector(v, color=BLUE)
#       vectors.append(vec)
#     self.add(*vectors)
  

#     A, B, C = np.linalg.svd(Xc, full_matrices=False)
#     k = 2

#     Xp = Xc @ C # N,n
#     Xr = Xp[:, :k] @ C[:, :k].T # Reconstructed with k factors 

#     p1 = C[0]
#     p2 = C[1]
#     self.add(Vector(p1, color=PURPLE))
#     self.add(Vector(p2, color=PURPLE))

#     plane = Surface(
#         lambda u, v: u * p1 + v * p2,
#         u_range=(-5, 5),
#         v_range=(-5, 5),
#         resolution=(5, 5),
#         fill_opacity=0.1,
#         # fill_color=BLUE_D,
#         stroke_color=LIGHT_GREY,
#     )
#     self.add(plane)


#     normal = np.cross(p1, p2)
#     normal = normal / np.linalg.norm(normal)

#     nx, ny, nz = normal
#     theta = np.arctan2(ny, nx)           # rotation around z-axis
#     phi   = np.arccos(nz)   


#     self.move_camera(phi=phi, theta=theta, run_time=2)
#     self.wait(2)






########################################################################################################################################
###################################################### ROUND 3 #########################################################################
########################################################################################################################################

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


#     # THE MATH
#     np.random.seed(0)
#     N, n = 4, 3
#     X = np.random.randn(N, n) * 2
#     Xc = X - X.mean(0, keepdims=True)
#     A, B, C = np.linalg.svd(Xc, full_matrices=False)

#     k = 3
#     Xp = Xc @ C.T
#     Xr = Xp[:, :k] @ C[:k, :]



#     colors = [LOGO_RED, LOGO_BLUE, LOGO_GREEN]
#     pcs = []
#     for i, pc in enumerate(C):
#       color = colors[i % len(colors)]
#       vec = Arrow3D(start=ORIGIN, end=pc, thickness=0.05, base_radius=0.05, color=color)
#       pcs.append(vec)
#     self.add(*pcs)


#     vectors = []
#     vec_labels = []
#     for i, v in enumerate(Xc):
#       # vec = Arrow3D(start=ORIGIN, end=v,color=BLUE, base_radius=0.05, thickness=0.01)
#       vec = Vector(v, color=BLUE)

#       label = Text(str(i), font_size=24, color=BLUE)
#       label.move_to(vec.get_end() + 0.1 * normalize(v))

#       vec_labels.append(label)
#       vectors.append(vec)
#     self.add(*vectors, *vec_labels)



#     pvecs = []
#     pvecs_labels = []
#     for i in range(N):
#       # vec = Arrow3D(start=ORIGIN, end=[pv.item(), 0, 0], thickness=0.01, base_radius=0.05, color=GREEN)

#       pv = [Xp[i, :k].item(),0,0] if k == 1 else [Xp[i,:k][0].item(), Xp[i,:k][1].item(), 0] if k == 2 else Xp[i, :k]
#       vec = Vector(pv, color=GREEN)
        

#       label = Text(str(i), font_size=24, color=GREEN)
#       label.move_to(vec.get_end() + 0.1 * normalize(pv))

#       pvecs.append(vec)
#       pvecs_labels.append(label)
#     self.add(*pvecs, *pvecs_labels)


#     rvecs = []
#     rvecs_labels = []
#     for i, rv in enumerate(Xr):
#       # vec = Arrow3D(start=ORIGIN, end=rv, thickness=0.01, base_radius=0.05, color=RED)
#       vec = Vector(rv, color=RED)

#       label = Text(str(i), font_size=24, color=RED)
#       label.move_to(vec.get_end() + 0.1 * normalize(rv))

#       rvecs.append(vec)
#       rvecs_labels.append(label)
#     self.add(*rvecs, *rvecs_labels)


#     self.wait(0.5)
#     def custom_mover(p1, p2):
#       def custom_mover2(p1, p2):
#         normal = np.cross(p1, p2)
#         normal = normal / np.linalg.norm(normal)
#         nx, ny, nz = normal
#         theta = np.arctan2(ny, nx)
#         phi = np.arccos(nz)
#         self.move_camera(phi=phi, theta=theta, run_time=1)
#       custom_mover2(p1, p2)
#       custom_mover2(p2, p1)
#       self.wait(0.5)

#     custom_mover(C[0], C[1])
#     custom_mover(C[1], C[2])
#     custom_mover(C[2], C[0])

#     self.wait(1)
#     # self.play(*[FadeOut(vec) for vec in vectors], run_time=1)



########################################################################################################################################
###################################################### ROUND 4 #########################################################################
########################################################################################################################################

import numpy as np
from manim import *
from manim.mobject.three_d.three_dimensions import Arrow3D


class Vectors(ThreeDScene):
  def construct(self):
    axes = ThreeDAxes()
    axes.x_axis.set_color(RED)
    axes.y_axis.set_color(BLUE)
    axes.z_axis.set_color(GREEN)
    self.add(axes)
    plane = NumberPlane().set_opacity(0.1)
    self.add(plane)

    # THE MATH 
    np.random.seed(0)
    N = 4
    n = 3
    X = np.random.randn(N, n)
    Xc = X - X.mean(0, keepdims=True)

    A, B, C = np.linalg.svd(Xc, full_matrices=False)

    k = 2
    Xp = Xc @ C[:k, :].T # (N, n) @ (k, n).T = (N, k)
    Xr = Xp @ C[:k, :] # (N, k) @ (k, n)


    colors = [PURE_RED, PURE_BLUE, PURE_GREEN]
    pcs = []
    for i, pc in enumerate(C):
      color = colors[i]
      vec = Arrow3D(start=ORIGIN, end=pc * B[i], thickness=0.05, base_radius=0.05, color=color)
      pcs.append(vec)
    self.add(*pcs)



    vectors = []
    for i in range(N):
      vec = Vector(Xc[i], color=BLUE)
      vectors.append(vec)
    self.add(*vectors)



    # pxs = []
    # for i, px in enumerate(Xp):
    #   temp = [px.item(), 0, 0]
    #   vec = Vector(temp, color=GREEN)
    #   pxs.append(vec)
    # self.add(*pxs)


    rxs = []
    for rx in Xr:
      vec = Vector(rx, color=RED)
      rxs.append(vec)
    self.add(*rxs)





    def custom_mover(v1, v2):
      def move_camera(v1, v2): 
        normal = np.cross(v1, v2)
        normal = normal / np.linalg.norm(normal)
        nx, ny, nz = normal
        theta = np.arctan2(ny, nx)
        phi = np.arccos(nz)
        self.move_camera(phi=phi, theta=theta, run_time=1)

      move_camera(v1, v2)
      move_camera(v2, v1)
      self.wait(1)

    custom_mover(C[0], C[1])
    custom_mover(C[1], C[2])
    custom_mover(C[2], C[0])


      

  













