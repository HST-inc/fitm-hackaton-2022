import axios from 'axios';

const defaultHeaders = {};

const defaultBodyHeaders = {
    ...defaultHeaders,
    'Content-Type': 'application/json'
};

const bearerTokenHeaders = {
    ...defaultBodyHeaders,
    Authorization: `Bearer ${localStorage.getItem('token')}`
};

export const mainAxios = axios.create({
    baseURL: import.meta.env.BASE_URL,
    headers: defaultBodyHeaders
});

export const tokenAxios = axios.create({
    baseURL: import.meta.env.BASE_URL,
    headers: bearerTokenHeaders
});

export const tokenAxiosWithInterceptor = axios
    .create({
        baseURL: import.meta.env.BASE_URL,
        headers: bearerTokenHeaders
    })
    .interceptors.response.use((response) => {
        console.log(response.headers);
        return response;
    });
