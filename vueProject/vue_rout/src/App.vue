<template>
  <div id="app">

      <h3>这是主页</h3>
      <router-link to="/home">访问Home组件</router-link>
      <router-link to="/user">访问User组件</router-link>
      <hr>
    <!--   组件对应内容的显示地址   -->
      <router-view></router-view>
  </div>
</template>

<script>
export default {
  name: 'App'
}
</script>

<style>

</style>
