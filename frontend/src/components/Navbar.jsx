import { BarChart3, UploadCloud, Home } from "lucide-react";

export default function Navbar() {
  return (
    <nav className="sticky top-0 z-50 bg-white/80 backdrop-blur border-b">
      <div className="max-w-7xl mx-auto px-6 py-4 flex items-center justify-between">
        
        {/* LOGO */}
        <div className="flex items-center gap-2">
          <div className="w-9 h-9 flex items-center justify-center rounded-xl
                          bg-gradient-to-br from-indigo-500 to-purple-500 text-white">
            <BarChart3 size={18} />
          </div>
          <span className="font-bold text-lg text-gray-900">
            Learning<span className="text-indigo-600">AI</span>
          </span>
        </div>

        {/* MENU */}
        <div className="flex items-center gap-3">
          <NavItem icon={<Home size={16} />} label="Dashboard" active />
          <NavItem icon={<UploadCloud size={16} />} label="Upload" />
        </div>
      </div>
    </nav>
  );
}

/* NAV ITEM */
function NavItem({ icon, label, active }) {
  return (
    <button
      className={`flex items-center gap-2 px-4 py-2 rounded-xl text-sm font-medium
        ${
          active
            ? "bg-indigo-600 text-white shadow"
            : "text-gray-600 hover:bg-gray-100"
        }`}
    >
      {icon}
      {label}
    </button>
  );
}
