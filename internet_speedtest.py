import speedtest

def test_speed():
    print("Checking your internet speed... Please wait.\n")
    st = speedtest.Speedtest()
    
    st.get_best_server()
    
    download_speed = st.download() / 1024 / 1024   # convert to Mbps
    upload_speed = st.upload() / 1024 / 1024       # convert to Mbps
    ping = st.results.ping
    
    print("--- Internet Speed Test Results ---")
    print(f"Download Speed : {download_speed:.2f} Mbps")
    print(f"Upload Speed   : {upload_speed:.2f} Mbps")
    print(f"Ping           : {ping:.2f} ms")
    print("-----------------------------------------") 

def main():
    print("Welcome to the Internet Speed Test Tool")
    while True:
        test_speed()
        choice = input("\nDo you want to test again? (y/n): ").lower()
        if choice != 'y':
            print("Exiting the program. Goodbye!")
            break
if __name__ == "__main__":
    main()
