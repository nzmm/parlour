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

const enqueueWithMethod = (player: AudioPlayer, tracks: ITrack[], method: (data: ITrack[]) => void) => {
    if (player.state === PlaybackState.Stopped) {
        player.play(tracks.shift());
    }
    queue.update(q => {
        method(q);
        return q;
    });
}

export const enqueue = (player: AudioPlayer, tracks: ITrack[]) => {
    tracks = [...tracks];
    enqueueWithMethod(player, tracks, data => data.push(...tracks));
}

export const enqueueNext = (player: AudioPlayer, tracks: ITrack[]) => {
    tracks = [...tracks];
    enqueueWithMethod(player, tracks, data => data.splice(0, 0, ...tracks));
}

export const playNow = (player: AudioPlayer, tracks: ITrack[]) => {
    tracks = [...tracks];
    player.play(tracks.shift());
    enqueueNext(player, tracks);
}