import numpy as np
import copy
from src.core_toolbox.Camera.Intrinsics import IntrinsicMatrix
from src.core_toolbox.Transformation.TransformationMatrix import TransformationMatrix
from src.core_toolbox.Plucker.Line import intersection_between_2_lines

if __name__ == "__main__":
    I = IntrinsicMatrix()
    I.info = "testCamera"
    I.fx = 1770
    I.fy = 1770

    I.width = 1440
    I.height = 1080
    I.cx = 685
    I.cy = 492
    I.RadialDistortion.set_from_list([-0.5,0.18,0])

    I.save_intrinsics_to_json('test.json')
    rays = I.generate_rays()
    I2 = IntrinsicMatrix()
    I2.load_intrinsics_from_json('test.json')
    #rays.PlotLine()

    H = TransformationMatrix()
    H.T = [0,0,0]
    H.angles_degree = [45,0,0]
    rayst= copy.deepcopy(rays)
    rayst.TransformLines(H)
    #rayst.PlotLine()
    import time
    start = time.time()
    p,d = intersection_between_2_lines(rays,rayst)
    print("elapsed time: ", time.time()-start)

    ## standard deviation and mean of d
    print("mean: ", np.mean(d))
    print("std: ", np.std(d))



    print(I.PerspectiveAngle)
    I.PerspectiveAngle = np.deg2rad(60)
    print(I.MatlabIntrinsics)
    print(I.OpenCVIntrinsics)
    print(I.PerspectiveAngle)