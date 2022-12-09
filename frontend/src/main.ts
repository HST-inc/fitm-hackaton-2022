import { createApp } from 'vue';
import './style.css';
import App from '@/App.vue';

import Antd from 'ant-design-vue';
import 'ant-design-vue/dist/antd.css';

import components from '@/components';

import { VueQueryPlugin } from 'vue-query';
import router from './router/router';

const app = createApp(App);

components.forEach((component) => {
    app.component(component.name, component);
});

app.use(Antd).use(router).use(VueQueryPlugin).mount('#app');
