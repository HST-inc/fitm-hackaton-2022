<template>
    <paper v-if="width > 420" class="sign-up" padding="30px">
        <SignUpForm @signup="onSignUp"></SignUpForm>
    </paper>
    <SignUpFormMobile v-else></SignUpFormMobile>
</template>

<script setup lang="ts">
import { signUp } from '@/api/auth';
import SignUpForm, { SignUpFormState } from '@/components/forms/SignUpForm.vue';
import SignUpFormMobile from '@/components/forms/SignUpFormMobile.vue';
import Paper from '@/components/Paper.vue';
import { onMounted, onUnmounted, ref } from 'vue';
import { useQuery } from 'vue-query';

let width = ref(window.innerWidth);
function setWidth() {
    width.value = window.innerWidth;
}

onMounted(() => {
    window.addEventListener('resize', setWidth);
});

onUnmounted(() => {
    window.removeEventListener('resize', setWidth);
});

const onSignUp = async (values: SignUpFormState) => {
    useQuery('signup', () => signUp(values));
};
</script>

<style scoped lang="scss">
.sign-up {
    position: absolute;
    left: 50%;
    top: 50%;
    transform: translate(-50%, -50%);
}
</style>
