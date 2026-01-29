import { useState } from "react";
import { generateReport } from "./api/reportApi";
import { fetchMetrics } from "./api/metricsApi";
import ReportView from "./components/ReportView";
import MetricsCards from "./components/MetricsCards";
import UploadTickets from "./components/UploadTickets";

function App() {
  const [report, setReport] = useState("");
  const [metrics, setMetrics] = useState(null);

  const handleGenerate = async () => {
    const reportData = await generateReport();
    const metricsData = await fetchMetrics();

    setReport(reportData.report);
    setMetrics(metricsData);
  };

  return (
    <div style={{ padding: "20px" }}>
      <h2>AI Ops Dashboard</h2>

      <UploadTickets />

      <button onClick={handleGenerate} style={{ marginTop: "10px" }}>
        Generate Report
      </button>

      <MetricsCards metrics={metrics} />

      <ReportView report={report} />
    </div>
  );
}

export default App;
