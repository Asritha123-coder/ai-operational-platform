function DepartmentBreakdown({ data }) {
  if (!data || Object.keys(data).length === 0) return null;

  return (
    <div style={{ marginTop: "20px" }}>
      <h3>🏢 Department-wise Issues</h3>

      <table border="1" cellPadding="8">
        <thead>
          <tr>
            <th>Department</th>
            <th>Issue Count</th>
          </tr>
        </thead>
        <tbody>
          {Object.entries(data).map(([dept, count]) => (
            <tr key={dept}>
              <td>{dept}</td>
              <td>{count}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}

export default DepartmentBreakdown;
