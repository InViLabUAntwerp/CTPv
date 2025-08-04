import time
import logging

from src.CTPv.ICP.ICP import ICPAligner
from src.CTPv.Transformation.TransformationMatrix import TransformationMatrix

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
    target_points = ICPAligner.load_ply(file_path)

    if target_points is not None:
        logger.info(f"✅ Successfully loaded '{file_path}' with {len(target_points)} points.")

        ## 2. Prepare Source Point Cloud
        # Define a ground truth transformation to create a misaligned source cloud
        T = TransformationMatrix()
        T.units = 'mm'
        T.angles_degree = [0, 1, 0]
        T.T = [2, 2, 2]
        source_points = T.transform(target_points)

        ## 3. Perform Alignment
        # Initialize the aligner with source and target data
        start = time.time()
        aligner = ICPAligner(source_points, target_points)
        end = time.time()
        logger.info(f"Time taken for ICPAligner init: {end - start:.4f} seconds")
        logger.info(f"Initialization FPS: {1 / (end - start):.2f}")

        # Run ICP and print results
        H = aligner.align(threshold=10, max_iteration=3000, manual_pre_alignment=True)

        ## 4. Visualize the result
        aligner.visualize_after_alignment()
        aligner.print_results()