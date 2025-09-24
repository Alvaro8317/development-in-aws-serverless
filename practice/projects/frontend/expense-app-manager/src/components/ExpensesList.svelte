<script>
    import { onMount } from "svelte";
    import { fetchExpenses } from "../utils/api";
    import ExpenseItem from "./ExpenseItem.svelte";

    export let username;
    export let password;

    let expenses = [];
    let loading = true;
    let error = "";

    onMount(async () => {
        try {
            const data = await fetchExpenses(
                "https://q3y1u5zf08.execute-api.us-east-1.amazonaws.com/Prod/spends",
                username,
                password,
            );
            expenses = data.spends?.Items ?? [];
        } catch (e) {
            error = "⚠️ Error al obtener gastos";
        } finally {
            loading = false;
        }
    });
</script>

<section id="expenses" class="px-8 md:px-20 py-16 bg-gray-50">
    <h3 class="text-3xl font-bold text-center mb-12">Latest Expenses</h3>

    {#if loading}
        <p class="text-center text-gray-500">Loading expenses...</p>
    {:else if error}
        <p class="text-center text-red-500">{error}</p>
    {:else if expenses.length === 0}
        <p class="text-center text-gray-500">No expenses found.</p>
    {:else}
        <div class="grid md:grid-cols-3 gap-6">
            {#each expenses as exp (exp.id)}
                <ExpenseItem {exp} />
            {/each}
        </div>
    {/if}
</section>
