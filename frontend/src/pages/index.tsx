import { useEffect } from 'react';
import { useRouter } from 'next/router';
import { useAuth } from '../services/auth';
import { Loader2, Sparkles } from 'lucide-react';

const IndexPage: React.FC = () => {
  const router = useRouter();
  const { loading, isAuthenticated } = useAuth();

  useEffect(() => {
    if (!loading) {
      if (isAuthenticated()) {
        router.push('/dashboard');
      } else {
        router.push('/signin');
      }
    }
  }, [isAuthenticated, loading, router]);

  return (
    <div className="min-h-screen flex flex-col items-center justify-center bg-slate-50 relative overflow-hidden">
      {/* Background Decorative Elements */}
      <div className="absolute top-[-10%] left-[-10%] w-72 h-72 bg-indigo-100 rounded-full blur-3xl opacity-50 animate-pulse"></div>
      <div className="absolute bottom-[-10%] right-[-10%] w-72 h-72 bg-purple-100 rounded-full blur-3xl opacity-50 animate-pulse delay-700"></div>

      <div className="relative z-10 flex flex-col items-center space-y-6">
        {/* Animated Loading Icon */}
        <div className="relative">
          <Loader2 className="h-12 w-12 text-indigo-600 animate-spin" />
          <Sparkles className="h-5 w-5 text-purple-400 absolute -top-2 -right-2 animate-bounce" />
        </div>

        <div className="text-center">
          <h2 className="text-xl font-black text-slate-800 tracking-tight">
            Syncing FocusFlow
          </h2>
          <p className="mt-2 text-sm font-bold text-slate-400 uppercase tracking-[0.2em]">
            Checking credentials...
          </p>
        </div>
      </div>
    </div>
  );
};

export default IndexPage;