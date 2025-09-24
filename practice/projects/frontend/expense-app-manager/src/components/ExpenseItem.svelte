<script>
    export let exp;
</script>

<div class="p-6 shadow-md rounded-xl bg-white hover:shadow-xl transition">
    <h4 class="text-xl font-semibold text-gray-800">{exp.name}</h4>
    <p class="text-gray-500">{exp.description}</p>
    <p class="mt-3 text-lg font-bold text-green-600">
        ${exp.amount.toLocaleString()}
    </p>
    <p class="text-sm text-gray-400 mt-1">📅 {exp.datetime_spend}</p>
</div>
