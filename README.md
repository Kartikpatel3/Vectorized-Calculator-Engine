# 🧮 Vectorized Calculator Engine

Vectorized Calculator Engine is a **Python Command Line based calculator** that performs
mathematical operations on **1D, 2D, and 3D arrays** and compares the performance of
**pure Python (native loops)** with **NumPy vectorized operations**.

This project is useful for learning **NumPy optimization**, **array operations**,
and **performance benchmarking**.

## ⚙️ Installation

```bash pip install -r requirements.txt```

## 🚀 Features

### 🔹 Mathematical Operations
- Vector Addition  
- Vector Subtraction  
- Element-wise Multiplication  
- Element-wise Division  
- Dot Product  

Supports **1D, 2D, and 3D arrays**.

---

### 🔹 Advanced Operations
- Matrix Multiplication  
- Norm Calculation  
- Transpose Operation  

---

### 🔹 Performance Comparison
Each operation is executed in two ways:
- **Native Python (loops)**
- **NumPy Vectorized Method**

Execution time is recorded for both and compared.

---

### 🔹 Reports Management
The project automatically saves results into CSV files.

You can:
- View Performance Report  
- Clear Performance Report  
- View Result Report  
- Clear Result Report  

---

## 📊 Reports Generated

### 📁 result_report.csv
Stores computation results.

| First_Array | Second_Array | Native_Output | Numpy_Output |
|------------|-------------|---------------|--------------|

---

### 📁 performance_report.csv
Stores performance comparison.

| Operation | Size | Naive Time | NumPy Time | Speedup |
|----------|------|------------|-----------|---------|

---

## 🧠 How It Works

1. User selects an option from the menu  
2. User enters array dimension and values  
3. Operation runs using:
   - Python loops
   - NumPy vectorization  
4. Execution time is measured  
5. Results are saved in reports  

---

## 📁 Project Structure

Vectorized-Calculator-Engine/
│
├── engine.py
├── operations.py
├── performance.py
├── reports/
│   ├── performance_report.csv
│   └── result_report.csv
├── requirements.txt
├── README.md
└── .gitignore


---

## 🖥 Example
...soon

## ▶️ Usage

Run the calculator using:

```bash python engine.py```

## 📸 Screenshots

### Main Menu
![Main Menu](screenshots/menu.png)

### Vector Operation Output
![Vector Output](screenshots/vector_addition.png)

### Performance Report
![Performance Report](screenshorts/performance_report_view (2).png)
