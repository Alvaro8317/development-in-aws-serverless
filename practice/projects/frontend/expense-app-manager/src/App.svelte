<script>
  import heroImage from "./assets/money.svg";
  import ExpensesList from "./components/ExpensesList.svelte";

  const utf8ToB64 = (str) => {
    const utf8Bytes = new TextEncoder().encode(str); // Uint8Array
    let binary = "";
    utf8Bytes.forEach((b) => (binary += String.fromCharCode(b)));
    return btoa(binary);
  };

  let username = "";
  let password = "";
  let isAuthenticated = false;
  let authError = "";

  async function login() {
    const credentials = utf8ToB64(`${username}:${password}`);
    try {
      const res = await fetch(
        "https://q3y1u5zf08.execute-api.us-east-1.amazonaws.com/Prod/spends",
        {
          headers: {
            Authorization: `Basic ${credentials}`,
          },
        },
      );

      if (res.status === 401) {
        authError = "❌ Credenciales inválidas. Intenta de nuevo.";
        return;
      }

      if (!res.ok) {
        const text = await res.text();
        authError =
          "⚠️ Error al autenticar. Código: " +
          res.status +
          ", Detalles: " +
          text;
        return;
      }

      isAuthenticated = true;
      authError = "";
    } catch (e) {
      console.error(e);
      authError = "⚠️ Error de conexión con el servidor.";
    }
  }
</script>

<main class="font-sans text-gray-800">
  <!-- Navbar -->
  <header class="flex justify-between items-center p-6 bg-white shadow-md">
    <h1 class="text-2xl font-bold text-green-600">Expense Manager</h1>
    <nav class="space-x-6 hidden md:flex">
      <a href="#features" class="hover:text-green-600">Features</a>
      <a href="#about" class="hover:text-green-600">About</a>
      <a href="#download" class="hover:text-green-600">Download</a>
    </nav>
  </header>

  <!-- Hero -->
  <section
    class="flex flex-col-reverse md:flex-row items-center justify-between px-8 md:px-20 py-16 bg-gradient-to-r from-green-50 to-green-100"
  >
    <div class="max-w-lg">
      <h2 class="text-4xl md:text-5xl font-bold leading-tight mb-6">
        Take control of your <span class="text-green-600">finances</span> today
      </h2>
      <p class="text-lg text-gray-600 mb-8">
        Track expenses, set budgets, and reach your goals with Expense Manager.
      </p>
    </div>
    <img
      src={heroImage}
      alt="Finance illustration"
      class="w-14 md:w-46 mx-auto md:mx-0"
    />
  </section>

  {#if !isAuthenticated}
    <section class="px-8 md:px-20 py-16 bg-white max-w-md mx-auto">
      <h3 class="text-2xl font-bold mb-6 text-center">🔐 Login</h3>
      <input
        type="text"
        placeholder="Usuario"
        bind:value={username}
        class="w-full p-3 mb-4 border rounded-lg"
      />
      <input
        type="password"
        placeholder="Contraseña"
        bind:value={password}
        class="w-full p-3 mb-4 border rounded-lg"
      />
      <button
        on:click={login}
        class="w-full bg-green-600 text-white px-6 py-3 rounded-lg font-semibold hover:bg-green-700"
      >
        Ingresar
      </button>
      {#if authError}
        <p class="text-red-500 mt-4 text-center">{authError}</p>
      {/if}
    </section>
  {:else}
    <ExpensesList {username} {password} />
  {/if}
</main>
