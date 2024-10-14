import math
import numpy as np
import matplotlib.pyplot as plt
import streamlit as st

# Streamlit commands replace input and print for interaction
st.title("Scientific Calculator with Plotting")

# Basic mathematical operations
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    else:
        return x / y

def power(x, y):
    return x ** y

def square_root(x):
    return math.sqrt(x)

def logarithm(x, base=10):
    if x <= 0:
        return "Error! Logarithm undefined for non-positive values."
    else:
        return math.log(x, base)

def sine(x):
    return math.sin(math.radians(x))

def cosine(x):
    return math.cos(math.radians(x))

def tangent(x):
    return math.tan(math.radians(x))

def factorial(x):
    if x < 0:
        return "Error! Factorial of a negative number doesn't exist."
    else:
        return math.factorial(x)

# Plotting functions
def plot_function(func, start, end, title):
    x = np.linspace(start, end, 400)
    y = func(np.radians(x))
    fig, ax = plt.subplots()
    ax.plot(x, y)
    ax.set(title=title, xlabel="Angle (degrees)", ylabel=title)
    ax.grid(True)
    st.pyplot(fig)

# Main calculator interface
operation = st.sidebar.selectbox("Select operation", 
                                 ["Add", "Subtract", "Multiply", "Divide", "Power", "Square Root", "Logarithm", 
                                  "Sine", "Cosine", "Tangent", "Factorial", "Plot Sine", "Plot Cosine", "Plot Tangent"])

# For basic operations
if operation in ["Add", "Subtract", "Multiply", "Divide", "Power"]:
    num1 = st.number_input("Enter first number", value=0.0, step=0.1)
    num2 = st.number_input("Enter second number", value=0.0, step=0.1)

    if operation == "Add":
        st.write(f"Result: {num1} + {num2} = {add(num1, num2)}")
    elif operation == "Subtract":
        st.write(f"Result: {num1} - {num2} = {subtract(num1, num2)}")
    elif operation == "Multiply":
        st.write(f"Result: {num1} * {num2} = {multiply(num1, num2)}")
    elif operation == "Divide":
        st.write(f"Result: {num1} / {num2} = {divide(num1, num2)}")
    elif operation == "Power":
        st.write(f"Result: {num1} ^ {num2} = {power(num1, num2)}")

# For square root
elif operation == "Square Root":
    num = st.number_input("Enter number", value=0.0, step=0.1)
    st.write(f"√{num} = {square_root(num)}")

# For logarithm
elif operation == "Logarithm":
    num = st.number_input("Enter number", value=1.0, step=0.1)
    base = st.number_input("Enter base (default is 10)", value=10.0, step=1.0)
    st.write(f"log base {base} of {num} = {logarithm(num, base)}")

# For sine, cosine, and tangent
elif operation in ["Sine", "Cosine", "Tangent"]:
    num = st.number_input("Enter angle in degrees", value=0.0, step=1.0)
    if operation == "Sine":
        st.write(f"sin({num}) = {sine(num)}")
    elif operation == "Cosine":
        st.write(f"cos({num}) = {cosine(num)}")
    elif operation == "Tangent":
        st.write(f"tan({num}) = {tangent(num)}")

# For factorial
elif operation == "Factorial":
    num = st.number_input("Enter a non-negative integer", value=1, step=1, min_value=0)
    st.write(f"{num}! = {factorial(num)}")

# For plotting sine, cosine, and tangent functions
elif operation == "Plot Sine":
    start = st.number_input("Enter start angle in degrees", value=0.0, step=1.0)
    end = st.number_input("Enter end angle in degrees", value=360.0, step=1.0)
    plot_function(np.sin, start, end, "Sine Function")

elif operation == "Plot Cosine":
    start = st.number_input("Enter start angle in degrees", value=0.0, step=1.0)
    end = st.number_input("Enter end angle in degrees", value=360.0, step=1.0)
    plot_function(np.cos, start, end, "Cosine Function")

elif operation == "Plot Tangent":
    start = st.number_input("Enter start angle in degrees", value=0.0, step=1.0)
    end = st.number_input("Enter end angle in degrees", value=360.0, step=1.0)
    plot_function(np.tan, start, end, "Tangent Function")
