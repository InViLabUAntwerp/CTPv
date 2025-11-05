import numpy as np
import copy
from src.CTPv.Camera.Intrinsics import IntrinsicMatrix

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

    print(I.PerspectiveAngle)
    I.PerspectiveAngle = np.deg2rad(60)
    print(I.MatlabIntrinsics)
    print(I.OpenCVIntrinsics)
    print(I.PerspectiveAngle)
