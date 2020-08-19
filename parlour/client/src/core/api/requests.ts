export async function GET(url: string) {
    return fetch(url)
        .then(response => {
            return response;
        })
        .catch(error => {
            console.error(error);
            return error;
        });
}
