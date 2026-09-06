# Other imports...
import requests

PROMETHEUS_URL = "http://localhost:9090/api/v1/query"

class PerformanceMonitor:
    # Other methods...

    @staticmethod
    def get_drop_metrics() -> dict:
        def query(q: str) -> int:
            try:
                res = requests.get(PROMETHEUS_URL, params={'query': q}).json()
                data = res.get('data', {}).get('result', [])
                return int(data[0]['value'][1])
            except Exception as e:
                logger.error(f"Failed to query Prometheus for '{q}': {e}")
                return 0
            
        return {
            "tetragon": query('tetragon_observer_ringbuf_events_lost_total'),
            "falco": query('falcosecurity_scap_n_drops_total')
        }