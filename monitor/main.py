import time

from influxdb_client_3 import InfluxDBClient3, Point

from probe import Probe
from config import Config


# get conf params
conf = Config()

# setup InfluxDB client
influx_client = InfluxDBClient3(
    host=conf.influx_url,
    token=conf.influx_token,
    org=conf.influx_org
)

probe = Probe(conf.hostname)


def run_scraper():
    while True:
        # scrape data
        data = probe.fetch()
        
        if conf.influx_url:
            point = (
                Point(conf.influx_measurement_name)
                .tag("host", data['hostname'])
                .field()
            )


        # only run one post if not in live mode
        if conf.env == 'prod':
            time.sleep(conf.sample_interval)
        else:
            break
    pass


if __name__ == '__main__':
    print('hello')