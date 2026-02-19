import React from "react";

function MetricCard({ title, value }) {
  const isPositive = value > 0;
  const isNegative = value < 0;

  return (
    <div className="metric-card">
      <div className="metric-title">{title}</div>

      <div
        className={`metric-value ${
          isPositive ? "positive" : isNegative ? "negative" : ""
        }`}
      >
        {value !== undefined && value !== null
          ? `${value.toFixed(2)}%`
          : "N/A"}
      </div>
    </div>
  );
}

export default function Dashboard({ metrics }) {
  if (!metrics) return null;

  // Get latest FY dynamically
  const latestYear =
    Object.keys(metrics.ebitda_margin || {})[0];

  return (
    <div className="dashboard">
      <h2 style={{ marginBottom: "20px" }}>
        Financial Dashboard — {latestYear}
      </h2>

      <div className="metric-grid">
        <MetricCard
          title="EBITDA Margin"
          value={metrics.ebitda_margin?.[latestYear]}
        />

        <MetricCard
          title="PAT Margin"
          value={metrics.pat_margin?.[latestYear]}
        />

        <MetricCard
          title="Revenue Growth"
          value={metrics.revenue_growth?.[latestYear]}
        />
      </div>
    </div>
  );
}
