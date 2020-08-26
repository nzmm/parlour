<script lang="ts">
    import { createDebouncer } from '../core/utils';
    import { enqueue, setArtistDetailsView, setAlbumDetailsView } from '../core/actions';
    import { search } from '../core/api/queries';
    import { SearchGroups } from '../core/enums/SearchGroups';
    import type { ITrack } from '../core/interfaces/ITrack';
    import type { AudioPlayer } from '../core/audio/player';
    import SearchInput from "./common/SearchInput.svelte";

    export let player: AudioPlayer;

    let matches: ITrack[] = [];
    const debounce = createDebouncer();

    const onInput = (event: InputEvent) => {
        const target = event.target as HTMLInputElement;
        debounce(async () => {
            const res = await search(target.value);
            const data = await res.json();
            matches = data.matches;
        });
    }

    const onSelect = (event: CustomEvent) => {
        const data = event.detail;

        switch (data.group) {
            case SearchGroups.Artists:
                setArtistDetailsView(data);
                break;
            case SearchGroups.Releases:
                setAlbumDetailsView(data);
                break;
            case SearchGroups.Tracks:
                enqueue(player, event.detail);
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
        width: 35vw;
    }
</style>