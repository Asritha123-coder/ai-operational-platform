import { useState } from "react";
import { generateReport } from "./api/reportApi";
import { fetchMetrics } from "./api/metricsApi";
import ReportView from "./components/ReportView";
import MetricsCards from "./components/MetricsCards";
import UploadTickets from "./components/UploadTickets";
import Recommendations from "./components/Recommendations";


function App() {
  const [report, setReport] = useState("");
  const [metrics, setMetrics] = useState(null);
  const [recommendations, setRecommendations] = useState([]);
  const [aiReport, setAiReport] = useState("");


  const handleGenerate = async () => {
    const reportData = await generateReport();
    const metricsData = await fetchMetrics();
    //  console.log("RECOMMENDATIONS FROM API:", reportData.recommendations);
    setReport(reportData.report);
    setAiReport(reportData.ai_report);
    setRecommendations(reportData.recommendations || []);
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
      <h3>🤖 AI Executive Summary</h3>
<pre style={{ whiteSpace: "pre-wrap", background: "#f5f5f5", padding: "10px" }}>
  {aiReport}
</pre>

      <Recommendations items={recommendations}/>
      <ReportView report={report} />
    </div>
  );
}

export default App;
