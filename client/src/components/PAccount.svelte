<script lang="ts">
    import { POST } from "../core/api/requests";
    import { user } from "../core/store";
    import Page from "./common/Page.svelte";

    const onRrefreshMusic = async (provider: string) => {
        const res = await POST(`/providers/refresh_music/${provider}/`);
        const data = await res.json();
    }
</script>

<Page>
    <h2 class="border-bottom">Accounts</h2>

    {#if $user}
    <section class="my-4">
        <p class="text-muted">Hi {$user.full_name},</p>
        <p class="text-muted">Here you can manage your content providers.</p>

        <a class="btn btn-success" href="/providers/graph_signin">
            Connect to OneDrive&hellip;
        </a>

        <h4 class="mt-5 mb-3">Your providers</h4>

        <ul class="providers list-group">
            {#each $user.providers as provider}
            <li class="list-group-item">
                {provider.provider}
                <div class="mt-2">
                    <button class="btn btn-sm btn-secondary" on:click={() => onRrefreshMusic(provider.provider)}>
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
