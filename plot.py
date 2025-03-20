import os
import re
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

def extract_time(file_path):
    """Estrae il tempo in secondi dal file di testo."""
    with open(file_path, 'r') as file:
        for line in file:
            match = re.search(r'Time elapsed: ([\d\.]+) seconds\.', line)
            if match:
                return float(match.group(1))
    return None

def collect_data(base_dir):
    """Raccoglie i dati dai file nelle sottocartelle."""
    data = []
    for config_name in os.listdir(base_dir):
        config_path = os.path.join(base_dir, config_name)
        if os.path.isdir(config_path):
            for file_name in os.listdir(config_path):
                if file_name.startswith("output_") and file_name.endswith(".txt"):
                    file_path = os.path.join(config_path, file_name)
                    time_value = extract_time(file_path)
                    if time_value is not None:
                        data.append((config_name, time_value))
    return data

def plot_boxplot(data):
    """Genera un boxplot orizzontale elegante con Seaborn."""
    df = pd.DataFrame(data, columns=["Configuration", "Time (s)"])
    plt.figure(figsize=(15, 7))
    sns.set_style("whitegrid")
    ax = sns.boxplot(y=df["Configuration"], x=df["Time (s)"], orient='h', width=0.6, linewidth=2.5, fliersize=4)
    
    ax.set_xlabel("Execution Time (seconds)", fontsize=14, fontweight='bold')
    ax.set_ylabel("Configuration", fontsize=14, fontweight='bold')
    ax.set_title("Performance Analysis per Configuration", fontsize=16, fontweight='bold')
    plt.yticks(rotation=45)
    plt.xticks(fontsize=12)
    plt.yticks(fontsize=12)
    plt.grid(axis='x', linestyle='--', alpha=0.7)

    output_file = "boxplot.png"
    plt.savefig(output_file)
    print(f"Plot saved as {output_file}")

    plt.show()

if __name__ == "__main__":
    base_directory = "times_configs"
    dataset = collect_data(base_directory)
    if dataset:
        plot_boxplot(dataset)
    else:
        print("Nessun dato trovato.")
