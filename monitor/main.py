import time

from influxdb_client_3 import InfluxDBClient3

from probe import Probe
from config import Config
import logging


logging.basicConfig(level=logging.INFO)

# get conf params
conf = Config()

# setup InfluxDB client
influx_client = InfluxDBClient3(
    host=conf.influx_url,
    token=conf.influx_token,
    database=conf.influx_bucket,
    org=conf.influx_org,
)

# create probe instance
probe = Probe(conf.hostname, conf.env)


# depending on run mode, fetch one value or run continuously
def run_scraper():
    logging.info('Starting metrics monitoring')
    logging.info(f'influx url: {conf.influx_url}')

    while True:
        data = probe.fetch()

        if conf.influx_url:
            influx_client.write(data)
        if conf.env == 'prod':
            time.sleep(conf.sample_interval)
        else:
            break


if __name__ == '__main__':
    print('hello')
    run_scraper()
