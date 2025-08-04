import numpy as np
import logging

from src.CTPv.ICP.ICP_wx import *

from src.CTPv.ICP.ICP import ICPAligner
from src.CTPv.Transformation.TransformationMatrix import TransformationMatrix

if __name__ == '__main__':

    # --- Main Execution Block ---

    # On Windows, address potential DPI scaling issues, especially in debug mode.
    # The debugger can sometimes set DPI awareness, causing a conflict.
    # This tries to set it, but safely ignores the "Access is denied" error if it's already set.



    # --- Main Execution Block ---


    # Replace these with your actual classes

    # Setup basic logging
    logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')
    logger = logging.getLogger()

    ## 2. Load Data
    file_path = '../src/CTPv/ICP/0.ply'
    target_points = ICPAligner.load_ply(file_path)

    if target_points is not None:
        logger.info(f"✅ Successfully loaded '{file_path}' with {len(target_points)} points.")

        ## 3. Prepare Source Point Cloud
        T = TransformationMatrix()
        T.units = 'mm'
        T.angles_degree = [0, 0, 0]
        T.T = [0, 0, 200]
        source_points = T.transform(target_points)
        Hx = T.calculate_rigid_transform(source_points,target_points)

        print(Hx)
        ## 4. Initialize and run the application
        app = wx.App(False)
        frame = MainFrame(target_points=target_points, source_points=source_points, num_points_to_select=4)
        app.MainLoop()

        # 5. Access selected points after closing
        if hasattr(frame, 'result_target_points'):
            print("\nFinal Results Available:")
            print(f"Target points: {frame.result_target_points.shape}")
            print(f"Source points: {frame.result_source_points.shape}")

        #6. ICP
        H = T.calculate_rigid_transform(frame.result_source_points,frame.result_target_points)
        source_points2 = H.transform(source_points)
        aligner = ICPAligner(source_points2, target_points)
        H2 = aligner.align(threshold=10, max_iteration=3000, manual_pre_alignment=False)
        H3 =  H2 @ H # combine the two transformations
        #plot with open3d source_points2 and target_points
        source_points2 = H3.transform(source_points)

        plot_open3d(target_points, source_points2)


        print(H)
    else:
        logger.error(f"Failed to load point cloud from {file_path}. Exiting.")