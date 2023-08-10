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

| Environment Variable | Description                                     | Default Value         | Example Value         |
|----------------------|-------------------------------------------------|-----------------------|-----------------------|
| ENV                  | Environment (e.g., "production", "development") |                       | production            |
| HOST_NAME            | Hostname of the container or machine            | Result of `socket.gethostname()` | my-container-host    |
| SAMPLE_INTERVAL      | Interval for metric sampling (in seconds)       | 900                   | 300                   |
| INFLUX_URL           | InfluxDB URL                                    |                       | http://localhost:8086 |
| INFLUX_TOKEN         | InfluxDB Token                                  |                       | my-secret-influx-token|
| INFLUX_BUCKET        | InfluxDB Bucket Name                            |                       | my-influx-bucket      |
| INFLUX_ORG           | InfluxDB Organization                           |                       | my-influx-org         |


## Optimizing image
The influx3 client library has a lot of heavy dependencies that are not really needed. 
Work can be done to improve image size by using requests to post to influx.
