import { Sparkles, AlertTriangle, BookOpen, CheckCircle } from "lucide-react";

export default function InsightSummary({ summary }) {
  if (!summary) return null;

  // Break summary into clean lines
  const lines = summary
    .split("\n")
    .map((l) => l.trim())
    .filter(Boolean);

  return (
    <div className="bg-white rounded-2xl shadow-lg p-8 space-y-8 hover:shadow-xl transition">

      {/* HEADER */}
      <div className="flex items-center gap-3">
        <div className="w-11 h-11 rounded-xl bg-indigo-100 flex items-center justify-center">
          <Sparkles className="text-indigo-600" size={22} />
        </div>
        <div>
          <h2 className="text-2xl font-semibold">AI-Generated Insights</h2>
          <p className="text-sm text-gray-500">
            Automatically summarized learning analytics & recommendations
          </p>
        </div>
      </div>

      {/* CONTENT */}
      <div className="space-y-6 leading-relaxed text-gray-700">
        {lines.map((line, idx) => {
          /* SECTION HEADERS */
          if (line.startsWith("**1.") || line.startsWith("**2.")) {
            return (
              <SectionTitle key={idx} text={strip(line)} />
            );
          }

          /* SUB-HEADINGS */
          if (
            line.toLowerCase().includes("observation") ||
            line.toLowerCase().includes("key factors") ||
            line.toLowerCase().includes("mentor recommendations")
          ) {
            return (
              <SubTitle key={idx} text={strip(line)} />
            );
          }

          /* BULLET POINTS */
          if (line.startsWith("*") || line.startsWith("-")) {
            return (
              <li
                key={idx}
                className="flex gap-2 items-start bg-gray-50 rounded-lg p-3"
              >
                <CheckCircle
                  size={18}
                  className="text-indigo-500 mt-1 shrink-0"
                />
                <span>{strip(line)}</span>
              </li>
            );
          }

          /* NORMAL TEXT */
          return (
            <p key={idx} className="pl-1">
              {strip(line)}
            </p>
          );
        })}
      </div>
    </div>
  );
}

/* UTIL */
function strip(text) {
  return text.replace(/\*\*/g, "").replace(/^[-*]\s*/, "");
}

/* SECTION TITLE */
function SectionTitle({ text }) {
  const icon =
    text.toLowerCase().includes("risk") ? (
      <AlertTriangle className="text-red-500" size={20} />
    ) : (
      <BookOpen className="text-indigo-600" size={20} />
    );

  return (
    <div className="flex items-center gap-2 mt-6">
      {icon}
      <h3 className="text-xl font-semibold text-gray-900">{text}</h3>
    </div>
  );
}

/* SUBTITLE */
function SubTitle({ text }) {
  return (
    <p className="font-semibold text-gray-900 mt-4">
      {text}
    </p>
  );
}
