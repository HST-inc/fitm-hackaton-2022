<template>
    <a-layout-sider v-model:collapsed="collapsed" collapsible>
        <div class="logo"></div>
        <a-menu v-model:selectedKeys="selectedKeys" theme="dark" mode="inline">
            <router-link to="/settings">
                <a-menu-item key="settings">
                    <desktop-outlined />
                    <span>Настройки</span>
                </a-menu-item>
            </router-link>
            <router-link to="/analytics">
                <a-menu-item key="2">
                    <pie-chart-outlined />
                    <span>Аналитика</span>
                </a-menu-item>
            </router-link>
            <a-sub-menu key="sub1">
                <template #title>
                    <span>
                        <user-outlined />
                        <span>User</span>
                    </span>
                </template>
                <a-menu-item key="3">Tom</a-menu-item>
                <a-menu-item key="4">Bill</a-menu-item>
                <a-menu-item key="5">Alex</a-menu-item>
            </a-sub-menu>
            <a-sub-menu key="sub2">
                <template #title>
                    <span>
                        <team-outlined />
                        <span>Team</span>
                    </span>
                </template>
                <a-menu-item key="6">Team 1</a-menu-item>
                <a-menu-item key="8">Team 2</a-menu-item>
            </a-sub-menu>
            <a-menu-item key="9">
                <file-outlined />
                <span>File</span>
            </a-menu-item>
        </a-menu>
    </a-layout-sider>
</template>
<script lang="ts" setup>
import {
    PieChartOutlined,
    DesktopOutlined,
    UserOutlined,
    TeamOutlined,
    FileOutlined
} from '@ant-design/icons-vue';
import { ref } from 'vue';
import { RouterLink, useRouter } from 'vue-router';
const collapsed = ref<boolean>(false);
const selectedKeys = ref<string[]>(['settings']);
</script>
<style scoped lang="scss">
.logo {
    height: 32px;
    margin: 16px;
    background: rgba(255, 255, 255, 0.3);
}

.site-layout .site-layout-background {
    background: #fff;
}
[data-theme='dark'] .site-layout .site-layout-background {
    background: #141414;
}
</style>
