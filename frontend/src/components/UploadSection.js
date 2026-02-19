import React, { useState } from "react";

const API_BASE = process.env.REACT_APP_API_BASE;

function UploadSection({ setResult, setFileId }) {
  const [file, setFile] = useState(null);
  const [error, setError] = useState(null);

  const handleUpload = async () => {
    if (!file) return;

    setError(null);

    const formData = new FormData();
    formData.append("file", file);

    try {
      // Upload file
      const uploadRes = await fetch(`${API_BASE}/upload`, {
        method: "POST",
        body: formData
      });

      const uploadData = await uploadRes.json();

      if (!uploadRes.ok) throw new Error("Upload failed");

      setFileId(uploadData.file_id);

      // Extract
      const extractRes = await fetch(
        `${API_BASE}/extract/${uploadData.file_id}`,
        { method: "POST" }
      );

      const extractData = await extractRes.json();

      if (!extractRes.ok) throw new Error("Extraction failed");

      setResult(extractData);

    } catch (err) {
      setError("Upload or extraction failed.");
    }
  };

  return (
    <div>
      <input
        type="file"
        accept="application/pdf"
        onChange={(e) => setFile(e.target.files[0])}
      />
      <button onClick={handleUpload}>Upload & Analyze</button>
      {error && <p style={{ color: "red" }}>{error}</p>}
    </div>
  );
}

export default UploadSection;
