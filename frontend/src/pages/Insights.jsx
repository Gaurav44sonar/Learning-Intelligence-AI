import { useEffect, useState } from "react";
import InsightSummary from "../components/InsightSummary";
import CompletionChart from "../components/CompletionChart";
import RiskChart from "../components/RiskChart";
import ChapterDifficultyChart from "../components/ChapterDifficultyChart";
import EngagementScatter from "../components/EngagementScatter";

export default function Insights() {
  const [data, setData] = useState(null);
  

  useEffect(() => {
    const stored = sessionStorage.getItem("analysisData");
    if (stored) {
      setData(JSON.parse(stored));
    }
  }, []);

  if (!data) {
    return (
      <div className="min-h-screen flex items-center justify-center text-gray-500">
        No insights found. Please upload a CSV first.
      </div>
    );
  }

  return (
    <div className="bg-gray-50 min-h-screen px-6 py-10 space-y-12 max-w-7xl mx-auto">

      {/* AI SUMMARY */}
      <InsightSummary summary={data.summary} />

      {/* CHARTS */}
      <div className="grid grid-cols-1 md:grid-cols-2 gap-10">
        <CompletionChart students={data.student_predictions} />
        <RiskChart insights={data.structured_insights} />
        <ChapterDifficultyChart chapters={data.chapter_difficulty} />
        <EngagementScatter students={data.student_predictions} />
      </div>

    </div>
  );
}
