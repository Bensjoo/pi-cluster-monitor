import time

from influxdb_client import InfluxDBClient
from influxdb_client.client.write_api import SYNCHRONOUS
from probe import Probe
from config import Config
import logging


logging.basicConfig(level=logging.INFO)

# get conf params
conf = Config()

# setup InfluxDB client
influx_client = InfluxDBClient(
    url=conf.influx_url,
    token=conf.influx_token,
)
write_api = influx_client.write_api(write_options=SYNCHRONOUS)

# create probe instance
probe = Probe(conf.hostname, conf.env)


# depending on run mode, fetch one value or run continuously
def run_scraper():
    logging.info('Starting metrics monitoring')
    logging.info(f'influx url: {conf.influx_url}')

    while True:
        data = probe.fetch()

        if conf.influx_url:
            write_api.write('hardware-metrics', 'vandelay', data)
        if conf.env == 'prod':
            time.sleep(conf.sample_interval)
        else:
            break


if __name__ == '__main__':
    run_scraper()
