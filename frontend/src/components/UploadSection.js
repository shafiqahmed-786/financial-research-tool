import React, { useState } from "react";
import { uploadFile, extractData } from "../api/api";

function UploadSection({ setResult, setFileId }) {
  const [file, setFile] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");

  const handleUpload = async () => {
    if (!file) return;

    try {
      setLoading(true);
      setError("");

      const uploadRes = await uploadFile(file);
      const id = uploadRes.data.file_id;

      setFileId(id);

      const extractRes = await extractData(id);
      setResult(extractRes.data);
    } catch (err) {
      setError("Upload or extraction failed.");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="card">
      <h2>Upload Financial Statement</h2>

      <input
        type="file"
        accept="application/pdf"
        onChange={(e) => setFile(e.target.files[0])}
      />

      <button onClick={handleUpload} disabled={loading}>
        {loading ? "Processing..." : "Upload & Analyze"}
      </button>

      {error && <p className="error">{error}</p>}
    </div>
  );
}

export default UploadSection;
