export async function fetchMetrics() {
  const res = await fetch("http://127.0.0.1:5000/metrics");
  return res.json();
}
