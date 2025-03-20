#include <iostream>
#include <fstream>
#include <complex>
#include <chrono>
#include <sys/time.h>
#include <cuda_runtime.h>
#include <cuda.h>
#include <cuComplex.h>

// Ranges of the set
#define MIN_X -2
#define MAX_X 1
#define MIN_Y -1
#define MAX_Y 1

// Image ratio
#define RATIO_X (MAX_X - MIN_X)
#define RATIO_Y (MAX_Y - MIN_Y)

// Image size
#define RESOLUTION 3000 //1000
#define WIDTH (RATIO_X * RESOLUTION)
#define HEIGHT (RATIO_Y * RESOLUTION)

#define STEP ((double)RATIO_X / WIDTH)

#define DEGREE 2        // Degree of the polynomial
#define ITERATIONS 1000 // Maximum number of iterations

using namespace std;


__global__ void mandelbrot(int *image)
{

    int i = blockIdx.x * blockDim.x + threadIdx.x;
    int j = blockIdx.y * blockDim.y + threadIdx.y;

    if (j > 0 && j <=HEIGHT - 1 && i > 0 && i <= WIDTH - 1){
        int pos = j * WIDTH + i;

        image[pos] = 0;
        cuDoubleComplex c = make_cuDoubleComplex(i * STEP + MIN_X, j * STEP + MIN_Y);

        cuDoubleComplex z = make_cuDoubleComplex(0.0, 0.0);
        for (int k = 1; k <= ITERATIONS; k++)
        {
            z = cuCadd(cuCmul(z, z), c);
            if (cuCabs(z) >= 2) {
                image[pos] = k;
                break;
            }
        }

    }

        
    
}

void cuda_check(cudaError_t err)
{
  if (err != cudaSuccess){
    fprintf(stderr, "GPUassert: %s\n", cudaGetErrorString(err));
    exit(err);
  }
}

int main(int argc, char **argv)
{

    if(argc < 2)
    {
        cout << "Usage: "<<argv[0] <<" THREAD_SIDE" << endl;
        return -1;
    }

    int THREAD_SIDE = atoi(argv[1]);

    int *const image = new int[HEIGHT * WIDTH];

    int* image_device;
    cuda_check(cudaMalloc(&image_device, HEIGHT * WIDTH * sizeof(int)));

    struct timeval t1, t2;

    gettimeofday(&t1, 0);


    dim3 threads(THREAD_SIDE, THREAD_SIDE);
    dim3 blocks((WIDTH + threads.x - 1) / threads.x, (HEIGHT + threads.y - 1) / threads.y);

    // Call the kernel
    mandelbrot<<<blocks,threads>>>(image_device);

    cuda_check(cudaMemcpy(image, image_device, HEIGHT * WIDTH * sizeof(int), cudaMemcpyDeviceToHost));
    cuda_check(cudaFree(image_device));

    gettimeofday(&t2, 0);

    cout << "Time elapsed: " << (t2.tv_sec - t1.tv_sec) + (t2.tv_usec - t1.tv_usec) * 0.000001 << " seconds." << endl;
    cout << "<<" << blocks.x <<" x "<< blocks.y <<","<< threads.x <<" x "<< threads.y << ">>" << endl;

    // Write the result to a file
    ofstream matrix_out;

    if (argc < 3)
    {
        cout << "Please specify the output file as a parameter." << endl;
        return -1;
    }

    matrix_out.open(argv[2], ios::trunc);
    if (!matrix_out.is_open())
    {
        cout << "Unable to open file." << endl;
        return -2;
    }

    for (int row = 0; row < HEIGHT; row++)
    {
        for (int col = 0; col < WIDTH; col++)
        {
            matrix_out << image[row * WIDTH + col];

            if (col < WIDTH - 1)
                matrix_out << ',';
        }
        if (row < HEIGHT - 1)
            matrix_out << endl;
    }
    matrix_out.close();

    delete[] image; // It's here for coding style, but useless
    return 0;
}