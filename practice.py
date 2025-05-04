import time

correct_password = "python123"
max_attempts = 3

while True:  # Loop restarts login system after lock
    attempt = 0

    while attempt < max_attempts:
        entered = input("Enter Password: ")  # Using input() instead of getpass
        if entered == correct_password:
            print("✅ Access Granted")
            exit()  # End the program
        else:
            attempt += 1
            if attempt < max_attempts:
                print(f"❌ Incorrect! Attempts left: {max_attempts - attempt}")
            else:
                print("⛔ Too many attempts! System locked for 10 seconds...")
                time.sleep(10)
                print("\n🔁 You can try logging in again.\n")
                break  # Restarts the outer loop

            
        