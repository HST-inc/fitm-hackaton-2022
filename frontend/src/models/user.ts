export type Sex = 'male' | 'female';

export type Passport = {
    series: string;
    number: string;
};

export type User = {
    login: string;
    password: string;
    name: string;
    secondName: string;
    patronymic: string;
    birthday: string;
    sex: Sex;
    phone: string;
    snils: string;
    passport: Passport;
};
