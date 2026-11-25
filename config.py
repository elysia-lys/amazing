from typing import Any


def read_config(filename: str) -> dict[str, Any]:
    config: dict[str, Any] = {}

    with open(filename, "r") as file:
        content = file.read()

        for line in content.splitlines():
            if not line or line.startswith("#"):
                continue

            key, value = line.split("=", 1)
            config[key] = value

    required_keys = [
            "WIDTH", "HEIGHT", "ENTRY",
            "EXIT", "OUTPUT_FILE", "PERFECT", "SEED"
            ]

    for key in required_keys:
        if key not in config:
            raise ValueError(f"Missing configuration key: {key}")

    return config


def convert_config(config: dict[str, Any]) -> dict[str, Any]:

    config["WIDTH"] = int(config["WIDTH"])
    config["HEIGHT"] = int(config["HEIGHT"])

    x, y = config["ENTRY"].split(",")
    config["ENTRY"] = (int(x), int(y))

    a, b = config["EXIT"].split(",")
    config["EXIT"] = (int(a), int(b))

    config["PERFECT"] = config["PERFECT"].lower() == "true"

    config["SEED"] = int(config["SEED"]) if "SEED" in config else None

    return config


def error_handling(config: dict[str, Any]) -> None:

    if config["WIDTH"] <= 0:
        raise ValueError("Invalid Width size")
    if config["HEIGHT"] <= 0:
        raise ValueError("Invalid Height size")

    x, y = config["ENTRY"]
    if x >= config["WIDTH"] or x < 0:
        raise ValueError("Invalid x entry")
    if y >= config["HEIGHT"] or y < 0:
        raise ValueError("Invalid y entry")
    if (
            x != 0 and x != config["WIDTH"] - 1
            and y != 0 and y != config["HEIGHT"] - 1
            ):
        raise ValueError("Entry must be on the maze boundary")

    a, b = config["EXIT"]
    if a >= config["WIDTH"] or a < 0:
        raise ValueError("Invalid x exit")
    if b >= config["HEIGHT"] or b < 0:
        raise ValueError("Invalid y exit")
    if (
            a != 0 and a != config["WIDTH"] - 1
            and b != 0 and b != config["HEIGHT"] - 1
            ):
        raise ValueError("Exit must be on the maze boundary")

    if config["ENTRY"] == config["EXIT"]:
        raise ValueError("Entry and Exit cannot be the same")

    if not config["OUTPUT_FILE"].endswith(".txt"):
        raise ValueError("Invalid file")

    if config["SEED"] is not None and not isinstance(config["SEED"], int):
        raise ValueError("Seed must be an integer")
