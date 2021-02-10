import { getChannels, getCurrentUser, getLibrary } from "./api/queries";
import { library, artists, channels } from "./store";

const initUser = async () => {
    const res = await getCurrentUser();
    const data = await res.json();
    return data.user;
}

const initLibrary = async () => {
    const res = await getLibrary();
    const data = await res.json();
    artists.set(data.artists);
    library.set(data.releases);
    return data.track_count;
}

const initChannels = async () => {
    const res = await getChannels();
    const data = await res.json();
    channels.set(data.channels);
    return data.channels.length;
}

export const bootstrapTW = async () => {
    const [user, trackCount, ] = await Promise.all([initUser(), initLibrary(), initChannels()]);
    return { user, trackCount };
}

