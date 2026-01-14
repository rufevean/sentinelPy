import regex as re

def login_detected(line):
    parameters = list(line.split())
    timestamp = parameters[0] + " " + parameters[1]
    description = " ".join(parameters[7:])
    pattern = r"'system\.login\.done'(.*)'"
    match = re.findall(pattern, description) 
    return timestamp, match

def main():
    with open("logs/auth.log", "r") as f:
        lines = f.readlines()   
    for line in lines:
        if "system.login.done" in line:
            timestamp, match = login_detected(line)
            print(timestamp, match)


if __name__ == "__main__":
    main()