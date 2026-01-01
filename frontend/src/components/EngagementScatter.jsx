// import { ScatterChart, Scatter, XAxis, YAxis, Tooltip } from "recharts";


// export default function EngagementScatter({ students }) {
// const data = students.map((s) => ({
// time: s.avg_time_spent,
// score: s.avg_score,
// }));


// return (
// <div className="bg-white p-6 rounded-xl shadow">
// <h2 className="font-semibold mb-4">Engagement vs Performance</h2>
// <ScatterChart width={300} height={250}>
// <XAxis dataKey="time" name="Avg Time" />
// <YAxis dataKey="score" name="Avg Score" />
// <Scatter data={data} fill="#6366f1" />
// <Tooltip />
// </ScatterChart>
// </div>
// );
// }

import {
  ScatterChart,
  Scatter,
  XAxis,
  YAxis,
  Tooltip,
  ResponsiveContainer,
} from "recharts";

export default function EngagementScatter({ students }) {
  const data = students.map((s) => ({
    time: s.avg_time_spent,
    score: s.avg_score,
  }));

  return (
    <div className="bg-white rounded-2xl shadow-lg p-6 hover:shadow-xl transition">
      <h2 className="text-lg font-semibold mb-1">
        Engagement vs Performance
      </h2>
      <p className="text-sm text-gray-500 mb-6">
        Relationship between time spent and scores
      </p>

      <ResponsiveContainer width="100%" height={260}>
        <ScatterChart>
          <XAxis
            dataKey="time"
            name="Avg Time Spent"
            unit="min"
          />
          <YAxis
            dataKey="score"
            name="Avg Score"
          />
          <Tooltip />
          <Scatter data={data} fill="#6366f1" />
        </ScatterChart>
      </ResponsiveContainer>
    </div>
  );
}
