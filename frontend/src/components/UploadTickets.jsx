function UploadTickets() {
  const handleUpload = async (e) => {
    const file = e.target.files[0];
    if (!file) return;

    const formData = new FormData();
    formData.append("file", file);

    await fetch("http://127.0.0.1:5000/upload-tickets", {
      method: "POST",
      body: formData,
    });

    alert("Tickets uploaded!");
  };

  return (
    <div style={{ marginBottom: "10px" }}>
      <input type="file" accept=".csv" onChange={handleUpload} />
    </div>
  );
}

export default UploadTickets;
