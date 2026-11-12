def read_config(filename):
    config = {}

    with open(filename, "r") as file:
        content = file.read()

        for line in content.splitlines():
            if not line or line.startswith("#"):
                continue

            key, value = line.split("=")
            config[key] = value

    return config


def convert_config(config):
    
    config["WIDTH"] = int(config["WIDTH"])
    config["HEIGHT"] = int(config["HEIGHT"])

    x , y = config["ENTRY"].split(",")
    config["ENTRY"] = (int(x) , int(y))

    a , b = config["EXIT"].split(",")
    config["EXIT"] = (int(a) , int(b))

    config["OUTPUT_FILE"] = "maze.txt"

    config["PERFECT"] = config["PERFECT"] == "True"

    return config


if __name__ == "__main__":
    read_config("config.txt")
