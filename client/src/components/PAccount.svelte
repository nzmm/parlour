<script lang="ts">
    import { POST } from "../core/api/requests";
    import { user } from "../core/store";
    import Page from "./common/Page.svelte";

    const onRrefreshMusic = async (provider_id: number) => {
        const res = await POST(`/providers/${provider_id}/refresh_music/`);
        const data = await res.json();
    }
</script>

<Page>
    <h2 class="border-bottom">Account</h2>

    {#if $user}
    <section class="my-4">
        <p class="text-muted">Hi {$user.full_name},</p>
        <p class="text-muted">Here you can manage your content providers.</p>

        <a class="btn btn-success" href="/providers/graph_signin">
            Connect to OneDrive&hellip;
        </a>

        <h4 class="mt-5 mb-3">Your providers</h4>

        <ul class="providers list-group">
            {#each $user.providers.filter(p => p.provider === "graph") as provider}
            <li class="list-group-item d-flex justify-content-between align-items-center">
                <div class="d-flex">
                    <img src="/static/data/im/onedrive.svg" height="40" alt="OneDrive" class="mr-3" />
                    <div>
                        <h6 class="p-0 m-0">Microsoft OneDrive</h6>
                        <span class="text-muted">This provider contributes 1000 tracks to your collection</span>
                    </div>
                </div>
                <div>
                    <button class="btn btn-sm btn-secondary" on:click={() => onRrefreshMusic(provider.id)}>
                        Refresh music
                    </button>
                    <button class="btn btn-sm btn-secondary">
                        Refresh art
                    </button>
                    <a class="btn btn-sm btn-danger" href="/providers/graph_signout">
                        Revoke access
                    </a>
                </div>
            </li>
            {/each}
        </ul>
    </section>
    {/if}
</Page>

<style lang="scss">
    h6 {
        font-weight: bold;
    }
</style>