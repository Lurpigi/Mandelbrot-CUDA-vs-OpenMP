#!/bin/bash

OUTPUT_DIR="output"
mkdir -p $OUTPUT_DIR

SOURCE_FILE="mandelbrot.cpp"

run_config() {
  local config_name=$1
  local compile_cmd=$2
  local output_subdir=$3

  mkdir -p $OUTPUT_DIR/$output_subdir

  echo "Compilazione con la configurazione: $config_name"
  
  eval "$compile_cmd"

  for i in {1..10}; do
    echo "Esecuzione $i di $config_name..."
    ./cool > "$OUTPUT_DIR/$output_subdir/output_$i.txt"
  done
}

declare -A configs
configs["CLASSIC_BEST"]="icpx -O3 -xHost -fp-model fast -ffast-math -o cool $SOURCE_FILE"
configs["_FAST"]="icpx -fast -o cool $SOURCE_FILE"
configs["FAST_XSSE3"]="icpx -fast -xSSE3 -o cool $SOURCE_FILE"
configs["FAST_FFASTSMATH"]="icpx -fast -ffast-math -o cool $SOURCE_FILE"
configs["SIMIL_BEST_FAST"]="icpx -O3 -xHost -fp-model fast -ffast-math -o cool $SOURCE_FILE"

for config_name in "${!configs[@]}"; do
  run_config "$config_name" "${configs[$config_name]}" "$config_name"
done

echo "Tutte le esecuzioni sono state completate. I risultati sono salvati nella cartella $OUTPUT_DIR."
