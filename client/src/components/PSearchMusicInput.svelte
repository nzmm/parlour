<script lang="ts">
    import { createDebouncer } from '../core/utils';
    import { enqueue } from '../core/actions';
    import { search } from '../core/api/queries';
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
        enqueue(player, event.detail);
    }
</script>

<SearchInput
    {matches}
    let:match
    on:input={onInput}
    on:select={onSelect}>

    <span>{match.name}</span>

</SearchInput>
