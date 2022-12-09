import SignIn from '@/pages/SignIn.vue';
import SignUp from '@/pages/SignUp.vue';
import NotFound from '@/pages/NotFound.vue';
import MainPage from '@/pages/MainPage.vue';
import Analytics from '@/pages/Analytics.vue';
import Settings from '@/pages/Settings.vue';
import { createRouter, createWebHistory } from 'vue-router';

const routes = [
    {
        path: '/',
        component: MainPage
    },
    {
        path: '/settings',
        component: Settings
    },
    {
        path: '/analytics',
        component: Analytics
    },
    {
        path: '/login',
        component: SignIn
    },
    {
        path: '/register',
        component: SignUp
    },
    {
        path: '/:pathMatch(.*)*',
        component: NotFound
    }
];

const router = createRouter({
    routes,
    history: createWebHistory(import.meta.env.BASE_URL)
});

export default router;
