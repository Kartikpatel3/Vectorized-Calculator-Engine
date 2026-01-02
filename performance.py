import os
import time
import pandas as pd
import numpy as np
import ast
from operations import vectorized_py as vec_py
from operations import vectorized_np as vec_np
vec_np = vec_np()
vec_py = vec_py()
class performance_table:
    def Save_data(self,operation,size,Native_time,Numpy_time,Speedup):
        ''' Saves the performance data into a CSV file
        
        Parameters:
        operation (str): The mathematical operation performed
        size (int): The size of the arrays involved in the operation
        Native_time (float): Time taken by the native Python implementation
        Numpy_time (float): Time taken by the NumPy implementation
        Speedup (str): The speedup factor achieved by using NumPy
        Description:
        This method saves the performance metrics of mathematical operations
        into a CSV file named 'performance_report.csv'. If the file already
        exists, it appends a new row with the provided data. If the file does
        not exist, it creates a new CSV file with the provided data.
        '''
        data ={
                "Operations":[],
                "Size": [],
                "Naive Time":[],
                "NumPy Time":[],
                "Speedup": []
            }

        data["Operations"] = operation
        data["Size"] = size
        data["Naive Time"] = str(Native_time) + "s"
        data["NumPy Time"] = str(Numpy_time) + "s"
        data["Speedup"] = Speedup
        file_name = "performance_report.csv"
        if os.path.exists(file_name):
            df = pd.read_csv(file_name)
            df.loc[len(df)] = data 
        else:
            df = pd.DataFrame([data])
        df.to_csv(file_name, index=False)
        print(df.tail(1))
    def Add(self, first, second, user_dim):
        """
    Compares element-wise addition performance between pure Python
    and NumPy implementation and calculates speedup.

    Parameters:
    first (list): First input array (1D / 2D / 3D)
    second (list): Second input array (same shape as first)
    user_dim (str): Dimension of array ("1d", "2d", or "3d")

    Description:
    - Executes Python-based addition using vec_py.add_array().
    - Executes NumPy-based addition using vec_np.add_array().
    - Calculates execution time for both approaches.
    - Computes speedup factor (how many times NumPy is faster).
    - Stores results (operation, size, time, speedup) using Save_data().
    """
        Native_time = vec_py.add_array(first, second, user_dim)
        Numpy_time = vec_np.add_array(np.array(first), np.array(second))
        if isinstance(Native_time, (int, float)):
            arr = np.array(first)
            size = arr.size
            Speedup = round(Native_time / Numpy_time , 1)
            if Speedup < 1:
                Speedup = str(round(Numpy_time / Native_time , 0)) + "x"
            else:
                Speedup = str(Speedup) + "x"
            operation = "Add"
            self.Save_data(operation,size,Native_time,Numpy_time,Speedup)
        else:
            print(Native_time)
    def Sub(self,first, second, user_dim):
        """
        Compares subtraction performance between pure Python loops
        and NumPy vectorized subtraction.

        Parameters:
        first (list): First input array
        second (list): Second input array
        user_dim (str): Dimension of array ("1d", "2d", or "3d")

        Description:
        - Measures execution time of Python subtraction.
        - Measures execution time of NumPy subtraction.
        - Calculates speedup ratio.
        - Saves benchmarking results using Save_data().
        """
        Native_time = vec_py.sub_array(first, second, user_dim)
        Numpy_time = vec_np.sub_array(np.array(first), np.array(second))
        if isinstance(Native_time, (int, float)):
            arr = np.array(first)
            size = arr.size
            Speedup = round(Native_time / Numpy_time , 0)
            if Speedup < 1:
                Speedup = str(round(Numpy_time / Native_time , 0)) + "x"
            else:
                Speedup = str(Speedup) + "x"
            operation = "Sub"
            self.Save_data(operation,size,Native_time,Numpy_time,Speedup)
        else:
            print(Native_time)
    def Dot(self, first, second, user_dim):
        """
        Compares dot product performance between Python implementation
        and NumPy optimized dot product.

        Parameters:
        first (list): First input array
        second (list): Second input array
        user_dim (str): Dimension of array ("1d", "2d", or "3d")

        Description:
        - Computes dot product using Python loops.
        - Computes dot product using np.dot().
        - Measures execution time for both.
        - Calculates speedup factor.
        - Stores benchmarking data.
        """
        Native_time = vec_py.dot_product(first, second, user_dim)
        Numpy_time = vec_np.dot_product(np.array(first), np.array(second))
        if isinstance(Native_time, (int, float)):
            arr = np.array(first)
            size = arr.size
            Speedup = round(Native_time / Numpy_time , 0)
            if Speedup < 1:
                Speedup = str(round(Numpy_time / Native_time , 0)) + "x"
            else:
                Speedup = str(Speedup) + "x"
            operation = "Dot Product"
            self.Save_data(operation,size,Native_time,Numpy_time,Speedup)
        else:
            print(Native_time)
    def Multi(self, first, second, user_dim):
        """
        Compares element-wise multiplication performance between
        Python loops and NumPy vectorization.

        Parameters:
        first (list): First input array
        second (list): Second input array
        user_dim (str): Dimension of array ("1d", "2d", or "3d")

        Description:
        - Measures execution time of Python multiplication.
        - Measures execution time of NumPy multiplication.
        - Calculates speedup factor.
        - Stores results using Save_data().
        """
        Native_time = vec_py.multiply_array(first, second, user_dim)
        Numpy_time = vec_np.multiply_array(np.array(first), np.array(second))
        if isinstance(Native_time, (int, float)):
            arr = np.array(first)
            size = arr.size
            Speedup = round(Native_time / Numpy_time , 0)
            if Speedup < 1:
                Speedup = str(round(Numpy_time / Native_time , 0)) + "x"
            else:
                Speedup = str(Speedup) + "x"
            operation = "Multiplication"
            self.Save_data(operation,size,Native_time,Numpy_time,Speedup)
        else:
            print(Native_time)
    def Divi(self, first, second, user_dim):
        """
        Compares element-wise division performance between
        pure Python implementation and NumPy vectorized division.

        Parameters:
        first (list): Numerator array
        second (list): Denominator array
        user_dim (str): Dimension of array ("1d", "2d", or "3d")

        Description:
        - Executes Python-based division.
        - Executes NumPy-based division.
        - Measures execution time.
        - Calculates speedup factor.
        - Saves benchmarking data for analysis.
        """
        Native_time = vec_py.div_array(first, second, user_dim)
        Numpy_time = vec_np.div_array(np.array(first), np.array(second))
        if isinstance(Native_time, (int, float)):
            arr = np.array(first)
            size = arr.size
            Speedup = round(Native_time / Numpy_time , 0)
            if Speedup < 1:
                Speedup = str(round(Numpy_time / Native_time , 0)) + "x"
            else:
                Speedup = str(Speedup) + "x"
            operation = "Division"
            self.Save_data(operation,size,Native_time,Numpy_time,Speedup)
        else:
            print(Native_time)
    def Mat_Mul(self, first, second, user_dim):
        """
        Compares matrix multiplication performance between
        pure Python implementation and NumPy's matmul function.

        Parameters:
        first (list): First input matrix
        second (list): Second input matrix

        Description:
        - Performs matrix multiplication using Python loops.
        - Performs matrix multiplication using np.matmul().
        - Measures execution time for both methods.
        - Calculates speedup factor.
        - Saves performance data for comparison.
        """
        Native_time = vec_py.matrix_multiply(first, second, user_dim)
        Numpy_time = vec_np.matrix_multiply(np.array(first), np.array(second))
        if isinstance(Native_time, (int, float)):
            arr = np.array(first)
            size = arr.size
            Speedup = round(Native_time / Numpy_time , 0)
            if Speedup < 1:
                Speedup = str(round(Numpy_time / Native_time , 0)) + "x"
            else:
                Speedup = str(Speedup) + "x"
            operation = "Matrix Multiplication"
            self.Save_data(operation,size,Native_time,Numpy_time,Speedup)
        else:
            print(Native_time)
    def Norm(self, array, ord_type):
        try:
            """
            Compares vector norm calculation performance between
            pure Python implementation and NumPy's norm function.

            Parameters:
            array (list): Input vector
            ord_type (int): Order of the norm (e.g., 1, 2, inf)

            Description:
            - Computes vector norm using Python loops.
            - Computes vector norm using np.linalg.norm().
            - Measures execution time for both methods.
            - Calculates speedup factor.
            - Saves performance data for analysis.
            """
            Native_time = vec_py.find_norm(array, ord_type)
            Numpy_time = vec_np.find_norm(np.array(array), ord_type)
            if isinstance(Native_time, (int, float)):
                arr = np.array(array)
                size = arr.size
                Speedup = round(Native_time / Numpy_time , 0)
                if Speedup < 1:
                    Speedup = str(round(Numpy_time / Native_time , 0)) + "x"
                else:
                    Speedup = str(Speedup) + "x"
                operation = "Vector Norm"
                self.Save_data(operation,size,Native_time,Numpy_time,Speedup)
            else:
                print(Native_time)
        except Exception as e:
            print("Error : ", e)
    def transpose(self, array, user_dim):
        """
        Compares matrix transpose performance between pure Python
        implementation and NumPy's transpose function.

        Parameters:
        array (list): Input matrix
        user_dim (str): Dimension of matrix ("2d" or "3d")

        Description:
        - Transposes matrix using Python loops.
        - Transposes matrix using np.transpose().
        - Measures execution time for both methods.
        - Calculates speedup factor.
        - Saves performance data for comparison.
        """
        Native_time = vec_py.transpose(array, user_dim)
        Numpy_time = vec_np.transpose(np.array(array))
        if isinstance(Native_time, (int, float)):
            arr = np.array(array)
            size = arr.size
            Speedup = round(Native_time / Numpy_time , 0)
            if Speedup < 1:
                Speedup = str(round(Numpy_time / Native_time , 0)) + "x"
            else:
                Speedup = str(Speedup) + "x"
            operation = "Transpose"
            self.Save_data(operation,size,Native_time,Numpy_time,Speedup)
        else:
            print(Native_time)