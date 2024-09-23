<script setup>
</script>

<template>
  <header>
    <img alt="Parking Management" class="logo" src="./assets/logo.svg" width="125" height="125" />

    <nav>
      <ul>
        <li><router-link to="/">Operação</router-link></li>
        <li><router-link to="/vehicles">Veículos</router-link></li>
        <li><router-link to="/customers">Clientes</router-link></li>
        <li><router-link to="/plans">Planos</router-link></li>
        <li><router-link to="/contracts">Contratos</router-link></li>
      </ul>
    </nav>
  </header>

  <main>
    <!-- This will render the matched component based on the route -->
    <router-view></router-view>
  </main>
</template>

<style scoped>
/* General header styling */
header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 1rem;
  background-color: #2c3e50;
  color: #fff;
}

.logo {
  margin-right: 2rem;
}

/* Navigation menu styling */
nav ul {
  list-style: none;
  display: flex;
  gap: 1.5rem;
  padding: 0;
}

nav li {
  margin: 0;
}

nav a {
  color: #fff;
  text-decoration: none;
  font-weight: bold;
}

nav a.router-link-exact-active {
  text-decoration: underline;
}

/* Main content styling */
main {
  padding: 2rem;
  background-color: #ecf0f1;
  min-height: 100vh;
}

/* Responsive styles */
@media (max-width: 768px) {
  header {
    flex-direction: column;
    align-items: flex-start;
  }

  nav ul {
    flex-direction: column;
    gap: 1rem;
  }

  .logo {
    margin-bottom: 1rem;
  }
}
</style>
