// import { BarChart, Bar, XAxis, Tooltip } from "recharts";


// export default function ChapterDifficultyChart({ chapters }) {
// const mapDifficulty = { LOW: 1, MEDIUM: 2, HIGH: 3 };


// const data = chapters.map((c) => ({
// chapter: `Ch ${c.chapter_order}`,
// difficulty: mapDifficulty[c.difficulty_level],
// }));


// return (
// <div className="bg-white p-6 rounded-xl shadow">
// <h2 className="font-semibold mb-4">Chapter Difficulty Index</h2>
// <BarChart width={300} height={250} data={data}>
// <XAxis dataKey="chapter" />
// <Bar dataKey="difficulty" fill="#10b981" />
// <Tooltip />
// </BarChart>
// </div>
// );
// }

import { BarChart, Bar, XAxis, Tooltip, ResponsiveContainer } from "recharts";

export default function ChapterDifficultyChart({ chapters }) {
  const difficultyMap = {
    LOW: 1,
    MEDIUM: 2,
    HIGH: 3,
  };

  const data = chapters.map((c) => ({
    chapter: `Chapter ${c.chapter_order}`,
    difficulty: difficultyMap[c.difficulty_level],
  }));

  return (
    <div className="bg-white rounded-2xl shadow-lg p-6 hover:shadow-xl transition">
      <h2 className="text-lg font-semibold mb-1">
        Chapter Difficulty Index
      </h2>
      <p className="text-sm text-gray-500 mb-6">
        Engagement & performance based difficulty
      </p>

      <ResponsiveContainer width="100%" height={260}>
        <BarChart data={data}>
          <XAxis dataKey="chapter" />
          <Tooltip />
          <Bar
            dataKey="difficulty"
            radius={[8, 8, 0, 0]}
            fill="#10b981"
          />
        </BarChart>
      </ResponsiveContainer>
    </div>
  );
}
