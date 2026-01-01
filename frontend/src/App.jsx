// import { useState } from "react";
// import UploadCSV from "./components/UploadCSV";
// import CompletionChart from "./components/CompletionChart";
// import RiskChart from "./components/RiskChart";
// import ChapterDifficultyChart from "./components/ChapterDifficultyChart";
// import EngagementScatter from "./components/EngagementScatter";
// import Navbar from "./components/Navbar";
// import InsightSummary from "./components/InsightSummary";



// export default function App() {
//   const [data, setData] = useState(null);

//   return (
//     <>
//       <Navbar />

//       <div className="min-h-screen bg-gradient-to-br from-indigo-50 via-white to-purple-50 px-6">
        
//         {/* HERO SECTION */}
//         <section className="flex flex-col items-center text-center pt-12 pb-20">
//           <span className="mb-5 inline-flex items-center gap-2 px-4 py-1 rounded-full bg-indigo-100 text-indigo-600 text-sm">
//             ⚡ Powered by Advanced AI
//           </span>

//           <h1 className="text-5xl md:text-6xl font-extrabold mb-6">
//             Learning<span className="text-indigo-600">Intelligence</span> AI
//           </h1>

//           <p className="text-gray-600 max-w-2xl text-lg mb-10">
//             Monitor learner engagement, predict course completion, detect high-risk
//             students, and identify difficult chapters using AI-driven insights.
//           </p>

//           {/* Upload Section */}
//           <UploadCSV onResult={setData} />
//         </section>

//             {/* AI INSIGHTS */}




//         {/* DASHBOARD */}
//      {data && (
//   <section className="max-w-7xl mx-auto pb-20 space-y-12">

//     {/* AI INSIGHTS */}
//     {data && data.summary && (
//   <InsightSummary summary={data.summary} />
// )}


//     {/* CHARTS */}
//     <div className="grid grid-cols-1 md:grid-cols-2 gap-10">
//       <CompletionChart students={data.student_predictions} />
//       <RiskChart insights={data.structured_insights} />
//       <ChapterDifficultyChart chapters={data.chapter_difficulty} />
//       <EngagementScatter students={data.student_predictions} />
//     </div>

//   </section>
// )}
//       </div>
//     </>
//   );
// }


import { Routes, Route } from "react-router-dom";
import Navbar from "./components/Navbar";
import Home from "./pages/Home";
import Insights from "./pages/Insights";

export default function App() {
  return (
    <>
      <Navbar />
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/insights" element={<Insights />} />
      </Routes>
    </>
  );
}
