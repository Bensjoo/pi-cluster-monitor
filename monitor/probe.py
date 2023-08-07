import psutil
import time


def to_gb(bytes):
    return round(bytes / (1024.0 ** 3), 2)


class Probe:
    def __init__(self, hostname, mode):
        self.hostname = hostname
        self.mode = mode

    def fetch(self):
        # memory and disk methods yields dicts
        memory_metrics = psutil.virtual_memory()
        disk_metrics = psutil.disk_usage('/')

        measurements = {
            'ts': int(time.time()),

            'cpu_tot': psutil.cpu_count(),
            'cpu_usage_pct': psutil.cpu_percent(),

            'memory_tot_gb': to_gb(memory_metrics.total),
            'memory_usage_pct': memory_metrics.percent,

            'disk_tot_gb': to_gb(disk_metrics.total),
            'disk_avail_gb': to_gb(disk_metrics.free),
            'disk_used_gb': to_gb(disk_metrics.used)
        }

        # we can fetch temps if on raspberry pi
        if self.mode in 'prod':
            temp_metrics = psutil.sensors_temperatures()
            measurements['temp_cpu_c'] = round(
                temp_metrics.get('cpu_thermal', {})[0].current, 1)

        # append metadata
        return {
            'hostname': self.hostname,
            'measurements': measurements,
        }


if __name__ == '__main__':
    probe = Probe('test', 'test')
    sample = probe.fetch()
    from pprint import pprint
    pprint(sample)
