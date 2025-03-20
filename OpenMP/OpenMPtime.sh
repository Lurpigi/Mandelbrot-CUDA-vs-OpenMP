#!/bin/bash

elements=(1 2 4 8 12 16 20 24)
mkdir -p times

icpx -O3 -xHost -qopenmp -fp-model fast -ffast-math mandelbrotOPENMP.cpp

for val in "${elements[@]}"; do
    echo "Eseguendo con argomento: $val"
    
    mkdir -p "times/$val"
    
    for i in {1..10}; do
        echo "Esecuzione $i per il valore $val"
        ./a.out "$val" > "times/$val/run_$i.txt"
    done
done
