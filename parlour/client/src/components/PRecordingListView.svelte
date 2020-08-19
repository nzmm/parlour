<script lang="ts">
    import ScrolledView from "./common/ScrolledView.svelte";
    import PCoverArt from "./PCoverArt.svelte";

    export let heading = "";
    export let subheading = "";
    export let items = [
        {title: '1'},
        {title: '2'},
        {title: '3'},
        {title: '4'},
        {title: '5'},
        {title: '6', playing: true},
        {title: '7'},
        {title: '8'},
        {title: '9'},
        {title: '10'},
        {title: '10'},
        {title: '10'},
        {title: '10'},
        {title: '10'},
        {title: '10'},
        {title: '10'},
        {title: '10'},
        {title: '10'},
        {title: '10'},
        {title: '10'},
        {title: '10'},
        {title: '10'},
        {title: '10'},
        {title: '10'},
        {title: '10'},
        {title: '10'},
        {title: '10'},
        {title: '10'},
        {title: '10'},
        {title: '10'},
        {title: '10'},
        {title: '10'},
        {title: '10'},
        {title: '10'},
        {title: '10'},
        {title: '10'},
        {title: '10'},
        {title: '10'},
        {title: '10'},
        {title: '10'},
        {title: '10'},
        {title: '10'},
        {title: '10'},
    ];
</script>

<ScrolledView overflowX="hidden" overflowY="scroll">
    <header class="px-2 pt-5">
        <h2>
            {heading}

            <small class="text-muted">
                {subheading}
            </small>
        </h2>
    </header>

    <div class="list px-2 py-4">
        {#each items as item}
        <button class="item d-flex py-2">
            <div class="playing">
                {#if item.playing}
                    <i class="fas fa-play"></i>
                {/if}
            </div>
            <div class="title">
                {item.title}
            </div>
        </button>
        {/each}
    </div>
</ScrolledView>

<style>
    h2 {
        padding-left: 24px;
        font-weight: bold;
    }
    h2 > small {
        font-size: 16px;
    }
    .item {
        width: 100%;
        margin: 0;
        padding-left: 24px;
        padding-right: 24px;
        background: transparent;
        border: 0;
        outline: 0;
    }
    .item:nth-child(odd) {
        background-color: #eee;
    }
    .item:focus {
        background-color: #ff2a2aff;
        color: #fff;
    }
    .item > .playing {
        text-align: left;
        width: 28px;
    }
</style>