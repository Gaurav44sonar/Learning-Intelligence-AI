import { useNavigate } from "react-router-dom";
import { useState } from "react";
import UploadCSV from "../components/UploadCSV";

export default function Home() {
  const navigate = useNavigate();
  const [loading, setLoading] = useState(false);

  const handleResult = (data) => {
    // store data temporarily
    sessionStorage.setItem("analysisData", JSON.stringify(data));
    navigate("/insights");
  };

  return (
    <div className="min-h-screen bg-gradient-to-br from-indigo-50 via-white to-purple-50 px-6">
      <section className="flex flex-col items-center text-center pt-16">
        <h1 className="text-5xl font-extrabold mb-6">
          Learning<span className="text-indigo-600">Intelligence</span> AI
        </h1>

        <p className="text-gray-600 max-w-2xl text-lg mb-10">
          Upload learner data to generate AI-powered insights.
        </p>

        <UploadCSV onResult={handleResult} />
      </section>
    </div>
  );
}
