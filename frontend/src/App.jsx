import { useState } from "react";
import { generateReport } from "./api/reportApi";
import ReportView from "./components/ReportView";

function App() {
  const [report, setReport] = useState("");

  const handleClick = async () => {
    const data = await generateReport();
    setReport(data.report);
  };

  return (
    <div style={{ padding: "20px" }}>
      <h2>AI Ops Report Generator</h2>
      <button onClick={handleClick}>Generate Report</button>
      <ReportView report={report} />
    </div>
  );
}

export default App;
