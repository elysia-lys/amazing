def read_config(filename):
    config = {}

    with open(filename, "r") as file:
        content = file.read()

        for line in content.splitlines():
            if not line or line.startswith("#"):
                continue

            key, value = line.split("=", 1)
            config[key] = value

    required_keys = [
            "WIDTH", "HEIGHT", "ENTRY"
            "EXIT", "OUTPUT_FILE", "PERFECT"
            ]

    for key in required_keys:
        if key not in config:
            raise ValueError(f"Missing configuration key: {key}")

    return config


def convert_config(config):

    config["WIDTH"] = int(config["WIDTH"])
    config["HEIGHT"] = int(config["HEIGHT"])

    x, y = config["ENTRY"].split(",")
    config["ENTRY"] = (int(x), int(y))

    a, b = config["EXIT"].split(",")
    config["EXIT"] = (int(a), int(b))

    config["PERFECT"] = config["PERFECT"].lower() == "true"

    return config


def error_handling(config):

    if config["WIDTH"] <= 0:
        raise ValueError("Invalid Width size")
    if config["HEIGHT"] <= 0:
        raise ValueError("Invalid Height size")

    x, y = config["ENTRY"]
    if x >= config["WIDTH"] or x < 0:
        raise ValueError("Invalid x entry")
    if y >= config["HEIGHT"] or y < 0:
        raise ValueError("Invalid y entry")

    a, b = config["EXIT"]
    if a >= config["WIDTH"] or a < 0:
        raise ValueError("Invalid x exit")
    if b >= config["HEIGHT"] or b < 0:
        raise ValueError("Invalid y exit")

    if config["ENTRY"] == config["EXIT"]:
        raise ValueError("Entry and Exit cannot be the same")

    if not config["OUTPUT_FILE"].endswith(".txt"):
        raise ValueError("Invalid file")


if __name__ == "__main__":
    print("=== Maze config ===")
    print("=== Getting config from config.txt ===")

    try:
        config = read_config("config.txt")

        if config["PERFECT"].lower() not in ("true", "false"):
            raise ValueError("PERFECT must be in True or False")

        convert_config(config)

        error_handling(config)

        print(config["WIDTH"])
        print(config["HEIGHT"])
        print(config["ENTRY"])
        print(config["EXIT"])
        print(config["OUTPUT_FILE"])
        print(config["PERFECT"])

    except ValueError as error:
        print(error)
