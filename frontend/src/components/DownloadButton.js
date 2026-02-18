import React from "react";
import { downloadExcel } from "../api/api";

function DownloadButton({ fileId }) {
  if (!fileId) return null;

  return (
    <div className="card">
      <a
        href={downloadExcel(fileId)}
        target="_blank"
        rel="noopener noreferrer"
      >
        <button>Download Excel</button>
      </a>
    </div>
  );
}

export default DownloadButton;
