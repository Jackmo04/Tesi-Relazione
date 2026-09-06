# Other imports...
import requests

PROMETHEUS_URL = "http://localhost:9090/api/v1/query"

class PerformanceMonitor:
    # Other methods...

    @staticmethod
    def get_drop_metrics() -> dict:
        def query(q: str) -> float:
            try:
                res = requests.get(PROMETHEUS_URL, params={'query': q}).json()
                data = res.get('data', {}).get('result', [])
                return int(data[0]['value'][1]) if data else 0
            except Exception:
                return 0.0
        return {
            "tetragon": query('sum(tetragon_observer_ringbuf_events_lost_total)'),
            "falco": query('sum(falcosecurity_scap_n_drops_total)')
        }