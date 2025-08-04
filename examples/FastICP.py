import time
import logging
import numpy as np
import open3d as o3d

from src.CTPv.Transformation.TransformationMatrix import TransformationMatrix
from src.CTPv.ICP.FastICP import FastICPAligner

# --- DEMONSTRATION ---
if __name__ == '__main__':
    # Configure basic logging for when the script is run directly
    logger = logging.getLogger(__name__)

    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)-15s - %(levelname)-8s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )

    ## 1. Load Data
    file_path = '../src/CTPv/ICP/0.ply'
    target_points = FastICPAligner.load_ply(file_path)

    if target_points is not None:
        print(f"✅ Successfully loaded '{file_path}' with {len(target_points)} points.")

        ## 2. Prepare Source Point Cloud
        T = TransformationMatrix()
        T.units = 'mm'
        T.angles_degree = [0, 1, 0]
        T.T = [2, 2, 2]
        source_points = T.transform(target_points)

        ## 3. Perform Alignment with the new FastICPAligner
        # Initialize the aligner
        start = time.time()
        fast_aligner = FastICPAligner(source_points, target_points)
        print(f"Time taken: FastICPAligner init: {time.time() - start:.4f} seconds")
        # Visualize before alignment
        fast_aligner.visualize_before_alignment()

        # Run the faster ICP and time it
        start_time = time.time()

        # --- Customize the alignment stages ---
        # You can define your own multi-scale pyramid here.
        # Each tuple is (downsample_ratio, max_iterations).
        # The last stage should always have a ratio of 1.0 to use the full point cloud.

        # Example: A faster 2-stage alignment
        # custom_scales = [(0.2, 50), (1.0, 20)]

        # Example: A more thorough 4-stage alignment
        #custom_scales = [(0.05, 50), (0.25, 10), (0.5, 2), (1.0, 2)]
        # Example: A faster 2-stage alignment
        custom_scales = [(0.05, 50), (1, 2)]
        H = fast_aligner.align(threshold=10, scales=custom_scales)
        end_time = time.time()

        print("--- Performance ---")
        print(f"Time taken for Fast ICP: {end_time - start_time:.4f} seconds")
        print(f"FPS: {1 / (end_time - start_time):.2f}")
        ## 4. Visualize the result
        fast_aligner.visualize_after_alignment()
        fast_aligner.print_results()
