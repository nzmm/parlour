<script lang="ts">
    import { POST } from "../core/api/requests";
    import { user } from "../core/store";
    import Page from "./common/Page.svelte";
    import type { IProvider } from "../core/interfaces/IProvider";

    const onRrefreshMusic = async (provider: IProvider) => {
        const res = await POST(`/providers/${provider.id}/refresh_music/`);
        //const data = await res.json();
    }

    const onRrefreshThumbs = async (provider: IProvider) => {
        const res = await POST(`/providers/${provider.id}/refresh_thumbs/`);
        //const data = await res.json();
    }
</script>

<Page>
    <h2 class="border-bottom">Account</h2>

    {#if $user}
    <section class="my-4">
        <p class="text-muted">Hi {$user.first_name},</p>
        <p class="text-muted">Here you can connect to and manage your content providers.</p>

        <h4 class="mt-5 mb-3">Content providers</h4>

        <ul class="providers list-group">
            {#each $user.providers as provider}
            <li class="list-group-item d-flex justify-content-between align-items-center">
                <div class="d-flex">
                    <img src={provider.brand} height="40" width="50" alt="OneDrive" class="mr-3" />
                    <div>
                        <h6 class="p-0 m-0">{provider.title}</h6>
                        <span class="text-muted">This provider contributes $N tracks to your collection</span>
                    </div>
                </div>
                <div>
                    {#if provider.id}
                    <button class="btn btn-sm btn-secondary" on:click={() => onRrefreshMusic(provider)}>
                        Refresh music
                    </button>
                    <button class="btn btn-sm btn-secondary" on:click={() => onRrefreshThumbs(provider)}>
                        Refresh art
                    </button>
                    <a class="btn btn-sm btn-danger" href="/providers/{provider.provider}_signout">
                        Revoke
                    </a>
                    {:else}
                    <a class="btn btn-sm btn-success" href="/providers/{provider.provider}_signin">
                        Connect&hellip;
                    </a>
                    {/if}
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
    .providers img {
        object-fit: contain;
    }
</style>