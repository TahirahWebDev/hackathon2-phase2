import React, { useState } from 'react';
import { useRouter } from 'next/router';
import Link from 'next/link';
import { useAuth } from '../services/auth';
import { Mail, Lock, CheckCircle2, ArrowRight } from 'lucide-react';

interface AuthFormProps {
  isSignup?: boolean;
}

const AuthForm: React.FC<AuthFormProps> = ({ isSignup = false }) => {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [confirmPassword, setConfirmPassword] = useState('');
  const [error, setError] = useState('');
  const [isLoading, setIsLoading] = useState(false);
  const router = useRouter();
  const { signin, signup } = useAuth();

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    setIsLoading(true);
    setError('');
    
    if (isSignup) {
      if (password !== confirmPassword) {
        setError('Passwords do not match');
        setIsLoading(false);
        return;
      }

      try {
        await signup(email, password);
        router.push('/signin');
      } catch (err) {
        setError('Signup failed. Email may already be in use.');
      } finally {
        setIsLoading(false);
      }
    } else {
      try {
        await signin(email, password);
        router.push('/dashboard');
      } catch (err) {
        setError('Invalid email or password. Please try again.');
      } finally {
        setIsLoading(false);
      }
    }
  };

  return (
    /* Change: Removed the gradient and min-h-screen from here.
       Added 'py-20' to give it space from the top and bottom.
    */
    <div className="flex items-center justify-center py-20 px-4 sm:px-6 lg:px-8 bg-transparent">
      <div className="max-w-md w-full space-y-8 bg-white/95 backdrop-blur-sm p-10 rounded-3xl shadow-2xl border border-white/20">
        <div className="text-center">
          <div className="mx-auto h-12 w-12 bg-indigo-600 rounded-xl flex items-center justify-center shadow-lg mb-4">
            <CheckCircle2 className="text-white h-8 w-8" />
          </div>
          <h2 className="text-3xl font-extrabold text-gray-900 tracking-tight">
            {isSignup ? 'Create Account' : 'Welcome Back'}
          </h2>
          <p className="mt-2 text-sm text-gray-600 font-medium">
            {isSignup ? 'Join us and start managing tasks' : 'Please enter your details'}
          </p>
        </div>

        <form className="mt-8 space-y-6" onSubmit={handleSubmit}>
          {error && (
            <div className="rounded-xl bg-red-50 border border-red-200 p-4 animate-pulse">
              <div className="text-sm text-red-700 font-bold">{error}</div>
            </div>
          )}
          
          <div className="space-y-5">
            <div className="relative">
              <label className="text-[10px] font-black text-indigo-600 uppercase tracking-[0.2em] ml-1">Email Address</label>
              <div className="mt-1 relative rounded-md shadow-sm">
                <div className="absolute inset-y-0 left-0 pl-3 flex items-center pointer-events-none">
                  <Mail className="h-5 w-5 text-gray-400" />
                </div>
                <input
                  type="email"
                  required
                  className="block w-full pl-10 pr-3 py-3 border border-gray-200 rounded-xl leading-5 bg-white placeholder-gray-400 focus:outline-none focus:ring-2 focus:ring-indigo-500 transition duration-150 sm:text-sm"
                  placeholder="name@example.com"
                  value={email}
                  onChange={(e) => setEmail(e.target.value)}
                />
              </div>
            </div>

            <div className="relative">
              <label className="text-[10px] font-black text-indigo-600 uppercase tracking-[0.2em] ml-1">Password</label>
              <div className="mt-1 relative rounded-md shadow-sm">
                <div className="absolute inset-y-0 left-0 pl-3 flex items-center pointer-events-none">
                  <Lock className="h-5 w-5 text-gray-400" />
                </div>
                <input
                  type="password"
                  required
                  className="block w-full pl-10 pr-3 py-3 border border-gray-200 rounded-xl leading-5 bg-white placeholder-gray-400 focus:outline-none focus:ring-2 focus:ring-indigo-500 transition duration-150 sm:text-sm"
                  placeholder="••••••••"
                  value={password}
                  onChange={(e) => setPassword(e.target.value)}
                />
              </div>
            </div>

            {isSignup && (
              <div className="relative">
                <label className="text-[10px] font-black text-indigo-600 uppercase tracking-[0.2em] ml-1">Confirm Password</label>
                <div className="mt-1 relative rounded-md shadow-sm">
                  <div className="absolute inset-y-0 left-0 pl-3 flex items-center pointer-events-none">
                    <Lock className="h-5 w-5 text-gray-400" />
                  </div>
                  <input
                    type="password"
                    required
                    className="block w-full pl-10 pr-3 py-3 border border-gray-200 rounded-xl leading-5 bg-white placeholder-gray-400 focus:outline-none focus:ring-2 focus:ring-indigo-500 transition duration-150 sm:text-sm"
                    placeholder="••••••••"
                    value={confirmPassword}
                    onChange={(e) => setConfirmPassword(e.target.value)}
                  />
                </div>
              </div>
            )}
          </div>

          <div>
            <button
              type="submit"
              disabled={isLoading}
              className="group relative w-full flex justify-center py-3.5 px-4 border border-transparent text-sm font-black uppercase tracking-widest rounded-xl text-white bg-indigo-600 hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500 transition-all duration-200 transform hover:-translate-y-1 active:scale-95 disabled:opacity-50 shadow-xl shadow-indigo-200"
            >
              {isLoading ? (
                <span className="flex items-center">
                  <svg className="animate-spin -ml-1 mr-3 h-5 w-5 text-white" fill="none" viewBox="0 0 24 24">
                    <circle className="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" strokeWidth="4"></circle>
                    <path className="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path>
                  </svg>
                  Syncing...
                </span>
              ) : (
                <span className="flex items-center">
                  {isSignup ? 'Create Account' : 'Sign In'}
                  <ArrowRight className="ml-2 h-4 w-4 transition-transform group-hover:translate-x-1" />
                </span>
              )}
            </button>
          </div>
        </form>

        <div className="pt-6 border-t border-gray-100 text-center">
          <p className="text-sm text-gray-500 font-medium">
            {isSignup ? (
              <>
                Already have an account?{' '}
                <Link href="/signin" className="font-black text-indigo-600 hover:text-indigo-500 transition-all duration-150">
                  Sign In
                </Link>
              </>
            ) : (
              <>
                Don't have an account?{' '}
                <Link href="/signup" className="font-black text-indigo-600 hover:text-indigo-500 transition-all duration-150">
                  Sign Up
                </Link>
              </>
            )}
          </p>
        </div>
      </div>
    </div>
  );
};

export default AuthForm;