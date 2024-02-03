import time

def send_token():
    # Simulate sending a token (replace this with your actual token sending logic)
    print("Token sent!")

def main():
    # Set the initial timestamp
    last_token_time = time.time()

    while True:
        current_time = time.time()

        # Check if 24 hours have passed since the last token sent
        if current_time - last_token_time >= 24 * 60 * 60:
            send_token()
            
            # Update the last token sent timestamp
            last_token_time = current_time

        # Sleep for 1 hour (adjust as needed)
        time.sleep(3600)

if __name__ == "__main__":
    main()
