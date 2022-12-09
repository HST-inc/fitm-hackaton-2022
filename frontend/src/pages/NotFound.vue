<template>
    <div class="not-found">
        <h1 class="not-found-link">
            Эта страница не найдена, возможно, вы перешли по неправильной ссылке.
        </h1>
        <a-anchor-link style="padding-left: 0px">
            <router-link to="/">Вернуться на главную страницу</router-link>
        </a-anchor-link>
    </div>
</template>

<style lang="scss" scoped>
.not-found {
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    text-align: center;
    &_link {
        font-size: 40px;
    }
}
</style>
