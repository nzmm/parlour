<script lang="ts">
    import { createDebouncer } from '../core/utils';
    import { filterArtists } from '../core/actions';
    import { search } from '../core/api/queries';
    import { SearchGroups } from '../core/enums/SearchGroups';
    import type { ITrack } from '../core/interfaces/ITrack';
    import SearchInput from "./common/SearchInput.svelte";

    let matches: ITrack[] = [];
    const debounce = createDebouncer();

    const onInput = (event: InputEvent) => {
        const target = event.currentTarget as HTMLInputElement;
        debounce(async () => {
            const res = await search(target.value);
            const data = await res.json();
            matches = data.matches;
            console.log(data);
        });
    }

    const onSelect = (event: CustomEvent) => {
        const data = event.detail;

        switch (data.group) {
            case SearchGroups.Artists:
                //setArtistDetailsView(data);
                break;
            case SearchGroups.Releases:
                //setAlbumDetailsView(data);
                break;
            case SearchGroups.Tracks:
                //enqueue(player, event.detail);
                break;
            default:
                break;
        }
    }

    const groups = {
        [SearchGroups.Artists]: 'Artists',
        [SearchGroups.Releases]: 'Albums',
        [SearchGroups.Tracks]: 'Tracks'
    };

</script>

<SearchInput
    {matches}
    let:match
    class="mx-1"
    grouper="group"
    on:input={onInput}
    on:select={onSelect}>

    <span slot="grouper">
        {groups[match.group]}
    </span>

    <span>{match.name}</span>

</SearchInput>

<style>
    :global(.form-control) {
        width: 25vw;
        min-width: 200px;
    }
</style>