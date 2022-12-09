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
            label="Имя"
            name="name"
            :rules="[{ required: true, message: 'Обязательно' }]"
            class="form-element"
        >
            <a-input v-model:value="formState.name" />
        </a-form-item>

        <a-form-item
            label="Фамилия"
            name="secondName"
            :rules="[{ required: true, message: 'Обязательно' }]"
            class="form-element"
        >
            <a-input v-model:value="formState.secondName" />
        </a-form-item>

        <a-form-item label="Отчество" name="patronymic" class="form-element">
            <a-input v-model:value="formState.patronymic" />
        </a-form-item>

        <a-form-item
            label="Логин"
            name="login"
            :rules="[{ required: true, message: 'Обязательно' }]"
            class="form-element"
        >
            <a-input v-model:value="formState.login" />
        </a-form-item>

        <a-form-item
            label="Пароль"
            name="password"
            :rules="[{ required: true, message: 'Обязательно' }]"
            class="form-element"
        >
            <a-input-password v-model:value="formState.password" />
        </a-form-item>

        <a-form-item label="Пол" required class="form-element">
            <a-select v-model:value="formState.sex">
                <a-select-option value="male">Мужчина</a-select-option>
                <a-select-option value="female">Женщина</a-select-option>
            </a-select>
        </a-form-item>

        <a-form-item
            name="birthday"
            label="Дата рождения"
            :rules="[{ required: true, message: 'Обязательно' }]"
            class="form-element"
        >
            <a-date-picker
                style="width: 100%"
                v-model:value="formState.birthday"
                value-format="YYYY-MM-DD"
                placeholder=""
            />
        </a-form-item>

        <a-form-item
            label="Серия"
            name="passport.series"
            :rules="[{ required: true, message: 'Обязательно' }]"
            class="form-element"
        >
            <a-input v-model:value="formState.passport.series" />
        </a-form-item>

        <a-form-item
            label="Номер паспорта"
            name="passport.number"
            :rules="[{ required: true, message: 'Обязательно' }]"
            class="form-element"
        >
            <a-input v-model:value="formState.passport.number" />
        </a-form-item>

        <a-form-item
            label="Телефон"
            name="phone"
            class="form-element"
            :rules="[{ required: true, message: 'Обязательно' }]"
        >
            <a-input v-model:value="formState.phone" />
        </a-form-item>

        <a-form-item
            label="СНИЛС"
            name="snils"
            class="form-element"
            :rules="[{ required: true, message: 'Обязательно' }]"
        >
            <a-input v-model:value="formState.snils" />
        </a-form-item>

        <a-form-item class="submit-button">
            <a-button type="primary" html-type="submit">Зарегистрироваться</a-button>
        </a-form-item>

        <a-anchor-link href="login" style="padding-left: 0px">
            <router-link to="/login">Уже есть аккаунт?</router-link>
        </a-anchor-link>
    </a-form>
</template>

<script lang="ts">
import { defineComponent, reactive } from 'vue';
import { ISignUp } from '@/models/auth';

export type SignUpFormState = ISignUp;
export default defineComponent({
    setup(_, context) {
        const formState = reactive<SignUpFormState>({
            login: '',
            password: '',
            name: '',
            secondName: '',
            patronymic: '',
            birthday: new Date(Date.now()).toString(),
            sex: 'male',
            phone: '',
            snils: '',
            passport: {
                series: '',
                number: ''
            }
        });
        const onFinish = (values: any) => {
            context.emit('signup', values);
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
.form-element {
    margin-bottom: 10px;
    width: 100%;
}
.submit-button {
    margin-top: 30px;
}
</style>
