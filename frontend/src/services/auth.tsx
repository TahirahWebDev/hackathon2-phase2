// frontend/src/services/auth.ts
import { useState, useEffect, createContext, useContext } from 'react';
import api, { User, TokenResponse } from './api';

interface AuthContextType {
  user: User | null;
  token: string | null;
  loading: boolean;
  signin: (email: string, password: string) => Promise<TokenResponse>;
  signup: (email: string, password: string) => Promise<User>;
  signout: () => Promise<void>;
  isAuthenticated: () => boolean;
}

const AuthContext = createContext<AuthContextType | undefined>(undefined);

interface AuthProviderProps {
  children: React.ReactNode;
}

export const AuthProvider: React.FC<AuthProviderProps> = ({ children }) => {
  const [user, setUser] = useState<User | null>(null);
  const [token, setToken] = useState<string | null>(null);
  const [loading, setLoading] = useState<boolean>(true);

  useEffect(() => {
    // Check if user is already logged in on initial load
    const storedToken = localStorage.getItem('token');
    if (storedToken) {
      // In a real implementation, we'd verify the token is still valid
      // For now, we'll just set the token and assume it's valid
      api.setToken(storedToken);
      setToken(storedToken);
      // We would typically fetch user details here
      // setUser(storedUserDetails);
    }
    setLoading(false);
  }, []);

  const signin = async (email: string, password: string): Promise<TokenResponse> => {
    try {
      const response = await api.signin(email, password);
      const { access_token, user } = response;
      
      // Store token in local storage
      localStorage.setItem('token', access_token);
      
      // Update state
      setToken(access_token);
      setUser(user);
      
      return response;
    } catch (error) {
      console.error('Signin error:', error);
      throw error;
    }
  };

  const signup = async (email: string, password: string): Promise<User> => {
    try {
      const response = await api.signup(email, password);
      
      // For signup, we might want to automatically sign in the user
      // Or redirect to signin page
      setUser(response);
      
      return response;
    } catch (error) {
      console.error('Signup error:', error);
      throw error;
    }
  };

  const signout = async (): Promise<void> => {
    try {
      await api.signout();
      
      // Clear token from local storage
      localStorage.removeItem('token');
      
      // Update state
      setToken(null);
      setUser(null);
    } catch (error) {
      console.error('Signout error:', error);
      // Even if API signout fails, we should clear local state
      localStorage.removeItem('token');
      setToken(null);
      setUser(null);
    }
  };

  const isAuthenticated = (): boolean => {
    return !!token;
  };

  const value = {
    user,
    token,
    loading,
    signin,
    signup,
    signout,
    isAuthenticated,
  };

  return <AuthContext.Provider value={value}>{children}</AuthContext.Provider>;
};

export const useAuth = (): AuthContextType => {
  const context = useContext(AuthContext);
  if (context === undefined) {
    throw new Error('useAuth must be used within an AuthProvider');
  }
  return context;
};