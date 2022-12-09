<template>
    <a-form
        :model="formState"
        name="basic"
        autocomplete="off"
        @finish="onFinish"
        layout="vertical"
        class="form"
    >
        <a-form-item
            label="Логин пользователя"
            name="login"
            :rules="[{ required: true, message: 'Обязательно' }]"
            class="input"
        >
            <a-input v-model:value="formState.login" />
        </a-form-item>

        <a-form-item
            label="Пароль"
            name="password"
            :rules="[{ required: true, message: 'Обязательно' }]"
            class="input"
        >
            <a-input-password v-model:value="formState.password" />
        </a-form-item>

        <a-form-item name="remember">
            <a-checkbox v-model:checked="formState.remember">Запомнить пароль</a-checkbox>
        </a-form-item>

        <a-form-item>
            <a-button type="primary" html-type="submit">Войти</a-button>
        </a-form-item>

        <a-anchor-link href="register" style="padding-left: 0px">
            <router-link to="/register">Ещё нет аккаунта?</router-link>
        </a-anchor-link>
    </a-form>
</template>

<script lang="ts">
import { ISignIn } from '@/models/auth';
import { defineComponent, reactive } from 'vue';

export type SignInFormState = ISignIn;
export default defineComponent({
    setup(_, context) {
        const formState = reactive<SignInFormState>({
            login: '',
            password: '',
            remember: true
        });
        const onFinish = (values: any) => {
            context.emit('signin', values);
        };
        const link = import.meta.env.BASE_URL;
        const handleRegisterLickClick = (e: Event) => {
            e.preventDefault();
        };
        return {
            formState,
            onFinish
        };
    }
});
</script>

<style lang="scss" scoped>
.form {
    display: flex;
    flex-direction: column;
    align-items: center;
}
.input {
    margin-top: 20px;
    width: 100%;
}
</style>
