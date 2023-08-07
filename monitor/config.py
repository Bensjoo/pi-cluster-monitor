import os
import socket


class Config():
    # assume we cant read temps and wont push to dbs if not prod
    env = os.getenv('ENV')
    hostname = os.getenv('HOST_NAME', socket.gethostname())
    sample_interval = int(os.getenv('SAMPLE_INTERVAL', 60*15))

    influx_url = os.getenv('INFLUX_URL')
    influx_token = os.getenv('INFLUX_TOKEN')
    influx_bucket = os.getenv('INFLUX_BUCKET')
    influx_measurement_name = os.getenv(
        'INFLUX_MEASUREMENT_NAME',
        'pi-metrics'
    )
    influx_org = os.getenv('INFLUX_ORG')

    enable_prom = os.getenv('ENABLE_PROM')
    prom_port = os.getenv('PROM_PORT')
