import { queue } from './store';
import { PlaybackState } from "./enums/PlaybackState";
import type { ITrack } from "./interfaces/ITrack";
import type { AudioPlayer } from "./audio/player";


export function shuffleSelection<T>(array: T[]): T[] {
    // Fisher-Yates shuffle
    const shuffled = [...array];
    for(let i = shuffled.length - 1; i > 0; i--){
        const j = Math.floor(Math.random() * i)
        const temp = shuffled[i]
        shuffled[i] = shuffled[j]
        shuffled[j] = temp
    }
    return shuffled;
}

const enqueueWithMethod = (player: AudioPlayer, track: ITrack, method: (data: ITrack[]) => void) => {
    if (player.state === PlaybackState.Stopped) {
        player.play(track);
    } else {
        queue.update(q => {
            method(q);
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

export const playNow = (player: AudioPlayer, track: ITrack, playlist: ITrack[] = []) => {
    if (player.state === PlaybackState.Stopped && !player.queue.length && playlist.length) {
        console.log(track.id, playlist);
        queue.set(shuffleSelection(playlist.filter(t => t.id !== track.id)));
    }
    player.play(track);
}