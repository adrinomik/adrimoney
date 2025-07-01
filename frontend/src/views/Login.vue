<template>
  <div class="login-container">
    <n-card style="max-width: 350px; margin: 60px auto; padding: 24px;">
      <h2 style="text-align: center; margin-bottom: 20px;">Вход</h2>
      <n-form @submit.prevent="handleLogin">
        <n-form-item label="Имя пользователя">
          <n-input v-model:value="username" placeholder="Введите имя пользователя" />
        </n-form-item>
        <n-form-item label="Пароль">
          <n-input
            v-model:value="password"
            type="password"
            placeholder="Введите пароль"
            show-password-on="mousedown"
          />
        </n-form-item>
        <n-button type="primary" block attr-type="submit">Войти</n-button>
      </n-form>
      <n-alert v-if="message" type="info" style="margin-top: 16px;">
        {{ message }}
      </n-alert>
    </n-card>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { NForm, NFormItem, NInput, NButton, NCard, NAlert } from 'naive-ui'

const username = ref('')
const password = ref('')
const message = ref('')

function handleLogin() {
  // Пока просто показываем сообщение, что вход выполнен
  message.value = `Вход выполнен для пользователя: ${username.value}`
  // Здесь позже будет запрос к backend
}
</script>

<style scoped>
.login-container {
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  background: #f5f7fa;
}
</style>