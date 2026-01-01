// import { BarChart, Bar, XAxis, Tooltip } from "recharts";


// export default function RiskChart({ insights }) {
// const data = [
// { name: "High Risk", value: insights.high_risk_students_count },
// { name: "Others", value: insights.total_students - insights.high_risk_students_count },
// ];


// return (
// <div className="bg-white p-6 rounded-xl shadow">
// <h2 className="font-semibold mb-4">Student Risk Distribution</h2>
// <BarChart width={300} height={250} data={data}>
// <XAxis dataKey="name" />
// <Bar dataKey="value" fill="#f59e0b" />
// <Tooltip />
// </BarChart>
// </div>
// );
// }

import { BarChart, Bar, XAxis, Tooltip, ResponsiveContainer } from "recharts";

export default function RiskChart({ insights }) {
  const data = [
    {
      name: "High Risk",
      value: insights.high_risk_students_count,
    },
    {
      name: "Others",
      value:
        insights.total_students - insights.high_risk_students_count,
    },
  ];

  return (
    <div className="bg-white rounded-2xl shadow-lg p-6 hover:shadow-xl transition">
      <h2 className="text-lg font-semibold mb-1">
        Student Risk Distribution
      </h2>
      <p className="text-sm text-gray-500 mb-6">
        Early dropout risk detected by AI
      </p>

      <ResponsiveContainer width="100%" height={260}>
        <BarChart data={data}>
          <XAxis dataKey="name" />
          <Tooltip />
          <Bar
            dataKey="value"
            radius={[8, 8, 0, 0]}
            fill="#f59e0b"
          />
        </BarChart>
      </ResponsiveContainer>
    </div>
  );
}
