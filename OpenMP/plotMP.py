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
                if file_name.startswith("run_") and file_name.endswith(".txt"):
                    file_path = os.path.join(config_path, file_name)
                    time_value = extract_time(file_path)
                    if time_value is not None:
                        data.append((config_name, time_value))
    return data

def plot_boxplot(data):
    """Genera un grafico a palle della varianza dei tempi."""
    df = pd.DataFrame(data, columns=['Threads', 'Time'])

    df['Threads'] = df['Threads'].astype(int)
    df = df.sort_values('Threads')
    
    # Calcola e stampa il tempo medio per ogni Thread
    mean_times = df.groupby('Threads')['Time'].mean()
    for thread, mean_time in mean_times.items():
        print(f"Thread: {thread}, Tempo medio: {mean_time:.6f} secondi")
    
    sns.set_style("whitegrid")
    plt.figure(figsize=(10, 6))
    sns.barplot(x='Threads', y='Time', data=df)
    plt.xlabel("Threads", fontsize=12)
    plt.ylabel("Times (s)", fontsize=12)
    plt.title("Execution time per Threads", fontsize=14)
    plt.tight_layout()

    output_file = "barplot.png"
    plt.savefig(output_file)
    print(f"Plot saved as {output_file}")
    plt.show()


    

if __name__ == "__main__":
    base_directory = "times"
    dataset = collect_data(base_directory)
    if dataset:
        plot_boxplot(dataset)
    else:
        print("Nessun dato trovato.")
