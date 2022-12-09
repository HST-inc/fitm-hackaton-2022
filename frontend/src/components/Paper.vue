<template>
    <div class="paper">
        <slot></slot>
    </div>
</template>

<script setup lang="ts">
const props = defineProps({
    padding: {
        type: String,
        default: '20px'
    }
});
const padding = props.padding;
</script>

<style land="scss" scoped>
.paper {
    border: 1px solid rgba(0, 0, 0, 0.25);
    box-shadow: 0 0 5px rgba(0, 0, 0, 0.15);
    border-radius: 10px;
    padding: v-bind(padding);
}
</style>
