<template>
    <paper class="sign-in" padding="30px">
        <sign-in-form @signin="onSignIn"></sign-in-form>
    </paper>
</template>

<script setup lang="ts">
import { signIn } from '@/api/auth';
import SignInForm, { SignInFormState } from '@/components/forms/SignInForm.vue';
import Paper from '@/components/Paper.vue';
import { useQuery } from 'vue-query';

const onSignIn = async (values: SignInFormState) => {
    useQuery('signin', () => signIn(values));
};
</script>

<style scoped lang="scss">
.sign-in {
    position: absolute;
    left: 50%;
    top: 50%;
    transform: translate(-50%, -50%);
}
</style>
