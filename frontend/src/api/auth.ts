import { ISignIn, ISignUp } from '@/models/auth';
import { mainAxios } from './axios';

export const signIn = ({ login, password, remember }: ISignIn) =>
    mainAxios.post('/auth/signin', { login, password, remember });

export const signUp = (signUpUserInfo: ISignUp) => mainAxios.post('/auth/signup', signUpUserInfo);
