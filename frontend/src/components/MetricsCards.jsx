function MetricsCards({ metrics }) {
  if (!metrics) return null;

  return (
    <div style={{ display: "flex", gap: "16px", marginTop: "20px" }}>
      <div style={cardStyle}>
        <h4>Total Incidents</h4>
        <p>{metrics.total_incidents}</p>
      </div>

      <div style={cardStyle}>
        <h4>Top Issue</h4>
        <p>{metrics.top_issue}</p>
      </div>

      <div style={cardStyle}>
        <h4>Root Cause</h4>
        <p>{metrics.top_root_cause}</p>
      </div>

      <div style={cardStyle}>
        <h4>Anomaly</h4>
        <p>{metrics.anomaly_detected ? "🚨 Yes" : "✅ No"}</p>
      </div>
    </div>
  );
}

const cardStyle = {
  border: "1px solid #ddd",
  padding: "12px",
  borderRadius: "8px",
  minWidth: "140px",
  textAlign: "center",
};

export default MetricsCards;
