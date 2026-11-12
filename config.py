def read_config():
    config = {}

    with open("config.txt", "r") as file:
        content = file.read()

        for line in content.splitlines():
            if not line or line.startswith("#"):
                continue

            key, value = line.split("=")
            config[key] = value

        # print(config)
        return config


if __name__ == "__main__":
    read_config()
