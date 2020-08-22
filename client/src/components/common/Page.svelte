<script lang="ts">
    import ScrolledView from './ScrolledView.svelte';

    export let heading: string = "";
    export let subheading: string = "";
    export let wideBody: boolean = false;
</script>

<ScrolledView overflowX="hidden" overflowY="scroll">
    <div class="wrapper mx-2 pt-5 pb-4">
        <header>
            <slot name="header">
                <h2>
                    {heading}

                    <small class="text-muted">
                        {subheading}
                    </small>
                </h2>
            </slot>
        </header>
    </div>

    <div class="wrapper mx-2 {wideBody ? "wide" : ""}">
        <slot />
    </div>
</ScrolledView>

<style>
    .wrapper {
        padding-left: 24px;
        padding-right: 24px;
    }
    .wrapper.wide {
        padding: 0;
    }
    h2 {
        font-weight: bold;
    }
    h2 > small {
        font-size: 18px;
    }
</style>