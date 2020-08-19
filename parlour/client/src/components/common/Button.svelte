<script lang="ts">
    let className = "";

    export { className as class };
//    export let active = false;
</script>

<button class="btn {className}">
    <slot/>
</button>