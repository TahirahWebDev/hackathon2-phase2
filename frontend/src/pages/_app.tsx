import '../styles/globals.css';
import React from 'react';
import type { AppProps } from 'next/app';
import { AuthProvider } from '../services/auth';

const MyApp: React.FC<AppProps> = ({ Component, pageProps }) => {
  return (
    <AuthProvider>
      {/* Tailwind Global Wrapper:
        - min-h-screen: Ensures the background covers the full page height.
        - bg-slate-50: A clean, off-white background.
        - font-sans: Uses the standard system sans-serif stack.
        - selection: Customizes the highlight color for the whole app.
      */}
      <div className="min-h-screen bg-slate-50 text-slate-900 antialiased selection:bg-indigo-100 selection:text-indigo-700">
        
        {/* Main Content Area */}
        <main className="relative">
          <Component {...pageProps} />
        </main>

        {/* Minimalist Tailwind Footer */}
        <footer className="py-10 flex flex-col items-center justify-center space-y-2">
          <div className="h-px w-16 bg-slate-200 mb-2"></div>
          <p className="text-[10px] font-black uppercase tracking-[0.3em] text-slate-400">
            FocusFlow Task Manager
          </p>
          <p className="text-[9px] text-slate-300 font-medium">
            GIAIC Q4 • Phase II Persistence
          </p>
        </footer>
      </div>
    </AuthProvider>
  );
};

export default MyApp;