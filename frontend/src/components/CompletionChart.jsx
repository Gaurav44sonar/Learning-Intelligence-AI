// import { PieChart, Pie, Cell, Tooltip } from "recharts";


// export default function CompletionChart({ students }) {
// const completed = students.filter((s) => s.prediction === 1).length;
// const notCompleted = students.length - completed;


// const data = [
// { name: "Completed", value: completed },
// { name: "Not Completed", value: notCompleted },
// ];


// const COLORS = ["#4f46e5", "#e11d48"];


// return (
// <div className="bg-white p-6 rounded-xl shadow">
// <h2 className="font-semibold mb-4">Course Completion Prediction</h2>
// <PieChart width={300} height={250}>
// <Pie data={data} dataKey="value" cx="50%" cy="50%" outerRadius={80}>
// {data.map((_, i) => (
// <Cell key={i} fill={COLORS[i]} />
// ))}
// </Pie>
// <Tooltip />
// </PieChart>
// </div>
// );
// }

import { PieChart, Pie, Cell, Tooltip, Legend } from "recharts";

export default function CompletionChart({ students }) {
  const completed = students.filter((s) => s.prediction === 1).length;
  const notCompleted = students.length - completed;

  const data = [
    { name: "Completed", value: completed },
    { name: "Not Completed", value: notCompleted },
  ];

  const COLORS = ["#6366f1", "#ef4444"];

  return (
    <div className="bg-white rounded-2xl shadow-lg p-6 hover:shadow-xl transition">
      <h2 className="text-lg font-semibold mb-1">
        Course Completion Prediction
      </h2>
      <p className="text-sm text-gray-500 mb-6">
        AI-based completion outcome distribution
      </p>

      <div className="flex justify-center">
        <PieChart width={280} height={260}>
          <Pie
            data={data}
            dataKey="value"
            innerRadius={60}
            outerRadius={90}
            paddingAngle={4}
          >
            {data.map((_, i) => (
              <Cell key={i} fill={COLORS[i]} />
            ))}
          </Pie>
          <Tooltip />
          <Legend />
        </PieChart>
      </div>
    </div>
  );
}
