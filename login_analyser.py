failed_counts = {}

with open("logins.txt", "r") as file:
    logs = file.readlines()

for log in logs:
    log = log.strip()
    parts = log.split(",")

    if len(parts) == 2:
        username = parts[0]
        status = parts[1].strip()

        if status == "failed":
            if username in failed_counts:
                failed_counts[username] += 1
            else:
                failed_counts[username] = 1

print("Failed login summary:")
for user, count in failed_counts.items():
    print(f"{user}: {count} failed attempt(s)")

print("\nSuspicious accounts (2 or more failed attempts):")
for user, count in failed_counts.items():
    if count >= 2:
        print(user)
        print("\n--- Analysis Complete ---")
        if len(failed_counts) == 0:
    print("No failed login attempts detected.")