import matplotlib.pyplot as plt
import seaborn as sns
import re

def parser():
    data = {}
    with open("time_medi.txt", "r") as file:
        for line in file:
            match = re.search(r"Thread: (\d+), Tempo medio: ([\d\.]+)", line)
            if match:
                threads = int(match.group(1))
                time = float(match.group(2))
                data[threads] = time
    return data

def plot(data):
    threads = sorted(data.keys())

    #print(data)


    T1 = data[1]  # Time with a single thread
    speedup = {p: T1 / Tp for p, Tp in data.items()}
    efficiency = {p: speedup[p] / p for p in threads}

    print(speedup)
    print(efficiency)
    
    sns.set(style="whitegrid")
    
    # Speedup plot
    plt.figure(figsize=(8, 6))
    plt.plot(threads, [speedup[p] for p in threads], marker='o', label="Speedup")
    plt.plot(threads, threads, 'k--', label="Ideal speedup")
    plt.xlabel("Number of Threads")
    plt.ylabel("Speedup")
    plt.xticks(threads)
    plt.legend()
    plt.title("Speedup vs Number of Threads")
    plt.savefig("speedup_plot.png")
    plt.close()
    
    # Efficiency plot
    plt.figure(figsize=(8, 6))
    plt.plot(threads, [efficiency[p] for p in threads], marker='s', label="Efficiency")
    plt.axhline(y=1, color='k', linestyle='--', label="Ideal efficiency")
    plt.xlabel("Number of Threads")
    plt.ylabel("Efficiency")
    plt.xticks(threads)
    plt.legend()
    plt.title("Efficiency vs Number of Threads")
    plt.savefig("efficiency_plot.png")
    plt.close()

def main():
    data = parser()
    plot(data)

if __name__ == '__main__':  
    main()
