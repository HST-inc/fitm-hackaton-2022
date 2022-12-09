import { User } from './user';

export type ISignIn = {
    login: string;
    password: string;
    remember: boolean;
};

export type ISignUp = User;
