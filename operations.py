import time
import numpy as np
import pandas as pd
import os

class vectorized_py:
    def save_Native_output(self,first,second,native_result):
        ''' This Functon is free'''
        data = {
            "First_Array": str(first),
            "Second_Array": str(second),
            "Native_Output": str(native_result),
            "Numpy_Output": ""
        }
        if os.path.exists("result_report.csv"):
            df = pd.read_csv("result_report.csv", dtype=str)
            df.loc[len(df)] = data
        else:
            df = pd.DataFrame([data], dtype=str)
        df.to_csv("result_report.csv", index=False)
    def add_array(self, first, second, user_dim):
        '''
        Function Name: add_array

            Description:
            The add_array function performs element-wise addition of two arrays and measures
            the execution time of the operation using time.perf_counter(). It supports 1D, 2D,
            and 3D arrays based on the user-defined dimension input.

            Parameters:
            first      : First input array (1D / 2D / 3D list)
            second     : Second input array (must have the same shape as first)
            user_dim   : Dimension of the array ("1d", "2d", or "3d")

            Working:
            - The function checks the array dimension provided by the user.
            - It records the start time before computation.
            - Element-wise addition is performed using nested loops.
            - The end time is recorded after computation.
            - The total execution time (in seconds) is returned.

            Return Value:
            - Float value representing execution time in seconds.
            - Error message if dimension is invalid or array shapes do not match.

            Exception Handling:
            - Handles TypeError when array dimensions or data types are incorrect.

            Use Case:
            - Useful for performance testing and comparison of array operations
            (e.g., Python loops vs NumPy).

        '''
        try:
            if user_dim == "2d":
                start = time.perf_counter()
                result = []
                for a,b in zip(first , second):
                    row_sum = []
                    for i,e in zip(a,b):
                        row_sum.append(i + e)
                    result.append(row_sum)
                end = time.perf_counter()
                self.save_Native_output(first, second, result)
                return end - start
            elif user_dim == "1d":
                start = time.perf_counter()
                result = []
                for i,e in zip(first , second):
                    result.append(i + e)
                end = time.perf_counter()
                self.save_Native_output(first, second, result)
                return end - start
            elif user_dim == "3d":
                start = time.perf_counter()
                result = []
                for a,b in zip(first , second):
                    sum = []
                    for c,d in zip(a,b):
                        row_sum = []
                        for i,e in zip(c,d):
                            row_sum.append(i + e)
                        sum.append(row_sum)
                    result.append(sum)
                end = time.perf_counter()
                self.save_Native_output(first, second, result)
                return end - start
            else:
                return "Please Enter Correct Dimentions of array(Like : 1d,2d,3d). THANKYOU"
        except Exception as e:
            return f"Error : {e}"
    def sub_array(self, first, second, user_dim):
        '''
        Function Name: sub_array

        Description:
            The add_array function performs element-wise substraction of two arrays and measures
            the execution time of the operation using time.perf_counter(). It supports 1D, 2D,
            and 3D arrays based on the user-defined dimension input.

            Parameters:
            first      : First input array (1D / 2D / 3D list)
            second     : Second input array (must have the same shape as first)
            user_dim   : Dimension of the array ("1d", "2d", or "3d")

            Working:
            - The function checks the array dimension provided by the user.
            - It records the start time before computation.
            - Element-wise substrsction is performed using nested loops.
            - The end time is recorded after computation.
            - The total execution time (in seconds) is returned.

            Return Value:
            - Float value representing execution time in seconds.
            - Error message if dimension is invalid or array shapes do not match.

            Exception Handling:
            - Handles TypeError when array dimensions or data types are incorrect.

            Use Case:
            - Useful for performance testing and comparison of array operations
            (e.g., Python loops vs NumPy).
        '''
        try:
            if user_dim == "2d":
                start = time.perf_counter()
                result = []
                for a,b in zip(first , second):
                    row_sum = []
                    for i,e in zip(a,b):
                        row_sum.append(i - e)
                    result.append(row_sum)
                end = time.perf_counter()
                self.save_Native_output(first, second, result)
                return end - start
            elif user_dim == "1d":
                start = time.perf_counter()
                result = []
                for i,e in zip(first , second):
                    result.append(i - e)
                end = time.perf_counter()
                self.save_Native_output(first, second, result)
                return end - start
            elif user_dim == "3d":
                start = time.perf_counter()
                result = []
                for a,b in zip(first , second):
                    sum = []
                    for c,d in zip(a,b):
                        row_sum = []
                        for i,e in zip(c,d):
                            row_sum.append(i - e)
                        sum.append(row_sum)
                    result.append(sum)
                end = time.perf_counter()
                self.save_Native_output(first, second, result)
                return end - start
        except Exception as e:
            return f"Error : {e}"
    def dot_product(self, first, second, user_dim):
        '''
            Calculates the dot product of two arrays based on the given dimension
            and measures the execution time using time.perf_counter().

            Parameters:
            first (list): First input array (1D / 2D / 3D)
            second (list): Second input array (compatible shape required)
            user_dim (str): Dimension of array ("1d", "2d", or "3d")

            Returns:
            float: Execution time in seconds

            Description:
            - For 1D arrays, computes scalar dot product.
            - For 2D arrays, performs matrix multiplication logic using nested loops.
            - For 3D arrays, performs dot product across matrices.
            - Used for performance comparison with NumPy dot product.
        '''
        try:
            if user_dim == "1d":
                start = time.perf_counter()
                result = 0
                for i,e in zip(first, second):
                    result += i * e
                    end = time.perf_counter()
                self.save_Native_output(first, second, result)
                return end - start
            elif user_dim == "2d":
                start = time.perf_counter()
                result = []
                for a in first:
                    row_result = []
                    for j in range(len(second[0])):
                        sum_product = 0
                        for i,e in zip(a, [row[j] for row in second]):
                            sum_product += i * e
                        row_result.append(sum_product)
                    result.append(row_result)
                    end = time.perf_counter()
                self.save_Native_output(first, second, result)
                return end - start
            elif user_dim == "3d":
                start = time.perf_counter()
                result = []
                for a in first:
                    matrix_result = []
                    for b in second:
                        row_result = []
                        for j in range(len(b[0])):
                            sum_product = 0
                            for i,e in zip(a[0], [row[j] for row in b]):
                                sum_product += i * e
                            row_result.append(sum_product)
                        matrix_result.append(row_result)
                    result.append(matrix_result)
                end = time.perf_counter()
                self.save_Native_output(first, second, result)
                return end - start
        except Exception as e:
            return f"Error : {e}"
    def multiply_array(self, first, second, user_dim):
        """
        Performs element-wise multiplication of two arrays and measures
        execution time using time.perf_counter().

        Parameters:
        first (list): First input array (1D / 2D / 3D)
        second (list): Second input array (same shape as first)
        user_dim (str): Dimension of array ("1d", "2d", or "3d")

        Returns:
        float: Execution time in seconds

        Description:
        - Multiplies corresponding elements of both arrays.
        - Supports 1D, 2D, and 3D arrays.
        - Useful for benchmarking Python loops vs NumPy vectorization.
        """
        try:
            if user_dim == "2d":
                start = time.perf_counter()
                result = []
                for a,b in zip(first , second):
                    row_product = []
                    for i,e in zip(a,b):
                        row_product.append(i * e)
                    result.append(row_product)
                end = time.perf_counter()
                self.save_Native_output(first, second, result)
                return end - start
            elif user_dim == "1d":
                start = time.perf_counter()
                result = []
                for i,e in zip(first , second):
                    result.append(i * e)
                end = time.perf_counter()
                self.save_Native_output(first, second, result)
                return end - start
            elif user_dim == "3d":
                start = time.perf_counter()
                result = []
                for a,b in zip(first , second):
                    product = []
                    for c,d in zip(a,b):
                        row_product = []
                        for i,e in zip(c,d):
                            row_product.append(i * e)
                        product.append(row_product)
                    result.append(product)
                end = time.perf_counter()
                self.save_Native_output(first, second, result)
                return end - start
        except Exception as e:
            return f"Error : {e}"
    def div_array(self, first, second, user_dim):
        """
        Performs element-wise division of two arrays and measures
        execution time using time.perf_counter().

        Parameters:
        first (list): Numerator array (1D / 2D / 3D)
        second (list): Denominator array (same shape as first)
        user_dim (str): Dimension of array ("1d", "2d", or "3d")

        Returns:
        float: Execution time in seconds

        Description:
        - Divides each element of first array by corresponding element of second.
        - Supports nested arrays up to 3D.
        - Used to analyze performance of division operations in pure Python.
        """
        try:
            if user_dim == "2d":
                start = time.perf_counter()
                result = []
                for a,b in zip(first , second):
                    row_div = []
                    for i,e in zip(a,b):
                        row_div.append(i / e)
                    result.append(row_div)
                end = time.perf_counter()
                self.save_Native_output(first, second, result)
                return end - start
            elif user_dim == "1d":
                start = time.perf_counter()
                result = []
                for i,e in zip(first , second):
                    result.append(i / e)
                end = time.perf_counter()
                self.save_Native_output(first, second, result)
                return end - start
            elif user_dim == "3d":
                start = time.perf_counter()
                result = []
                for a,b in zip(first , second):
                    div = []
                    for c,d in zip(a,b):
                        row_div = []
                        for i,e in zip(c,d):
                            row_div.append(i / e)
                        div.append(row_div)
                    result.append(div)
                end = time.perf_counter()
                self.save_Native_output(first, second, result)
                return end - start
        except Exception as e:
            return f"Error : {e}"
    def matrix_multiply(self, first, second, user_dim):
        '''
            Performs matrix multiplication of two arrays based on the given dimension
            and measures the execution time using time.perf_counter().

            Parameters:
            first (list): First input array (2D / 3D)
            second (list): Second input array (compatible shape required)
            user_dim (str): Dimension of array ("2d", or "3d")

            Returns:
            float: Execution time in seconds

            Description:
            - For 2D arrays, performs standard matrix multiplication using nested loops.
            - For 3D arrays, performs matrix multiplication across matrices.
            - Used for performance comparison with NumPy matrix multiplication.
        '''
        try:
            if user_dim == "2d":
                start = time.perf_counter()
                result = []
                for a in first:
                    row_result = []
                    for j in range(len(second[0])):
                        sum_product = 0
                        for i,e in zip(a, [row[j] for row in second]):
                            sum_product += i * e
                        row_result.append(sum_product)
                    result.append(row_result)
                end = time.perf_counter()
                self.save_Native_output(first, second, result)
                return end - start
            elif user_dim == "3d":
                start = time.perf_counter()
                result = []
                for a in first:
                    matrix_result = []
                    for b in second:
                        row_result = []
                        for j in range(len(b[0])):
                            sum_product = 0
                            for i,e in zip(a[0], [row[j] for row in b]):
                                sum_product += i * e
                            row_result.append(sum_product)
                        matrix_result.append(row_result)
                    result.append(matrix_result)
                end = time.perf_counter()
                self.save_Native_output(first, second, result)
                return end - start
        except Exception as e:
            return f"Error : {e}"
    def find_norm(array, ord_type):
        """
        Calculates the norm of an array using pure Python implementation
        and measures execution time.

        Parameters:
        array (list): Input array (1D / 2D / 3D)
        ord_type (int or str): Order of the norm (e.g., 1, 2, 'fro', etc.)

        Returns:
        float: Execution time in seconds

        Description:
        - Computes various norms based on ord_type.
        - Supports 1D, 2D, and 3D arrays.
        - Useful for performance comparison with NumPy norm calculations.
        """
        try:
            start = time.perf_counter()
            if ord_type == "1":
                if isinstance(array[0], list):  # 2D or 3D
                    total = 0
                    for row in array:
                        for elem in row:
                            if isinstance(elem, list):  # 3D
                                for sub_elem in elem:
                                    total += abs(sub_elem)
                            else:
                                total += abs(elem)
                    result = total
                else:  # 1D
                    result = sum(abs(i) for i in array)
            elif ord_type == "2":
                if isinstance(array[0], list):  # 2D or 3D
                    total = 0
                    for row in array:
                        for elem in row:
                            if isinstance(elem, list):  # 3D
                                for sub_elem in elem:
                                    total += sub_elem ** 2
                            else:
                                total += elem ** 2
                    result = total ** 0.5
                else:  # 1D
                    result = sum(i ** 2 for i in array) ** 0.5
            else:
                return "Please Enter ord (1 or 2)."
            end = time.perf_counter()
            return end - start
        except Exception as e:
            return f"Error : {e}"
    def transpose(array, user_dim):
        '''
            Transposes the given array based on its dimension
            and measures execution time using time.perf_counter().

            Parameters:
            array (list): Input array (2D / 3D)
            user_dim (str): Dimension of array ("2d", or "3d")

            Returns:
            float: Execution time in seconds

            Description:
            - For 2D arrays, swaps rows and columns.
            - For 3D arrays, transposes each matrix within the 3D structure.
            - Used for performance comparison with NumPy transpose.
        '''
        try:
            if user_dim == "2d":
                start = time.perf_counter()
                result = []
                for j in range(len(array[0])):
                    row = []
                    for i in range(len(array)):
                        row.append(array[i][j])
                    result.append(row)
                end = time.perf_counter()
                return end - start
            elif user_dim == "3d":
                start = time.perf_counter()
                result = []
                for matrix in array:
                    transposed_matrix = []
                    for j in range(len(matrix[0])):
                        row = []
                        for i in range(len(matrix)):
                            row.append(matrix[i][j])
                        transposed_matrix.append(row)
                    result.append(transposed_matrix)
                end = time.perf_counter()
                return end - start
        except Exception as e:
            return f"Error : {e}"
        
#numpy vectorizetion method


class vectorized_np:
    def save_Numpy_output(self, numpy_output):
        df = pd.read_csv("result_report.csv", dtype=str)
        df.loc[df.index[-1], "Numpy_Output"] = str(numpy_output)
        df.to_csv("result_report.csv", index=False)
        print(df.tail(1))
    def add_array(self, first, second):
        """
        Performs element-wise addition of two NumPy arrays using vectorization
        and measures execution time.

        Parameters:
        first (numpy.ndarray): First NumPy array
        second (numpy.ndarray): Second NumPy array

        Returns:
        float: Execution time in seconds

        Description:
        - Uses NumPy broadcasting for fast computation.
        - Significantly faster than Python loops.
        """
        start = time.perf_counter()
        result = first + second
        end = time.perf_counter()
        self.save_Numpy_output(result)
        return end - start
    def sub_array(self, first, second):
        """
        Performs element-wise subtraction of two NumPy arrays using vectorization
        and measures execution time.

        Parameters:
        first (numpy.ndarray): First NumPy array
        second (numpy.ndarray): Second NumPy array

        Returns:
        float: Execution time in seconds

        Description:
        - Uses NumPy optimized operations.
        - Useful for performance comparison with Python subtraction loops.
        """
        start = time.perf_counter()
        result = first - second
        end = time.perf_counter()
        self.save_Numpy_output(result)
        return end - start
    def dot_product(self, first, second):
        """
        Computes the dot product of two NumPy arrays using np.dot
        and measures execution time.

        Parameters:
        first (numpy.ndarray): First NumPy array
        second (numpy.ndarray): Second NumPy array

        Returns:
        float: Execution time in seconds

        Description:
        - Uses highly optimized NumPy linear algebra routines.
        - Much faster than manual dot product using loops.
        """
        start = time.perf_counter()
        result = np.dot(first, second)
        end = time.perf_counter()
        self.save_Numpy_output(result)
        return end - start
    def multiply_array(self, first, second):
        """
        Performs element-wise multiplication of two NumPy arrays
        and measures execution time.

        Parameters:
        first (numpy.ndarray): First NumPy array
        second (numpy.ndarray): Second NumPy array

        Returns:
        float: Execution time in seconds

        Description:
        - Uses NumPy vectorized multiplication.
        - Suitable for benchmarking against Python-based multiplication.
        """
        start = time.perf_counter()
        result = first * second
        end = time.perf_counter()
        self.save_Numpy_output(result)
        return end - start
    def div_array(self, first, second):
        """
        Performs element-wise division of two NumPy arrays
        and measures execution time.

        Parameters:
        first (numpy.ndarray): Numerator array
        second (numpy.ndarray): Denominator array

        Returns:
        float: Execution time in seconds

        Description:
        - Uses NumPy vectorized division.
        - Demonstrates performance improvement over Python loops.
        """
        start = time.perf_counter()
        result = first / second
        end = time.perf_counter()
        self.save_Numpy_output(result)
        return end - start
    def matrix_multiply(self, first, second):
        """
        Performs matrix multiplication of two NumPy arrays
        using np.matmul and measures execution time.

        Parameters:
        first (numpy.ndarray): First input matrix
        second (numpy.ndarray): Second input matrix

        Returns:
        float: Execution time in seconds

        Description:
        - Utilizes NumPy's optimized matrix multiplication.
        - Significantly faster than manual nested loop multiplication.
        """
        start = time.perf_counter()
        result = np.matmul(first, second)
        end = time.perf_counter()
        self.save_Numpy_output(result)
        return end - start
    def find_norm(array, ord_type):
        try:
            """
            Calculates the norm of a NumPy array using np.linalg.norm
            and measures execution time.

            Parameters:
            array (numpy.ndarray): Input array
            ord_type (int or str): Order of the norm (e.g., 1, 2, 'fro', etc.)

            Returns:
            float: Execution time in seconds

            Description:
            - Uses NumPy's linear algebra module for norm calculation.
            - Efficiently computes various types of norms.
            """
            start = time.perf_counter()
            result = np.linalg.norm(array, ord=int(ord_type))
            end = time.perf_counter()
            return end - start
        except Exception as e:
            return f"Error : {e}"
    def transpose(array):
        """
        Transposes a NumPy array and measures execution time.

        Parameters:
        array (numpy.ndarray): Input array

        Returns:
        float: Execution time in seconds

        Description:
        - Uses NumPy's built-in transpose function.
        - Efficiently transposes arrays of any dimension.
        """
        start = time.perf_counter()
        result = np.transpose(array)
        end = time.perf_counter()
        return end - start