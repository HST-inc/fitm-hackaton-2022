<template lang="">
    <a-layout style="min-height: 100vh">
        <Slider></Slider>
        <a-layout>
            <a-layout-header style="background: #fff; padding: 0" />
            <a-layout-content style="margin: 0 16px">
                <a-breadcrumb style="margin: 16px 0">
                    <a-breadcrumb-item>User</a-breadcrumb-item>
                    <a-breadcrumb-item>Bill</a-breadcrumb-item>
                </a-breadcrumb>
                <slot></slot>
            </a-layout-content>
            <a-layout-footer style="text-align: center">
                Ant Design ©2018 Created by Ant UED
            </a-layout-footer>
        </a-layout></a-layout
    >
</template>
<script setup lang="ts">
import Slider from '@/components/Slider.vue';
</script>
<style lang="scss" scoped></style>
