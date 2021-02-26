<script lang="ts">
    import { push } from "svelte-spa-router";
    import { createDebouncer } from "../core/utils";
    import { setArtistBreadcrumbs, setAlbumBradcrumbs } from "../core/actions";
    import { search } from "../core/api/queries";
    import { SearchGroups } from "../core/enums/SearchGroups";
    import type { ITrack } from "../core/interfaces/ITrack";
    import SearchInput from "./common/SearchInput.svelte";

    let matches: ITrack[] = [];
    const debounce = createDebouncer();

    const onInput = (event: InputEvent) => {
        const target = event.currentTarget as HTMLInputElement;

        debounce(async () => {
            if (!target.value.length) {
                return;
            }

            const res = await search(target.value);
            const data = await res.json();
            matches = data.matches;
        });
    };

    const onSelect = (event: CustomEvent) => {
        const data = event.detail;

        switch (data.group) {
            case SearchGroups.Artists:
                setArtistBreadcrumbs(data.id, data.name);
                push(`/artists/${data.id}`);
                break;
            case SearchGroups.Releases:
                setAlbumBradcrumbs(data.id, data.name);
                push(`/albums/${data.id}`);
                break;
            case SearchGroups.Tracks:
                setAlbumBradcrumbs(data.release_id, data.name);
                push(`/albums/${data.release_id}`).then(() => {
                    setTimeout(() => {
                        document.getElementById(`track:${data.id}`)?.focus();
                    }, 350);
                });
                break;
            default:
                break;
        }
    };

    const onClear = () => {
        setTimeout(() => push("/"), 100);
    };

    const groups = {
        [SearchGroups.Artists]: "Artists",
        [SearchGroups.Releases]: "Albums",
        [SearchGroups.Tracks]: "Tracks",
    };
</script>

<SearchInput
    {matches}
    let:match
    class="mx-1"
    grouper="group"
    placeholder="Search here..."
    on:input={onInput}
    on:select={onSelect}
    on:clear={onClear}
>
    <span slot="grouper">
        {groups[match.group]}
    </span>

    <span>{match.name}</span>
</SearchInput>

<style>
    :global(.form-control) {
        width: 30vw;
        min-width: 200px;
    }
</style>
