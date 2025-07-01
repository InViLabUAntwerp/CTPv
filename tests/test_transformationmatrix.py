from src.CTPv.Transformation.TransformationMatrix import TransformationMatrix
import matplotlib.pyplot as plt

# Example Usage
if __name__ == "__main__":
    T1 = TransformationMatrix()
    T1.T = [0,10,0]
    T1.angles_degree = [0, 30, 0]
    #T1.invert()
    T1.save_bundler_file("test.out")
    print("Transformation Matrix T1:\n", T1)
    print("\nTranslation:\n", T1.T)
    print("\nRotation:\n", T1.R)
    print("\nEuler Angles (degrees):\n", T1.angles_degree)
    print("\nQuaternion:\n", T1.quaternion)
    T1.plot()
    T1.save_to_json("test.json")
    T2 = TransformationMatrix()
    T2.load_from_json("test.json")


    T2 = TransformationMatrix()
    T2.T = [-1, -2, -3]
    T2.angles_degree = [-30, -45, -60]
    plt.ioff()

    T2 = T1.copy()


    T2.invert()
    T2.plot()
    T2.load_bundler_file("test.out")

    T_combined = T1 @ T2  # Chaining transformations

    print("\nCombined Transformation:\n", T_combined)