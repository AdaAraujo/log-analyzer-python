import pandas as pd
import matplotlib.pyplot as plt

def analyze_logs(file):
    data = []
    
    with open(file, "r") as f:
        for line in f:
            ip, status = line.strip().split(" - ")
            data.append({"ip": ip, "status": status})
            
    df = pd.DataFrame(data)
    
    # filter failed logins
    failed = df[df["status"] == "FAILED LOGIN"]
    
    # count attempts per IP
    attempts = failed["ip"].value_counts()
    
    print("\n Top IPs with most failed attempts:\n")
    print(attempts.head())
    
    print("\n Possible brute force detected:\n")
    
    alerts = attempts[attempts >= 3]
    
    for ip, count in alerts.items():
        print(f"[ALERT] {ip} had {count} failed attempts")
        
    # save results
    with open("results.txt", "w") as f:
        for ip, count in alerts.items():
            f.write(f"[ALERT] {ip} had {count} failed attempts\n")
            
    print("\nResults saved to results.txt")
    
    return attempts

def generate_graph(attempts):
    attempts.head(5).plot(kind="bar")
    plt.title("Top IPs with Failed Login Attempts")
    plt.xlabel("IP address")
    plt.ylabel("Number of Failures")
    plt.show()
    
def menu():
    print("\n=== LOG ANALYZER ===")
    print("1 - Analyze log file")
    print("2 - Exit")
    
    option = input("Choose an option: ")
    
    if option == "1":
        file = input("Enter log file name (e.g., sample_log.txt): ")
        
        try:
            attempts = analyze_logs(file)
            
            show_graph = input("\nDo you want to see the graph? (y/n): ")
            if show_graph.lower() == "y":
                generate_graph(attempts)
        
        except FileNotFoundError:
            print("File not found.")
    elif option == "2":
        print("Existing...")
        
    else:
        print("Invalid option.")
        
if __name__ == "__main__":
    menu()