def generate_report(password, strength):
    with open("report.txt", "w") as f:
        f.write("PASSWORD SECURITY REPORT\n\n")
        f.write(f"Password: {password}\n")
        f.write(f"Strength: {strength}\n")
    print("Report generated!")
