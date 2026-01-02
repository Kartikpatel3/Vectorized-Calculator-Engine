import numpy as np
import pandas as pd
import os
import ast
from performance import performance_table as pt
performance = pt()
def main():
    while True:
        print("<<<<< Vectorized Calculator Engine >>>>>\n\n1. Mathematical Operations \n2. Advance Operations \n3. Reports Manager\n4. Exit ")
        user_input = input("ENTER YOUR KEY >> ")
        if user_input == "1":
            print("\n<<<<< Mathematical Operations >>>>>\n\n1. Vector Addition \n2. Vector Subtraction \n3. Element-Wise Multiplication \n4. Element-Wise Division \n5. Menu")
            user_input = input("ENTER YOUR KEY >> ")
            if user_input == "1":
                user_dim = input("Enter Your Dimentions of Array (1D,2D,3D) = ").lower().strip()
                try:
                    first = ast.literal_eval(input("\nNOW >> \nEnter First Array = "))
                    second = ast.literal_eval(input("Enter Second Array = "))
                except:
                    print("\nPlease!!! Enter Input as a List With Proper Commas and Brackets.")
                    continue
                performance.Add(first, second, user_dim)
            elif user_input == "2":
                user_dim = input("Enter Your Dimentions of Array (1D,2D,3D) = ")
                try:
                    first = ast.literal_eval(input("\nNOW >> \nEnter First Array = "))
                    second = ast.literal_eval(input("Enter Second Array = "))
                except:
                    print("\nPlease!!! Enter Input as a List With Proper Commas and Brackets.")
                    continue
                performance.Sub(first, second, user_dim)
            elif user_input == "3":
                user_dim = input("Enter Your Dimentions of Array (1D,2D,3D) = ")
                try:
                    first = ast.literal_eval(input("\nNOW >> \nEnter First Array = "))
                    second = ast.literal_eval(input("Enter Second Array = "))
                except:
                    print("\nPlease!!! Enter Input as a List With Proper Commas and Brackets.")
                    continue
                performance.Multi(first, second, user_dim)
            elif user_input == "4":
                user_dim = input("Enter Your Dimentions of Array (1D,2D,3D) = ")
                try:
                    first = ast.literal_eval(input("\nNOW >> \nEnter First Array = "))
                    second = ast.literal_eval(input("Enter Second Array = "))
                except:
                    print("\nPlease!!! Enter Input as a List With Proper Commas and Brackets.")
                    continue
                performance.Divi(first, second, user_dim)
            elif user_input == "5":
                continue
        elif user_input == "2":
            print("\n<<<<< Advance Operations >>>>>\n\n1. Matrix Multiplication \n2. Transpose of Matrix \n3. Dot Product \n4. Norm Of a Vector \n5. Menu")
            user_input = input("ENTER YOUR KEY >> ")
            if user_input == "1":
                user_dim = input("Enter Your Dimentions of Matrix (2D,3D) = ")
                try:
                    first = ast.literal_eval(input("\nNOW >> \nEnter First Matrix = "))
                    second = ast.literal_eval(input("Enter Second Matrix = "))
                except:
                    print("\nPlease!!! Enter Input as a List With Proper Commas and Brackets.")
                    continue
                performance.Mat_Mul(first, second, user_dim)
            elif user_input == "2":
                user_dim = input("Enter Your Dimentions of Matrix (2D,3D) = ")
                try:
                    array = ast.literal_eval(input("\nNOW >> \nEnter Matrix = "))
                except:
                    print("\nPlease!!! Enter Input as a List With Proper Commas and Brackets.")
                    continue
                performance.transpose(array, user_dim)
            elif user_input == "3":
                user_dim = input("Enter Your Dimentions of Vectors (1D,2D,3D) = ")
                try:
                    first = ast.literal_eval(input("\nNOW >> \nEnter First Vector = "))
                    second = ast.literal_eval(input("Enter Second Vector = "))
                except:
                    print("\nPlease!!! Enter Input as a List With Proper Commas and Brackets.")
                    continue
                performance.Dot(first, second, user_dim)
            elif user_input == "4":
                ord_type = input("Enter ord for Norm Value (1 or 2)= ")
                try:
                    first = ast.literal_eval(input("\nNOW >> \nEnter Vector = "))
                except:
                    print("\nPlease!!! Enter Input as a List With Proper Commas and Brackets.")
                    continue
                performance.Norm(first, ord_type)
            elif user_input == "5":
                continue
            else:
                print("\nPlease Enter Correct Key Numbers Only\n")
                continue
        elif user_input == "3":
            print("\n<<<<< Reports Manager >>>>>\n\n1. View Calculation Report \n2. Clear Calculation Report \n3. View Performance Report \n4. Clear Performance Report \n5. Menu")
            user_input = input("ENTER YOUR KEY >> ")
            if user_input == "1":
                if os.path.exists("result_report.csv"):
                    df = pd.read_csv("result_report.csv")
                    print(df)
            elif user_input == "2":
                if os.path.exists("result_report.csv"):
                    df = pd.read_csv("result_report.csv")
                    df.drop(df.index, inplace=True)
                    df.to_csv("result_report.csv", index=False)
                    print("Calculation Report Cleared Successfully")
            elif user_input == "3":
                if os.path.exists("performance_report.csv"):
                    df = pd.read_csv("performance_report.csv")
                    print(df)
            elif user_input == "4":
                if os.path.exists("performance_report.csv"):
                    df = pd.read_csv("performance_report.csv")
                    df.drop(df.index, inplace=True)
                    df.to_csv("performance_report.csv", index=False)
                    print("Performance Report Cleared Successfully")
                else:
                    print("File not found")
            elif user_input == "5":
                continue
            else:
                print("Please enter correct number ")
                continue
        elif user_input == "4":
            print("THANKYOU FOR USING VECTORISED CALCULATOR ENGINE")
            break
        else:
            print("Please Enter Correct Key Numbers Only")
            continue
        
main()
