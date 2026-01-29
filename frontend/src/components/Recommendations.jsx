function Recommendations({ items }) {
  if (!items || items.length === 0) return null;

  return (
    <div style={{ marginTop: "20px" }}>
      <h3>🛠️ Recommended Actions</h3>
      <ul>
        {items.map((rec, index) => (
          <li key={index}>{rec}</li>
        ))}
      </ul>
    </div>
  );
}

export default Recommendations;
