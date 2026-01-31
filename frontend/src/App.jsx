import { useState } from "react";
import { generateReport } from "./api/reportApi";
import { fetchMetrics } from "./api/metricsApi";
import ReportView from "./components/ReportView";
import MetricsCards from "./components/MetricsCards";
import UploadTickets from "./components/UploadTickets";
import Recommendations from "./components/Recommendations";
import DepartmentBreakdown from "./components/DepartmentBreakDown";



function App() {
  const [report, setReport] = useState("");
  const [metrics, setMetrics] = useState(null);
  const [recommendations, setRecommendations] = useState([]);
  const [aiReport, setAiReport] = useState("");
  const [departments,setDepartments] =useState("");
  const [riskScore, setRiskScore] = useState(null);
  const [priority, setPriority] = useState("");
  const [riskLevel, setRiskLevel] = useState("");
  const [aiReasoning, setAiReasoning] = useState("");



  const handleGenerate = async () => {
    const reportData = await generateReport();
    const metricsData = await fetchMetrics();
    //  console.log("RECOMMENDATIONS FROM API:", reportData.recommendations);
    setReport(reportData.report);
    setAiReport(reportData.ai_report);
    setRecommendations(reportData.recommendations || []);
    setMetrics(metricsData);
    setDepartments(reportData.department_breakdown || {});
    setRiskScore(reportData.risk_score);
    setRiskLevel(reportData.risk_level);
    setPriority(reportData.priority);
    setAiReasoning(reportData.ai_reasoning);

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
      <div style={{ marginTop: "20px", padding: "10px", border: "1px solid #ccc" }}>
  <h3>🚨 AI Risk Assessment</h3>

  {riskScore !== null && (
    <>
      <p><b>Risk Score:</b> {riskScore}</p>
      <p><b>Risk Level:</b> {riskLevel}</p>
      <p><b>Priority:</b> {priority}</p>
    </>
  )}
</div>

<div style={{ marginTop: "20px" }}>
  <h3>🧠 AI Reasoning</h3>
  <pre style={{ whiteSpace: "pre-wrap" }}>
    {aiReasoning}
  </pre>
</div>

      <DepartmentBreakdown data={departments}/>

      <Recommendations items={recommendations}/>
      <ReportView report={report} />
      {/* <h3>🚨 AI Risk Assessment</h3>
      <p><b>Risk Score:</b> {riskScore}</p>
      <p><b>Priority:</b> {priority}</p>

      <h3>🧠 AI Reasoning</h3>
      <pre>{aiReasoning}</pre> */}

    </div>
  );
}

export default App;
