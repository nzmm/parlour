import { queue, currentTrack, currentView } from './store';
import { setLiked } from '../core/api/commands';
import { PlaybackState } from "./enums/PlaybackState";
import type { ITrack } from "./interfaces/ITrack";
import type { AudioPlayer } from "./audio/player";
import type { SublevelViews } from './enums/SublevelViews';


const enqueueWithMethod = (player: AudioPlayer, track: ITrack, method: (data: ITrack[]) => void) => {
    if (player.state === PlaybackState.Stopped) {
        player.play(track);
    } else {
        queue.update(q => {
            method(q.data);
            return q;
        });
    }
}

export const enqueue = (player: AudioPlayer, track: ITrack) => {
    enqueueWithMethod(player, track, data => data.push(track));
}

export const enqueueNext = (player: AudioPlayer, track: ITrack) => {
    enqueueWithMethod(player, track, data => data.splice(0, 0, track));
}

export const playNow = (player: AudioPlayer, track: ITrack) => {
    player.play(track);
}

export const likeTrack = async (track: ITrack) => {
    const liked = !track.liked;
    const res = await setLiked(track.id, liked);
    const data = await res.json();

    if (!data.success) {
        return;
    }

    currentTrack.update(cur => ({
        ...cur, liked
    }));
}

export const setDetailsView = (sublevel: SublevelViews, data: any) => {
    currentView.update(cur => ({
        ...cur,
        sublevel,
        data
    }));
}

export const goBack = () => setDetailsView(null, null);