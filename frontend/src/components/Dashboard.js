function MetricCard({ title, value }) {

  const isPositive = value > 0;

  return (
    <div style={{
      padding: "20px",
      background: "#f4f6f8",
      borderRadius: "10px",
      width: "220px",
      boxShadow: "0 4px 12px rgba(0,0,0,0.05)"
    }}>
      <h4>{title}</h4>
      <h2 style={{ color: isPositive ? "green" : "red" }}>
        {value ? value.toFixed(2) + "%" : "N/A"}
      </h2>
    </div>
  );
}

export default function Dashboard({ metrics }) {

  if (!metrics) return null;

  const latest = Object.keys(metrics.ebitda_margin || {})[0];

  return (
    <div style={{ marginTop: "40px" }}>
      <h2>Financial Dashboard</h2>
      <div style={{ display: "flex", gap: "20px", flexWrap: "wrap" }}>

        <MetricCard
          title="EBITDA Margin"
          value={metrics.ebitda_margin?.[latest]}
        />

        <MetricCard
          title="PAT Margin"
          value={metrics.pat_margin?.[latest]}
        />

        <MetricCard
          title="Revenue Growth"
          value={metrics.revenue_growth?.[latest]}
        />

      </div>
    </div>
  );
}
