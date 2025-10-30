import time

def instant_find(num):
    print("🔍 Searching...")
    time.sleep(0)  # zero delay
    if 1 <= num <= 1_000_000_000:
        print(f"✅ Found number: {num}")
    else:
        print("❌ Number not in range!")

instant_find(123456789)
