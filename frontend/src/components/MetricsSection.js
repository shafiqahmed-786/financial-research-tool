import React from "react";

function MetricsSection({ metrics }) {
  if (!metrics) return null;

  return (
    <div className="card">
      <h2>Financial Metrics</h2>

      <pre>{JSON.stringify(metrics, null, 2)}</pre>
    </div>
  );
}

export default MetricsSection;
