export async function generateReport() {
  const res = await fetch("http://127.0.0.1:5000/generate-report");
  return res.json();
}
