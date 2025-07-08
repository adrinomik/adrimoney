<template>
  <div style="max-width: 1200px; margin: 0 auto;">
    <h1>Playground</h1>
    <p>Счетчик: {{ count }}</p>

    <button @click="increment" :disabled="count >= 10">Увеличить</button>
    <button @click="decrement" :disabled="count <= -5">Уменьшить</button>
    <button @click="reset">Сбросить</button>

    
  </div>
</template>

<script setup>
import { ref } from 'vue'

const count = ref(0)

function reset() {
    count.value = -2
}

function increment() {
    if (count.value < 10) {
        count.value++
    }
}

function decrement() {
    if (count.value > -5) {
        count.value--
    }
}

</script>
