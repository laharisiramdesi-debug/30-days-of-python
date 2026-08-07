with open("log.txt","w") as file:
    file.write("INFO User lahari logged in\n")
    file.write("ERROR Database connection failed\n")
    file.write("SUCCESS File uploaded\n")
    file.write("FAILED Login attempt for madhu\n")
    file.write("INFO System restarted\n")
with open("log.txt","r") as file:
    for line in file:
        if "ERROR"  in line or "FAILED" in line:
            print(line.strip())