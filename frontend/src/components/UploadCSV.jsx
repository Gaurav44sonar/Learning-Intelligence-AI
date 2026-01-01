// import { useState } from "react";
// import { uploadCSV } from "../api";


// export default function UploadCSV({ onResult }) {
// const [file, setFile] = useState(null);
// const [loading, setLoading] = useState(false);


// const handleUpload = async () => {
// if (!file) return;
// setLoading(true);
// const res = await uploadCSV(file);
// onResult(res.data);
// setLoading(false);
// };


// return (
// <div className="bg-white p-6 rounded-xl shadow">
// <input type="file" accept=".csv" onChange={(e) => setFile(e.target.files[0])} />
// <button
// onClick={handleUpload}
// className="ml-4 px-4 py-2 bg-indigo-600 text-white rounded"
// >
// {loading ? "Processing..." : "Upload CSV"}
// </button>
// </div>
// );
// }

// import { useState } from "react";
// import { uploadCSV } from "../api";
// import { UploadCloud } from "lucide-react";

// export default function UploadCSV({ onResult }) {
//   const [file, setFile] = useState(null);
//   const [loading, setLoading] = useState(false);

//   const handleUpload = async () => {
//     if (!file) return;
//     setLoading(true);
//     const res = await uploadCSV(file);
//     onResult(res.data);
//     setLoading(false);
//   };

//   return (
//     <div className="bg-white rounded-2xl shadow-lg p-8 flex flex-col md:flex-row items-center justify-between gap-6">
//       <div>
//         <h3 className="text-lg font-semibold text-gray-900">
//           Upload Learner Dataset
//         </h3>
//         <p className="text-sm text-gray-500 mt-1">
//           Upload CSV to generate AI-powered insights instantly
//         </p>
//       </div>

//       <div className="flex items-center gap-4">
//         <input
//           type="file"
//           accept=".csv"
//           onChange={(e) => setFile(e.target.files[0])}
//           className="text-sm"
//         />

//         <button
//           onClick={handleUpload}
//           disabled={loading}
//           className="flex items-center gap-2 px-6 py-2
//                      bg-gradient-to-r from-indigo-500 to-purple-500
//                      text-white rounded-xl font-medium
//                      hover:opacity-90 transition"
//         >
//           <UploadCloud size={18} />
//           {loading ? "Analyzing..." : "Upload & Analyze"}
//         </button>
//       </div>
//     </div>
//   );
// }


import { useState, useRef } from "react";
import { uploadCSV } from "../api";
import { UploadCloud } from "lucide-react";

export default function UploadCSV({ onResult }) {
  const [file, setFile] = useState(null);
  const [loading, setLoading] = useState(false);
  const [dragActive, setDragActive] = useState(false);
  const inputRef = useRef(null);

  const handleUpload = async () => {
    if (!file) return;
    setLoading(true);
    const res = await uploadCSV(file);
    onResult(res.data);
    setLoading(false);
  };

  const handleDrop = (e) => {
    e.preventDefault();
    setDragActive(false);
    if (e.dataTransfer.files && e.dataTransfer.files[0]) {
      setFile(e.dataTransfer.files[0]);
    }
  };

  return (
    <div
      onDragOver={(e) => {
        e.preventDefault();
        setDragActive(true);
      }}
      onDragLeave={() => setDragActive(false)}
      onDrop={handleDrop}
      onClick={() => inputRef.current.click()}
      className={`w-full max-w-3xl cursor-pointer rounded-2xl border-2 border-dashed
        ${
          dragActive
            ? "border-indigo-500 bg-indigo-50"
            : "border-gray-300 bg-white"
        }
        shadow-lg px-10 py-12 transition`}
    >
      <input
        ref={inputRef}
        type="file"
        accept=".csv"
        className="hidden"
        onChange={(e) => setFile(e.target.files[0])}
      />

      <div className="flex flex-col items-center text-center">
        <UploadCloud className="text-indigo-600 mb-4" size={40} />

        <h3 className="text-lg font-semibold mb-1">
          {file ? file.name : "Upload Learner Dataset"}
        </h3>

        <p className="text-sm text-gray-500 mb-6">
          Drag & drop CSV here, or click to browse
        </p>

        <button
          onClick={(e) => {
            e.stopPropagation();
            handleUpload();
          }}
          disabled={!file || loading}
          className="px-8 py-3 rounded-xl bg-gradient-to-r from-indigo-500 to-purple-500
                     text-white font-medium hover:opacity-90 transition"
        >
          {loading ? "Analyzing..." : "Upload & Analyze"}
        </button>
      </div>
    </div>
  );
}
