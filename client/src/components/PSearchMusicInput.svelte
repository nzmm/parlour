<script lang="ts">
    import { createDebouncer } from '../core/utils';
    import { search } from '../core/api/queries';
    import type { ITrack } from '../core/interfaces/ITrack';

    import SearchInput from "./common/SearchInput.svelte";

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
</script>

<SearchInput
    {matches}
    let:match
    on:input={onInput}>

    <span>{match.name}</span>

</SearchInput>
