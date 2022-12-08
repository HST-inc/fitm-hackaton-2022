import axios from 'axios';

export const mainAxios = axios.create({
    baseURL: import.meta.env.BASE_URL,
}) 