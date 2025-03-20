# Mandelbrot Set - High Performance Computing

## Overview

This repository contains the source code for computing and visualizing the Mandelbrot set using high-performance computing techniques, specifically leveraging **OpenMP** and **CUDA** for parallel execution.

Additionally, the file **Frattini_Timossi.pdf** contains the complete report, which includes detailed explanations, performance analysis, and visual representations of the results.

## Repository Structure

```
.
├── CUDA
│   ├── CUDA_Mandelbrot.ipynb   # Jupyter Notebook with CUDA implementation
│   ├── devicequery.cu          # CUDA device query script
│   ├── helper_cuda.h           # CUDA helper functions
│   ├── helper_string.h         # String manipulation utilities
│   └── mandelbrot.cu           # CUDA implementation of Mandelbrot set
├── Frattini_Timossi.pdf        # Full project report with images and analysis
├── mandelbrot.cpp              # Sequential Mandelbrot C++ implementation
├── mandelbrot_plot.png         # Image of the Mandelbrot fractal
├── OpenMP
│   ├── mandelbrotOPENMP.cpp    # OpenMP implementation of Mandelbrot set
│   ├── OpenMPtime.sh           # Shell script for timing OpenMP execution
│   ├── plotMP.py               # Python script for OpenMP results visualization
│   └── study_plot.py           # Additional OpenMP performance analysis
├── plot.py                     # Python script for plotting results
├── reports_vectorization
│   ├── mandelbrot.optrpt       # Vectorization report
│   └── mandelbrot.opt.yaml     # Optimization report
├── time.sh                     # Shell script for timing sequential execution
└── view_fractal.py             # Python script to display the Mandelbrot set
```

## Implementations

- **Sequential (C++)**: Basic implementation using iterative computation.
- **OpenMP (C++)**: Parallelized version leveraging OpenMP for CPU multi-threading.
- **CUDA (CU)**: GPU-accelerated implementation using CUDA for massively parallel computation.

## Performance Analysis

The **Frattini_Timossi.pdf** report provides a comprehensive analysis of:

- Machine specifications used for testing (CPU & GPU details)
- Vectorization optimizations and issues
- Performance comparisons between **OpenMP** and **CUDA**
- Memory usage and execution time analysis
- Speedup and efficiency graphs

## Results

- OpenMP achieves optimal performance when utilizing all available CPU cores.
- CUDA provides significant speedup but requires careful memory management and thread optimization.
- The best configuration is achieved by optimizing compiler flags and leveraging hardware-specific features.

## License

This project is for academic purposes. Feel free to use and modify the code with appropriate attribution.

---

For a detailed discussion of implementation strategies, optimizations, and results, refer to **Frattini_Timossi.pdf**.
