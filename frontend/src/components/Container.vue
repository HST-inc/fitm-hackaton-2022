<template>
    <div class="container">
        <slot></slot>
    </div>
</template>

<style land="scss" scoped>
.container {
    width: 100%;
}
@media screen and (max-width: 420px) {
    .container {
        padding: 20px;
    }
}
</style>
