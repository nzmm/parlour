<script lang="ts">
    import { createEventDispatcher, SvelteComponent } from 'svelte';
    import DropdownMenu from './DropdownMenu.svelte';

    let className = "";
    let value = '';
    let focus = false;

    let container: HTMLElement;
    let input: HTMLElement;
    let items: HTMLElement[] = [];

    export { className as class };
    export let matches = [];
    export let grouper: string = null;

    $: visible = focus && value.length > 0 && matches.length > 0;

    const dispatch = createEventDispatcher();

    const onKeyDown = (event: KeyboardEvent) => {
        if (!event.shiftKey && (event.keyCode === 9 || event.keyCode === 40)) {
            // tab or down-arrow
            event.preventDefault();
            items[0].focus();
            return false;
        }
    }

    const cycle = (event: KeyboardEvent, i: number) => {
        const up = event.keyCode === 38;
        const down = event.keyCode === 40;

        if (!(up || down)) {
            return;
        }

        event.preventDefault();

        let j: number;
        if (up && i === 0) {
            j = matches.length - 1;
        }
        else if (down && i === matches.length - 1) {
            j = 0;
        }
        else {
            j = up ? i-1 : i+1;
        }

        items[j]?.focus();
    }

    const onBlur = () => {
        setTimeout(() => {
            focus = container.contains(document.activeElement);
        }, 50);
    }

    const clear = () => {
        value = "";
        items = [];
        dispatch("clear");
    }
</script>

<div class="p-search {className}" class:active={visible} bind:this={container}>
    <input
        type="text"
        class="form-control pr-4"
        placeholder="Search here..."
        bind:this={input}
        bind:value={value}
        on:focus={() => focus = true}
        on:blur={onBlur}
        on:keydown={onKeyDown}
        on:input />

    {#if value}
    <a class="clear" href="#clear" on:click={clear} title="Clear">
        <i class="pr-2 fas fa-times"></i>
    </a>
    {:else}
    <a class="clear" href="#search" on:click={() => input.focus()} title="Search here...">
        <i class="pr-2 fas fa-search"></i>
    </a>
    {/if}

    <DropdownMenu
        {visible}
        interceptor={false}
        dropshadowSize="small"
        on:hide={() => focus = false}>

        {#each matches as match, i}

        {#if grouper && match[grouper] !== matches[i-1]?.[grouper]}
        <h6 class="dropdown-header">
            <slot name="grouper">
                {match[grouper]}
            </slot>
        </h6>
        {/if}

        <a tabindex="0"
            class="dropdown-item"
            href="#match"
            bind:this={items[i]}
            on:click={() => dispatch("select", match)}
            on:keydown={e => cycle(e, i)}
            on:blur={onBlur}>

            <slot {match} />
        </a>
        {/each}
    </DropdownMenu>
</div>

<style>
    .p-search {
        position: relative;
    }
    .p-search :global(.p-drop-menu) {
        top: calc(100% - 4px);
        width: 100%;
        border-top-left-radius: 0 !important;
        border-top-right-radius: 0 !important;
    }
    i {
        position: absolute;
        top: 0;
        bottom: 0;
        right: 0;
        opacity: .25;
        color: #000;
    }
    i::before {
        vertical-align: -65%;
    }
    .form-control {
        width: 350px;
    }
    .form-control::placeholder {
        font-style: italic;
        color: #aaa;
    }
    .dropdown-item:focus {
        outline: 0;
        background-color: #ff2a2aff;
        color: #fff;
    }
</style>