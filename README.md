# Pi cluster monitoring microservice
**Work in progress, but goal is:**

Uses primarily python + psutil package to check hardware metrics  at an interval 
on your Raspberry Pi or even cluster of Pis.

Able to post these metrics to influx DB and/or expose as a metrics endpoint for prometheus.

## setup development
Im using [poetry](https://python-poetry.org/) together with `pyenv`, `pyenv-virtualenv` (installed using brew)

```bash
poetry install
```

## Configuration
The microservice will look for the following environment variables:

| Environment Variable | Description                                     | Example Value          |
|----------------------|-------------------------------------------------|------------------------|
| ENV                  | Environment (e.g., "prod", "dev")               | prod                   |
| HOST_NAME            | hostname of device (e.g. 'elaine', 'raspberry') | raspberrypi            |
| INFLUX_URL           | InfluxDB URL (if not set, disable influx posts) | http://localhost:8086  |
| INFLUX_TOKEN         | InfluxDB Token                                  | my-secret-influx-token |
| INFLUX_BUCKET        | InfluxDB Bucket Name                            | my-influx-bucket       |
| INFLUX_ORG           | InfluxDB Organization                           | my-influx-org          |
| ENABLE_PROM          | Enable Prometheus metrics endpoint              | true                   |
| PROM_PORT            | Prometheus metrics endpoint port                | 8000                   |


## WIP sample code
```python
influx docs example
    # connectivity
    database = "smoke-test"

    data = {
        "point1": {
            "location": "Klamath",
            "species": "bees",
            "count": 23,
        },
        "point2": {
            "location": "Portland",
            "species": "ants",
            "count": 30,
        },
        "point3": {
            "location": "Klamath",
            "species": "bees",
            "count": 28,
        },
        "point4": {
            "location": "Portland",
            "species": "ants",
            "count": 32,
        },
        "point5": {
            "location": "Klamath",
            "species": "bees",
            "count": 29,
        },
        "point6": {
            "location": "Portland",
            "species": "ants",
            "count": 40,
        },
    }

    for key in data:
        point = (
            Point("census")
            .tag("location", data[key]["location"])
            .field(data[key]["species"], data[key]["count"])
        )
        influx_client.write(database=database, record=point)
        time.sleep(1)  # separate points by 1 second

    print("Complete. Return to the InfluxDB UI.")
```