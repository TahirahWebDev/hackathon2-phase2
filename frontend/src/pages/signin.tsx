// frontend/src/pages/signin.tsx
import React from 'react';
import AuthForm from '../components/AuthForm';

const SigninPage: React.FC = () => {
  return <AuthForm isSignup={false} />;
};

export default SigninPage;