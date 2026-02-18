import React from "react";

function ResultsTable({ data }) {
  if (!data) return null;

  const { periods, income_statement } = data;

  return (
    <div className="card">
      <h2>Income Statement</h2>

      <table>
        <thead>
          <tr>
            <th>Line Item</th>
            {periods.map((period) => (
              <th key={period}>{period}</th>
            ))}
          </tr>
        </thead>
        <tbody>
          {income_statement.map((row, index) => (
            <tr key={index}>
              <td>{row.line_item}</td>
              {periods.map((period) => (
                <td key={period}>
                  {row[period] !== undefined
                    ? row[period].toLocaleString()
                    : "-"}
                </td>
              ))}
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}

export default ResultsTable;
