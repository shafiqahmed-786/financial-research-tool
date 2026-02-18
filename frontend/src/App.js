import React, { useState } from "react";
import UploadSection from "./components/UploadSection";
import ResultsTable from "./components/ResultsTable";
import MetricsSection from "./components/MetricsSection";
import DownloadButton from "./components/DownloadButton";
import Dashboard from "./components/Dashboard";
import "./styles/main.css";

function App() {
  const [result, setResult] = useState(null);
  const [fileId, setFileId] = useState(null);

  return (
    <div className="container">
      <h1>Financial Research Tool</h1>

      <UploadSection setResult={setResult} setFileId={setFileId} />

      {result && (
        <>
          <Dashboard metrics={result.metrics} />
          <ResultsTable data={result} />
          <MetricsSection metrics={result.metrics} />
          <DownloadButton fileId={fileId} />
        </>
      )}
    </div>
  );
}

export default App;
