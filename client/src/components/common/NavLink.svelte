<script lang="ts">
    import { link } from 'svelte-spa-router';
    import active from 'svelte-spa-router/active';

    let className = "";

    export { className as class };
    export let label: string = "";
    export let href: string = "/";
    export let activePath: string = null;
    export let count: number | string = null;
</script>

<a
    {href}
    class="d-flex justify-content-between align-items-center side-nav {className}"
    use:active={activePath}
    use:link>

    {label}

    {#if count != null}
    <span class="badge badge-pill">{count}</span>
    {/if}

</a>

<style type="text/scss">
    @import '../../scss/vars';

    .side-nav {
        width: 280px;
        padding-left: 14px;
        padding-right: 8px;
        padding-top: 5px;
        padding-bottom: 5px;
        margin-bottom: 3px;
        white-space: nowrap;
        overflow: hidden;
        text-overflow: ellipsis;
        display: block;
        color: $colour-grey-dark;
        text-decoration: none;
        transition: background-color .3s;
    }
    .side-nav:hover {
        background-color: $colour-grey-light;
    }
    .side-nav.active {
        background-color: $colour-primary;
        color: $colour-white;
        font-weight: bold;
    }
    .badge {
        background-color: $colour-grey-medium;
        color: $colour-white;
        padding-top: 3px;
        padding-bottom: 4px;
        min-width: 20px;
    }
    .side-nav.active .badge {
        background-color: $colour-white;
        color: $colour-primary;
    }
</style>
