import psutil


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

        # add measurement fields
        measurements = [
            {
                'measurement': 'cpu',
                'fields': {
                    'core_count': psutil.cpu_count(),
                    'usage_pct': psutil.cpu_percent(),
                },
            },
            {
                'measurement': 'memory',
                'fields': {
                    'total_gb': to_gb(memory_metrics.total),
                    'memory_usage_pct': memory_metrics.percent,
                },
            },
            {
                'measurement': 'disk',
                'fields': {
                    'total_gb': to_gb(disk_metrics.total),
                    'avail_gb': to_gb(disk_metrics.free),
                    'used_gb': to_gb(disk_metrics.used),

                },
            },
        ]

        # we can fetch temps if on raspberry pi
        if self.mode == 'prod':
            temp_metrics = psutil.sensors_temperatures()
            cpu_temp_c = round(
                temp_metrics.get('cpu_thermal', {})[0].current,
                1
            )
            measurements.append(
                {
                    'measurement': 'temp',
                    'fields': {
                        'cpu_c': cpu_temp_c,
                    },
                },
            )

        # add hostname as tags
        measurements = [
            {**meas_dict, 'tags': {'hostname': self.hostname}}
            for meas_dict in measurements
        ]
        return measurements


if __name__ == '__main__':
    probe = Probe('test', 'test')
    sample = probe.fetch()
    from pprint import pprint
    pprint(sample)
